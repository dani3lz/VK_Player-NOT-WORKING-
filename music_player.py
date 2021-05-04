from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtGui import QPixmap, QIcon
from playerUI import Ui_MainWindow
from loginUI import Ui_SecondWindow
import captchaUI
from PyQt5.QtCore import QUrl, QTimer, Qt
import vk_api
from vk_api import audio
import time
import os
import sys
import requests
import json


def suppress_qt_warnings():
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"


# MAIN WINDOW ----------------------------------------------------------------------------------------------------------
class PlayerWindow(QMainWindow):
    def __init__(self):
        super(PlayerWindow, self).__init__()

        # Setup main window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("VK PLayer by dani3lz")
        self.setWindowIcon(QIcon('icon.ico'))

        # Setup music elements Nr.1
        self.volume = 50
        self.titles = []
        self.artists = []

        # Read file with songs
        self.readSongs()

        # Setup music elements Nr.2
        self.isPlaying = False
        self.ui.musicSlider.setPageStep(0)
        self.valueSlider = 0
        self.currentIndex = -1
        self.newIndex = 1
        self.playlist.setPlaybackMode(3)
        self.ui.listWidget.setCurrentRow(0)

        # Check if exist first song in file
        try:
            self.settings_read()
            self.ui.infoLabel.setText(self.titles[self.row] + " - " + self.artists[self.row])
            self.player.playlist().setCurrentIndex(self.row)
            self.ui.listWidget.setCurrentRow(self.row)
        except Exception as e:
            self.row = 0

        # Volume and duration labels
        self.ui.durationLabel.setText("0:00 / 0:00")
        self.ui.volumeLabel.setText("Volume: " + str(self.volume))

        # Connect buttons
        self.ui.playButton.clicked.connect(self.play)
        self.ui.nextButton.clicked.connect(self.next)
        self.ui.prevButton.clicked.connect(self.prev)
        self.ui.shuffleButton.clicked.connect(self.shuffleMode)
        self.ui.repeatThis.clicked.connect(self.repeatThisMode)
        self.ui.repeatOnce.clicked.connect(self.repeatOnceMode)
        self.ui.refreshButton.clicked.connect(self.refreshMode)

        # Music slider bar connect
        self.ui.musicSlider.actionTriggered.connect(self.sliderValue)
        self.ui.listWidget.itemClicked.connect(self.changeSong)

        # Volume slider bar connect
        self.ui.volumeSlider.setValue(self.volume)
        self.ui.volumeSlider.actionTriggered.connect(self.setVolume)

        # Setup timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_hit)
        self.timer.start(int(1000 / 60))

    # Refresh button
    def refreshMode(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Advertisement")
        self.msg.setText("This function may take a long time, please don't close the application. "
                    "It depends on  the number of songs in your playlist. "
                    "Please insert your username, password and VK ID. Here you can get your ID: "
                    "<a href='https://regvk.com/id/'>https://regvk.com/id/</a>")
        self.msg.show()
        self.msg.raise_()
        self.setEnabled(False)
        logwin.show()

    # Convert duration of song to minutes and seconds
    def convertMillis(self, millis):
        seconds = (millis / 1000) % 60
        minutes = (millis / (1000 * 60)) % 60
        return minutes, seconds

    # Volume slider
    def setVolume(self):
        self.volume = self.ui.volumeSlider.value()
        self.player.setVolume(self.volume)
        self.ui.volumeLabel.setText("Volume: " + str(self.volume))

    # Change music using the list
    def changeSong(self):
        self.row = self.ui.listWidget.currentRow()
        self.player.playlist().setCurrentIndex(self.row)
        if not self.isPlaying:
            self.player.play()
            self.ui.playButton.setText("Pause")
            self.isPlaying = True

    # Music slider
    def sliderValue(self):
        self.player.setVolume(0)
        self.valueSlider = self.ui.musicSlider.value()
        self.player.setPosition(self.valueSlider)
        self.player.setVolume(self.volume)

    # Read information about volume and row
    def settings_read(self):
        try:
            with open("settings.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            for i in data["Settings"]:
                self.volume = i["Volume"]
                self.row = i["Row"]
        except Exception as e:
            pass

    # Write information about volume and row
    def settings_write(self):
        settings_list = {}
        settings_list["Settings"] = []
        settings_list["Settings"].append({
            "Volume": self.volume,
            "Row": self.row
        })
        with open("settings.json", "w", encoding="utf-8") as f:
            json.dump(settings_list, f, indent=4)

    # Timer
    def time_hit(self):
        if not captchawin.isVisible():
            try:
                os.remove("captcha.png")
            except Exception as e:
                pass
        if self.first and not logwin.isVisible():
            self.close()
            captchawin.close()
        if not self.isEnabled() and not logwin.isVisible():
            self.setEnabled(True)

        if self.isPlaying:
            self.ui.musicSlider.setMaximum(self.player.duration())
            self.ui.musicSlider.setValue(self.player.position())
            self.row = self.ui.listWidget.currentRow()
            self.ui.infoLabel.setText(str(self.titles[self.row]) + " - " + str(self.artists[self.row]))
            self.newIndex = self.player.playlist().currentIndex()
            self.checkList()

            song_min, song_sec = self.convertMillis(int(self.player.duration()))
            if song_sec < 10:
                self.song_duration = "{0}:0{1}".format(int(song_min), int(song_sec))
            else:
                self.song_duration = "{0}:{1}".format(int(song_min), int(song_sec))

            now_min, now_sec = self.convertMillis(int(self.ui.musicSlider.value()))
            if now_sec < 10:
                self.now_duration = "{0}:0{1}".format(int(now_min), int(now_sec))
            else:
                self.now_duration = "{0}:{1}".format(int(now_min), int(now_sec))

            self.ui.durationLabel.setText(str(self.now_duration) + " / " + str(self.song_duration))

            if self.ui.repeatOnce.text() == "Repeat Once: On":
                if self.now_duration == self.song_duration:
                    self.ui.playButton.setText("Play")
                    self.isPlaying = False
                    self.player.stop()
        self.settings_write()

    # Sets the current position in the list
    def checkList(self):
        if self.currentIndex == self.newIndex:
            pass
        else:
            self.ui.listWidget.setCurrentRow(self.player.playlist().currentIndex())
            self.currentIndex = self.newIndex

    # Read file with songs
    def readSongs(self):
        self.ui.listWidget.clear()
        self.artists.clear()
        self.titles.clear()
        self.setWindowTitle("VK Player by dani3lz")
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist(self.player)
        self.first = False
        try:
            with open("songs.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            for i in data["Songs"]:
                # link
                self.url = i["url"]
                self.playlist.addMedia(QMediaContent(QUrl(self.url)))
                # title
                self.titleSong = i["title"]
                self.titles.append(i["title"])
                # artist
                self.artistSong = i["artist"]
                self.artists.append(i["artist"])
                self.ui.listWidget.addItem(str(i["id"]) + ". " + self.titleSong + " - " + self.artistSong)
            self.ui.infoLabel.setText(self.titles[0] + " - " + self.artists[0])
        except Exception as e:
            print(str(e))
            self.setEnabled(False)
            self.first = True
            logwin.show()
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Advertisement")
            self.msg.setText("This function may take a long time, please don't close the application. "
                        "It depends on  the number of songs in your playlist. "
                        "Please insert your username, password and VK ID. Here you can get your ID: "
                        "<a href='https://regvk.com/id/'>https://regvk.com/id/</a>")
            self.msg.show()
            self.msg.raise_()

        self.player.setPlaylist(self.playlist)
        self.player.playlist().setCurrentIndex(0)
        self.player.setVolume(self.volume)

    # Play button
    def play(self):
        if self.ui.playButton.text() == "Play":
            self.player.play()
            self.isPlaying = True
            self.ui.playButton.setText("Pause")
            self.newIndex = self.player.playlist().currentIndex()

        else:
            self.player.pause()
            self.isPlaying = False
            self.ui.playButton.setText("Play")

    # Next button
    def next(self):
        self.playlist.next()
        self.newIndex = self.player.playlist().currentIndex()
        if not self.isPlaying:
            self.player.play()
            self.ui.playButton.setText("Pause")
            self.isPlaying = True

    # Previous button
    def prev(self):
        self.playlist.previous()
        self.newIndex = self.player.playlist().currentIndex()
        if not self.isPlaying:
            self.player.play()
            self.ui.playButton.setText("Pause")
            self.isPlaying = True

    # Repeat This button
    def repeatThisMode(self):
        if self.ui.repeatThis.text() == "Repeat This: Off":
            self.playlist.setPlaybackMode(1)
            self.player.play()
            self.isPlaying = True
            self.ui.playButton.setText("Pause")
            self.newIndex = self.player.playlist().currentIndex()
            self.ui.repeatThis.setText("Repeat This: On")
            self.ui.shuffleButton.setText("Shuffle: Off")
            self.ui.repeatOnce.setText("Repeat Once: Off")
        else:
            self.playlist.setPlaybackMode(3)
            self.ui.repeatThis.setText("Repeat This: Off")

    # Repeat Once button
    def repeatOnceMode(self):
        if self.ui.repeatOnce.text() == "Repeat Once: Off":
            self.playlist.setPlaybackMode(0)
            self.player.play()
            self.isPlaying = True
            self.ui.playButton.setText("Pause")
            self.newIndex = self.player.playlist().currentIndex()
            self.ui.repeatOnce.setText("Repeat Once: On")
            self.ui.shuffleButton.setText("Shuffle: Off")
            self.ui.repeatThis.setText("Repeat This: Off")
        else:
            self.playlist.setPlaybackMode(3)
            self.ui.repeatOnce.setText("Repeat Once: Off")

    # Shuffle button
    def shuffleMode(self):
        if self.ui.shuffleButton.text() == "Shuffle: Off":
            self.playlist.setPlaybackMode(4)
            self.player.play()
            self.isPlaying = True
            self.ui.playButton.setText("Pause")
            self.newIndex = self.player.playlist().currentIndex()
            self.ui.shuffleButton.setText("Shuffle: On")
            self.ui.repeatThis.setText("Repeat This: Off")
            self.ui.repeatOnce.setText("Repeat Once: Off")
        else:
            self.playlist.setPlaybackMode(3)
            self.ui.shuffleButton.setText("Shuffle: Off")


# LOGIN WINDOW ---------------------------------------------------------------------------------------------------------
class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        # Setup login window
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('login_icon.ico'))
        self.ui.passEdit.setEchoMode(QLineEdit.Password)
        self.setFixedSize(self.width(), self.height())

        # Connect button
        self.ui.pushButton.clicked.connect(self.button_login)

        # Setup timer
        self.timerlog = QTimer(self)
        self.timerlog.timeout.connect(self.time_hit_log)
        self.timerlog.start(int(1000 / 60))

    # Timer
    def time_hit_log(self):
        if not window.isVisible():
            self.close()

    # Login button
    def button_login(self):
        self.login = self.ui.userEdit.text()
        self.password = self.ui.passEdit.text()
        self.my_id = self.ui.vkidEdit.text()
        if (self.login == "") or (self.password == "") or (self.my_id == ""):
            self.ui.errorLabel.setText("All fields are required!")
        else:
            if not self.my_id.isdecimal():
                self.ui.errorLabel.setText("VK ID must contain only digits")
            else:
                vkwin.auth_vk(self.login, self.password, self.my_id)

# CAPTCHA WINDOW -------------------------------------------------------------------------------------------------------
class CaptchaWindow(QMainWindow):
    def __init__(self):
        super(CaptchaWindow, self).__init__()

        # Setup captcha window
        self.ui = captchaUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Captcha")
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # Connect button
        self.ui.captchaButton.clicked.connect(self.verify)

    # Download captcha image
    def get_Image(self, url):
        response = requests.get(str(url))
        file = open("captcha.png", "wb")
        file.write(response.content)
        file.close()

    # Get captcha url
    def getUrl(self, url):
        self.get_Image(url)
        self.captchurl = QPixmap("captcha.png")
        self.w = self.ui.captchaImg.width()
        self.h = self.ui.captchaImg.height()
        self.ui.captchaImg.setPixmap(self.captchurl.scaled(self.w, self.h))

    # Send answer to VK API
    def verify(self):
        self.answer = self.ui.captchaEdit.text()
        if self.answer == "":
            pass
        else:
            self.close()
            vk_api.exceptions.Captcha.try_again(self.answer)

# VK API --------------------------------------------------------------------------------------------------------
class GetAudioVK():

    # Get our session
    def auth_vk(self, username, password, my_id):
        try:
            self.vk_session = None
            self.vk_session = vk_api.VkApi(login=username, password=password)
            self.vk_session.auth()
            self.vk = self.vk_session.get_api()
            logwin.close()
            window.setEnabled(True)
            self.download_refresh(my_id)
        except vk_api.exceptions.Captcha as captcha:
            captchawin.show()
            self.urlCaptcha = captcha.get_url()  # Получить ссылку на изображение капчи
            self.cphwin = captchawin.getUrl(self.urlCaptcha)
        except vk_api.exceptions.AuthError as auth:
            logwin.ui.errorLabel.setText("Username or Password is wrong!")

    # Get information about songs and write in json file
    def download_refresh(self, my_id):
        if self.vk_session is not None:
            logwin.close()
            window.setWindowTitle("VK Player by dani3lz | Downloading...")
            vk_audio = audio.VkAudio(self.vk_session)
            time_start = time.time()
            songs_list = {}
            songs_list["Songs"] = []
            list_audio = vk_audio.get(owner_id=my_id)
            try:
                os.remove("songs.json")
            except Exception as e:
                pass
            j = 0
            file = open("songs.json", "a", encoding="utf-8")
            for i in list_audio:
                j += 1
                id_song = str(j)
                try:
                    title = i["title"]
                except Exception as e:
                    title = i["title"]
                try:
                    artist = i["artist"]
                except Exception as e:
                    artist = i["artist"]
                try:
                    url = i["url"]
                    songs_list["Songs"].append({
                        "id": id_song,
                        "title": title,
                        "artist": artist,
                        "url": str(url)
                    })
                except Exception as e:
                    pass
            json.dump(songs_list, file, indent=4)
            file.close()

            time_finish = time.time()
            self.timeFinal = time_finish - time_start
            self.msg_succes = QMessageBox()
            self.msg_succes.setWindowTitle("Congratulation")
            self.msg_succes.setText("All songs was downloaded in " + str(round(self.timeFinal)) + " seconds.")
            self.msg_succes.show()
            self.msg_succes.raise_()
            window.readSongs()
        else:
            self.msg_error = QMessageBox()
            self.msg_error.setWindowTitle("Error")
            self.msg_error.setText("Something goes wrong!")
            self.msg_error.show()
            self.msg_error.raise_()
# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    suppress_qt_warnings()
    app = QApplication([])
    logwin = LoginWindow()
    vkwin = GetAudioVK()
    captchawin = CaptchaWindow()
    window = PlayerWindow()
    window.show()
    sys.exit(app.exec())
