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
import threading
import shutil


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
        self.setWindowTitle("VK PLayer 1.0 by dani3lz")
        self.setWindowIcon(QIcon('img/icon.ico'))

        # Setup music elements Nr.1
        self.volume = 50
        self.titles = []
        self.artists = []
        self.covers = []
        self.shuffle = False
        self.repeatthis = False
        self.repeatonce = False

        # Read file with songs and settings
        self.readSongs()
        self.settings_read()
        self.checkCover()

        # Setup music elements Nr.2
        self.isPlaying = False
        self.ui.musicSlider.setPageStep(0)
        self.valueSlider = 0
        self.currentIndex = 0
        self.newIndex = 1
        self.playlist.setPlaybackMode(3)
        self.ui.listWidget.setCurrentRow(0)

        # Check if exist first song in file
        try:
            self.ui.titleLabel.setText(self.titles[self.row])
            self.ui.artistLabel.setText(self.artists[self.row])
            self.player.playlist().setCurrentIndex(self.row)
            self.ui.listWidget.setCurrentRow(self.row)
        except Exception as e:
            self.row = 0

        # Volume and duration labels
        self.player.setVolume(self.volume)
        self.ui.durationLabel.setText("0:00 / 0:00")
        self.ui.volumeLabel.setText("Volume: " + str(self.volume))

        # Connect buttons
        self.ui.playButton.clicked.connect(self.play)
        self.ui.nextButton.clicked.connect(self.next)
        self.ui.prevButton.clicked.connect(self.prev)
        self.ui.shuffleButton.clicked.connect(self.shuffleMode)
        self.ui.repeatThis.clicked.connect(self.repeatThisMode)
        self.ui.refreshButton.clicked.connect(self.refreshMode)

        self.ui.playButton.setIcon(QIcon("play.png"))

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
            self.ui.playButton.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/pause.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")
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

            self.currentIndex = self.row
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
        if self.first and not logwin.isVisible():
            self.close()
            cpwin.close()
        if not self.isEnabled() and not logwin.isVisible():
            self.setEnabled(True)
        self.checkStyle()
        self.setVolume()
        if self.isPlaying:
            self.ui.musicSlider.setMaximum(self.player.duration())
            self.ui.musicSlider.setValue(self.player.position())
            self.row = self.ui.listWidget.currentRow()
            self.ui.titleLabel.setText(self.titles[self.row])
            self.ui.artistLabel.setText(self.artists[self.row])
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

            if self.repeatonce:
                if self.now_duration == self.song_duration:
                    self.isPlaying = False
                    self.ui.playButton.setStyleSheet("background-color: transparent;\n"
                                                     "border-image: url(img/play.png);\n"
                                                     "background: none;\n"
                                                     "border: none;\n"
                                                     "background-repeat: none;")
                    self.player.stop()
        self.settings_write()
    def checkCover(self):
        try:
            if self.covers[self.currentIndex] == "no_image.jpg":
                self.imgsrc = QPixmap("img/" + self.covers[self.currentIndex])
            else:
                self.imgsrc = QPixmap("covers/" + self.covers[self.currentIndex])
            self.w = self.ui.imgLabel.width()
            self.h = self.ui.imgLabel.height()
            self.ui.imgLabel.setPixmap(self.imgsrc.scaled(self.w, self.h))
        except Exception as e:
            print(e)

    # Sets the current position in the list
    def checkList(self):
        try:
            if self.currentIndex == self.newIndex:
                pass
            else:
                self.ui.listWidget.setCurrentRow(self.player.playlist().currentIndex())
                self.currentIndex = self.newIndex
                self.checkCover()

        except Exception as e:
            print(e)


    # Read file with songs
    def readSongs(self):
        self.ui.listWidget.clear()
        self.artists.clear()
        self.titles.clear()
        self.covers.clear()
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
                self.ui.listWidget.addItem(str(i["id"] + 1) + ". " + self.titleSong + " - " + self.artistSong)
                # cover
                if i["cover"] == "Undefined":
                    self.covers.append("no_image.jpg")
                else:
                    self.covers.append(i["cover"])
            self.ui.titleLabel.setText(self.titles[0])
            self.ui.artistLabel.setText(self.artists[0])

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
        if not self.isPlaying:
            self.player.play()
            self.isPlaying = True
            self.newIndex = self.player.playlist().currentIndex()
            self.checkStyle()
        else:
            self.player.pause()
            self.isPlaying = False
            self.checkStyle()


    # Next button
    def next(self):
        self.playlist.next()
        self.newIndex = self.player.playlist().currentIndex()
        if not self.isPlaying:
            self.player.play()
            self.isPlaying = True
            self.ui.playButton.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/pause.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")

    # Previous button
    def prev(self):
        self.playlist.previous()
        self.newIndex = self.player.playlist().currentIndex()
        if not self.isPlaying:
            self.player.play()
            self.isPlaying = True
            self.ui.playButton.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/pause.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")

    # Repeat This button
    def repeatThisMode(self):
        if not self.repeatthis and not self.repeatonce:
            self.playlist.setPlaybackMode(1)
            self.repeatthis = True
            self.shuffle = False
            self.repeatonce = False
            self.checkstylebuttons()
        elif self.repeatthis:
            self.playlist.setPlaybackMode(0)
            self.repeatthis = False
            self.shuffle = False
            self.repeatonce = True
            self.checkstylebuttons()
        else:
            self.playlist.setPlaybackMode(3)
            self.repeatonce = False
            self.checkstylebuttons()

    # Shuffle button
    def shuffleMode(self):
        if not self.shuffle:
            self.playlist.setPlaybackMode(4)
            self.shuffle = True
            self.repeatonce = False
            self.repeatthis = False
            self.checkstylebuttons()

        else:
            self.playlist.setPlaybackMode(3)
            self.shuffle = False
            self.checkstylebuttons()

    def checkstylebuttons(self):
        if self.shuffle:
            self.ui.shuffleButton.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/shuffle_on.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")
        else:
            self.ui.shuffleButton.setStyleSheet("background-color: transparent;\n"
                                                "border-image: url(img/shuffle.png);\n"
                                                "background: none;\n"
                                                "border: none;\n"
                                                "background-repeat: none;")

        if self.repeatthis and not self.repeatonce:
            self.ui.repeatThis.setStyleSheet("background-color: transparent;\n"
                                                "border-image: url(img/repeatthis_on.png);\n"
                                                "background: none;\n"
                                                "border: none;\n"
                                                "background-repeat: none;")
        elif not self.repeatthis and self.repeatonce:
            self.ui.repeatThis.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/repeatonce.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")
        else:
            self.ui.repeatThis.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/repeatthis.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")

    def checkStyle(self):
        if self.ui.musicSlider.underMouse():
            self.ui.musicSlider.setStyleSheet("QSlider{\n"
                                                "    background-color: transparent;\n"
                                                "}\n"
                                                "QSlider::groove:horizontal \n"
                                                "{\n"
                                                "    background-color: transparent;\n"
                                                "    height: 3px;\n"
                                                "}\n"
                                                "QSlider::sub-page:horizontal \n"
                                                "{\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(98, 9, 54, 255), stop:1 rgba(33, 13, 68, 255))\n"
                                                "}\n"
                                                "QSlider::add-page:horizontal \n"
                                                "{\n"
                                                "    background-color: rgb(118, 118, 118);\n"
                                                "}\n"
                                                "QSlider::handle:horizontal \n"
                                                "{\n"
                                                "    background-color: rgb(216, 216, 216);\n"
                                                "    width: 14px;\n"
                                                "    margin: -5px;\n"
                                                "    border-radius: 6px;\n"
                                                "}\n"
                                                "QSlider::handle:horizontal:hover \n"
                                                "{\n"
                                                "    background-color: rgb(240, 240, 240);\n"
                                                "}")
        else:
            self.ui.musicSlider.setStyleSheet("QSlider{\n"
                                                "    background-color: transparent;\n"
                                                "}\n"
                                                "QSlider::groove:horizontal \n"
                                                "{\n"
                                                "    background-color: transparent;\n"
                                                "    height: 3px;\n"
                                                "}\n"
                                                "QSlider::sub-page:horizontal \n"
                                                "{\n"
                                                "    background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(98, 9, 54, 255), stop:1 rgba(33, 13, 68, 255))\n"
                                                "}\n"
                                                "QSlider::add-page:horizontal \n"
                                                "{\n"
                                                "    background-color: rgb(118, 118, 118);\n"
                                                "}\n"
                                                "QSlider::handle:horizontal \n"
                                                "{\n"
                                                "    background-color: transparent;\n"
                                                "    width: 14px;\n"
                                                "    margin: -5px;\n"
                                                "    border-radius: 6px;\n"
                                                "}\n"
                                                "QSlider::handle:horizontal:hover \n"
                                                "{\n"
                                                "    background-color: rgb(240, 240, 240);\n"
                                                "}")

        if self.ui.playButton.underMouse():
            if not self.isPlaying:
                self.ui.playButton.setStyleSheet("background-color: transparent;\n"
                                                 "border-image: url(img/play_focus.png);\n"
                                                 "background: none;\n"
                                                 "border: none;\n"
                                                 "background-repeat: none;")
            else:
                self.ui.playButton.setStyleSheet("background-color: transparent;\n"
                                                 "border-image: url(img/pause_focus.png);\n"
                                                 "background: none;\n"
                                                 "border: none;\n"
                                                 "background-repeat: none;")
        else:
            if not self.isPlaying:
                self.ui.playButton.setStyleSheet("background-color: transparent;\n"
                                                 "border-image: url(img/play.png);\n"
                                                 "background: none;\n"
                                                 "border: none;\n"
                                                 "background-repeat: none;")
            else:
                self.ui.playButton.setStyleSheet("background-color: transparent;\n"
                                                 "border-image: url(img/pause.png);\n"
                                                 "background: none;\n"
                                                 "border: none;\n"
                                                 "background-repeat: none;")

        if self.ui.nextButton.underMouse():
            self.ui.nextButton.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/next_focus.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")
        else:
            self.ui.nextButton.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/next.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")

        if self.ui.prevButton.underMouse():
            self.ui.prevButton.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/prev_focus.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")
        else:
            self.ui.prevButton.setStyleSheet("background-color: transparent;\n"
                                             "border-image: url(img/prev.png);\n"
                                             "background: none;\n"
                                             "border: none;\n"
                                             "background-repeat: none;")


# LOGIN WINDOW ---------------------------------------------------------------------------------------------------------
class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        # Setup login window
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('img/login_icon.ico'))
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
        login = self.ui.userEdit.text()
        password = self.ui.passEdit.text()
        my_id = self.ui.vkidEdit.text()
        if (login == "") or (password == "") or (my_id == ""):
            self.ui.errorLabel.setText("All fields are required!")
        else:
            if not my_id.isdecimal():
                self.ui.errorLabel.setText("VK ID must contain only digits")
            else:
                vkwin.auth_vk(login, password, my_id)


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
        try:
            os.remove("captcha.png")
        except Exception as e:
            pass
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
            print("F: AUTH")
            self.vk_session = vk_api.VkApi(login=username, password=password)
            self.vk_session.auth()
            self.vk = self.vk_session.get_api()
            window.setWindowTitle("VK Player by dani3lz | Downloading...")
            logwin.close()
            self.download_refresh(my_id)

        except vk_api.exceptions.Captcha as captcha:
            cpwin.show()
            self.urlCaptcha = captcha.get_url()
            cpwin.getUrl(self.urlCaptcha)
            captcha.try_again()
        except vk_api.exceptions.AuthError as auth:
            self.msg_auth = QMessageBox()
            self.msg_auth.setWindowTitle("Error")
            self.msg_auth.setText("Username or Password is wrong!")
            self.msg_auth.show()
            self.msg_auth.raise_()

    def get_Image(self, url, id_song):
        response = requests.get(str(url))
        file = open(id_song + ".jpg", "wb")
        file.write(response.content)
        file.close()

    def download_refresh(self, my_id):
        print("F: DOWNLOAD")
        vk_audio = audio.VkAudio(self.vk_session)
        time_start = time.time()
        self.songs_list = {}
        self.songs_list["Songs"] = []
        self.list_audio = vk_audio.get(owner_id=my_id)
        size = len(self.list_audio)

        try:
            os.remove("songs.json")
        except Exception as e:
            pass

        th = []
        try:
            shutil.rmtree("covers")
        except Exception as e:
            pass
        if not os.path.exists('covers'):
            os.makedirs('covers')
        os.chdir('covers')

        for nr in range(size):
            t1 = threading.Thread(target=self.write_list, args=[nr])
            t1.start()
            th.append(t1)

        for t in th:
            t.join()
        os.chdir("../")

        self.songs_list["Songs"].sort(key=lambda x: x["id"])
        with open("songs.json", "a", encoding="utf-8") as file:
            json.dump(self.songs_list, file, indent=4)

        time_finish = time.time()
        timefinal = time_finish - time_start
        self.msg_succes = QMessageBox()
        self.msg_succes.setWindowTitle("Congratulation")
        self.msg_succes.setText("All songs was downloaded in " + str(round(timefinal)) + " seconds.")
        self.msg_succes.show()
        self.msg_succes.raise_()
        window.readSongs()
        print("COMPLETED")

    def write_list(self, nr):
        print("F: WRITE")
        id_song = nr
        try:
            title = self.list_audio[nr]["title"]
        except Exception as e:
            title = "Undefined_Title"
        try:
            artist = self.list_audio[nr]["artist"]
        except Exception as e:
            artist = "Undefined_Artist"
        try:
            if not self.list_audio[nr]["track_covers"]:
                cover = "Undefined"
            else:
                img = self.list_audio[nr]["track_covers"][1]
                self.get_Image(img, str(nr))
                cover = str(id_song) + ".jpg"
            url = self.list_audio[nr]["url"]
            self.songs_list["Songs"].append({
                        "id": id_song,
                        "title": title,
                        "artist": artist,
                        "url": url,
                        "cover": cover
            })
        except Exception as e:
            print(e)
# ----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    suppress_qt_warnings()
    app = QApplication([])
    logwin = LoginWindow()
    vkwin = GetAudioVK()
    cpwin = CaptchaWindow()
    window = PlayerWindow()
    window.show()
    sys.exit(app.exec())
