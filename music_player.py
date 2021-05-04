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
from bs4 import BeautifulSoup

def suppress_qt_warnings():
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"

class PlayerWindow(QMainWindow):
    def __init__(self):
        super(PlayerWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("VK PLayer by dani3lz")
        self.setWindowIcon(QIcon('vk_icon.ico'))
        self.volume = 50
        self.titles = []
        self.artists = []
        self.readTxt()
        self.isPlaying = False
        self.ui.musicSlider.setPageStep(0)
        self.valueSlider = 0
        self.currentIndex = -1
        self.newIndex = 1
        self.playlist.setPlaybackMode(3)
        self.ui.listWidget.setCurrentRow(0)
        self.row = 0
        try:
            self.ui.infoLabel.setText(self.titles[self.row] + " - " + self.artists[self.row])
        except Exception as e:
            pass
        self.ui.durationLabel.setText("0.00 / 0.00")

        self.ui.volumeLabel.setText("Volume: " + str(self.volume))

        self.ui.playButton.clicked.connect(self.play)
        self.ui.nextButton.clicked.connect(self.next)
        self.ui.prevButton.clicked.connect(self.prev)
        self.ui.shuffleButton.clicked.connect(self.shuffleMode)
        self.ui.repeatThis.clicked.connect(self.repeatThisMode)
        self.ui.repeatOnce.clicked.connect(self.repeatOnceMode)
        self.ui.refreshButton.clicked.connect(self.refreshMode)

        self.ui.musicSlider.actionTriggered.connect(self.sliderValue)
        self.ui.listWidget.itemClicked.connect(self.changeSong)

        self.ui.volumeSlider.setValue(self.volume)
        self.ui.volumeSlider.actionTriggered.connect(self.setVolume)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_hit)
        self.timer.start(int(1000 / 60))

    def refreshMode(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Advertisement")
        self.msg.setText("This function may take a long time, please don't close the application. It depends on  the number of songs in your playlist.")
        self.msg.show()
        self.setEnabled(False)
        logwin.show()

    def setVolume(self):
        self.volume = self.ui.volumeSlider.value()
        self.player.setVolume(self.volume)
        self.ui.volumeLabel.setText("Volume: " + str(self.volume))


    def changeSong(self):
        self.row = self.ui.listWidget.currentRow()
        self.player.playlist().setCurrentIndex(self.row)
        if not self.isPlaying:
            self.player.play()
            self.ui.playButton.setText("Pause")
            self.isPlaying = True

    def sliderValue(self):
        self.player.setVolume(0)
        self.valueSlider = self.ui.musicSlider.value()
        self.player.setPosition(self.valueSlider)
        self.player.setVolume(self.volume)

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
            self.ui.infoLabel.setText(self.titles[self.row] + " - " + self.artists[self.row])
            self.newIndex = self.player.playlist().currentIndex()
            self.checkList()
            self.song_duration = "{:.2f}".format(self.player.duration() / 60000, 2)
            self.now_duration = "{:.2f}".format(self.ui.musicSlider.value() / 60000, 2)
            self.ui.durationLabel.setText(str(self.now_duration) + " / " + str(self.song_duration))

    def checkList(self):
        if self.currentIndex == self.newIndex:
            pass
        else:
            self.ui.listWidget.setCurrentRow(self.player.playlist().currentIndex())
            self.currentIndex = self.newIndex

    def readTxt(self):
        self.setWindowTitle("VK Player by dani3lz")
        i = 0
        self.nr = 0
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist(self.player)
        try:
            with open("music.txt", "r", encoding="utf-8") as file:
                for f in file:
                    i += 1
                    self.temp = f.rsplit("\n")
                    self.temp = ''.join(self.temp)
                    if i == 1: # link
                        self.url = self.temp
                        self.playlist.addMedia(QMediaContent(QUrl(self.url)))
                    if i == 2: # title
                        self.titleSong = self.temp
                        self.titles.append(self.temp)
                    if i == 3: # artist
                        self.artistSong = self.temp
                        self.artists.append(self.temp)
                        i = 0
                        self.nr += 1
                        self.ui.listWidget.addItem(str(self.nr) + ". " + self.titleSong + " - " + self.artistSong)
                        self.first = False
        except Exception as e:
            self.setEnabled(False)
            self.first = True
            logwin.show()


        self.player.setPlaylist(self.playlist)
        self.player.playlist().setCurrentIndex(0)
        self.player.setVolume(self.volume)


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

    def next(self):
        self.playlist.next()
        self.newIndex = self.player.playlist().currentIndex()
        if not self.isPlaying:
            self.player.play()
            self.ui.playButton.setText("Pause")
            self.isPlaying = True

    def prev(self):
        self.playlist.previous()
        self.newIndex = self.player.playlist().currentIndex()
        if not self.isPlaying:
            self.player.play()
            self.ui.playButton.setText("Pause")
            self.isPlaying = True

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
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('login_icon.ico'))
        self.ui.passEdit.setEchoMode(QLineEdit.Password)
        self.setFixedSize(self.width(), self.height())
        self.ui.pushButton.clicked.connect(self.button_login)
        self.timerlog = QTimer(self)
        self.timerlog.timeout.connect(self.time_hit_log)
        self.timerlog.start(int(1000 / 60))

    def time_hit_log(self):
        if not window.isVisible():
            self.close()

    def button_login(self):
        self.login = self.ui.userEdit.text()
        self.password = self.ui.passEdit.text()
        self.my_id = self.ui.vkidEdit.text()
        if (self.login == "") or (self.password == "") or (self.my_id == ""):
            self.ui.errorLabel.setText("All fields are required!")
        else:
            vkwin.auth_vk(self.login, self.password, self.my_id)

# ----------------------------------------------------------------------------------------------------------------------
# CAPTCHA WINDOW -------------------------------------------------------------------------------------------------------
class CaptchaWindow(QMainWindow):
    def __init__(self):
        super(CaptchaWindow, self).__init__()
        self.ui = captchaUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Captcha")
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.ui.captchaButton.clicked.connect(self.verify)

    def get_Image(self, url):
        response = requests.get(str(url))
        file = open("captcha.png", "wb")
        file.write(response.content)
        file.close()

    def getUrl(self, url):
        self.get_Image(url)
        self.captchurl = QPixmap("captcha.png")
        self.w = self.ui.captchaImg.width()
        self.h = self.ui.captchaImg.height()
        self.ui.captchaImg.setPixmap(self.captchurl.scaled(self.w, self.h))

    def verify(self):
        self.answer = self.ui.captchaEdit.text()
        if self.answer == "":
            pass
        else:
            self.close()
            vk_api.exceptions.Captcha.try_again(self.answer)

# ----------------------------------------------------------------------------------------------------------------------


class GetAudioVK():
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
            self.urlCaptcha = captcha.get_url() # Получить ссылку на изображение капчи
            self.cphwin = captchawin.getUrl(self.urlCaptcha)
        except vk_api.exceptions.AuthError as auth:
            logwin.ui.errorLabel.setText("Username or Password is wrong!")


    def download_refresh(self, my_id):
        if self.vk_session is not None:
            logwin.close()
            window.setWindowTitle("VK Player by dani3lz | Downloading...")
            vk_audio = audio.VkAudio(self.vk_session)
            time_start = time.time()
            list_audio = vk_audio.get(owner_id=my_id)
            try:
                os.remove("music.txt")
            except Exception as e:
                pass
            file = open("music.txt", "a", encoding="utf-8")
            for i in list_audio:
                try:
                    file.write(str(i["url"]) + "\n")
                    file.write(str(i["title"]) + "\n")
                    file.write(str(i["artist"]) + "\n")
                except Exception as e:
                    file.write("Undefined_Except_Title\n")
                    file.write("Undefined_Except_Artist\n")
            file.close()

            time_finish = time.time()
            self.timeFinal = time_finish - time_start
            self.msg_succes = QMessageBox()
            self.msg_succes.setWindowTitle("Congratulation")
            self.msg_succes.setText("All songs was downloaded in " + str(round(self.timeFinal)) + " seconds.")
            self.msg_succes.show()
            window.readTxt()
        else:
            self.msg_error = QMessageBox()
            self.msg_error.setWindowTitle("Error")
            self.msg_error.setText("Something goes wrong!")
            self.msg_error.show()
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
