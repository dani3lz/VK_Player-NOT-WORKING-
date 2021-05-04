# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 531)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.durationLabel = QtWidgets.QLabel(self.centralwidget)
        self.durationLabel.setGeometry(QtCore.QRect(780, 52, 61, 21))
        self.durationLabel.setStyleSheet("color: white;\n"
"background: none;")
        self.durationLabel.setObjectName("durationLabel")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(960, 490, 81, 31))
        self.refreshButton.setStyleSheet("QPushButton#refreshButton {\n"
"background-color: #F52B2B;\n"
"border: 2px solid #F52B2B;\n"
"  color: white;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"QPushButton#refreshButton:hover{\n"
"    background-color: #A31B1B;\n"
"border: none;\n"
"}")
        self.refreshButton.setObjectName("refreshButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 130, 771, 381))
        self.listWidget.setStyleSheet("background: none;")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName("listWidget")
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(870, 52, 140, 22))
        self.volumeSlider.setStyleSheet("background: none;")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 50)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.volumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.volumeLabel.setGeometry(QtCore.QRect(910, 80, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setStyleSheet("color: white;\n"
"background: none;")
        self.volumeLabel.setObjectName("volumeLabel")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(100, 50, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("QPushButton#playButton {\n"
"background-color: #5181B8;\n"
"border: 2px solid #5181B8;\n"
"  color: white;\n"
"font-size: 18px;\n"
"width: 100%;\n"
"height: 28px;\n"
"    font:\"Bahnschrift\";\n"
"}\n"
"\n"
"QPushButton#playButton:hover{\n"
"    background-color: #2787F5;\n"
"border: none;\n"
"}")
        self.playButton.setObjectName("playButton")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(20, 50, 71, 30))
        self.prevButton.setStyleSheet("QPushButton#prevButton {\n"
"background-color: #809FC2;\n"
"  color: white;\n"
"  border: 2px solid #809FC2;\n"
"  height: 28px;\n"
"width: 75%;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 20px;\n"
"}\n"
"\n"
"QPushButton#prevButton:hover{\n"
"    background-color: #5181B8;\n"
"border:none;\n"
"}")
        self.prevButton.setObjectName("prevButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(210, 50, 71, 30))
        self.nextButton.setStyleSheet("QPushButton#nextButton {\n"
"background-color: #809FC2;\n"
"  color: white;\n"
"  border: 2px solid #809FC2;\n"
"  height: 28px;\n"
"width: 75%;\n"
"  text-decoration: none;\n"
"  font-size: 20px;\n"
"}\n"
"\n"
"QPushButton#nextButton:hover{\n"
"    background-color: #5181B8;\n"
"border:none;\n"
"}")
        self.nextButton.setObjectName("nextButton")
        self.musicSlider = QtWidgets.QSlider(self.centralwidget)
        self.musicSlider.setGeometry(QtCore.QRect(290, 50, 481, 31))
        self.musicSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.musicSlider.setStyleSheet("background: transparent;")
        self.musicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.musicSlider.setObjectName("musicSlider")
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(300, 20, 720, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.infoLabel.setFont(font)
        self.infoLabel.setStyleSheet("background: none;\n"
"color: white;")
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.repeatOnce = QtWidgets.QPushButton(self.centralwidget)
        self.repeatOnce.setGeometry(QtCore.QRect(790, 210, 249, 32))
        self.repeatOnce.setStyleSheet("QPushButton#repeatOnce {\n"
"background: none;\n"
"background-color: #4CAF50;\n"
"  color: white;\n"
"  border: 2px solid #4CAF50;\n"
"  padding: 5px 15px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"QPushButton#repeatOnce:hover{\n"
"    background-color: #4CAF35;\n"
"}")
        self.repeatOnce.setObjectName("repeatOnce")
        self.shuffleButton = QtWidgets.QPushButton(self.centralwidget)
        self.shuffleButton.setGeometry(QtCore.QRect(790, 130, 249, 32))
        self.shuffleButton.setStyleSheet("QPushButton#shuffleButton {\n"
"background: none;\n"
"background-color: #4CAF50;\n"
"  color: white;\n"
"  border: 2px solid #4CAF50;\n"
"  padding: 5px 15px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"QPushButton#shuffleButton:hover{\n"
"    background-color: #4CAF35;\n"
"}")
        self.shuffleButton.setObjectName("shuffleButton")
        self.repeatThis = QtWidgets.QPushButton(self.centralwidget)
        self.repeatThis.setGeometry(QtCore.QRect(790, 170, 249, 32))
        self.repeatThis.setStyleSheet("QPushButton#repeatThis {\n"
"background: none;\n"
"background-color: #4CAF50;\n"
"  color: white;\n"
"  border: 2px solid #4CAF50;\n"
"  padding: 5px 15px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
"QPushButton#repeatThis:hover{\n"
"    background-color: #4CAF35;\n"
"}")
        self.repeatThis.setObjectName("repeatThis")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(-10, -10, 1071, 571))
        self.groupBox.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(28, 95, 66, 255), stop:1 rgba(17, 81, 118, 255))")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.raise_()
        self.durationLabel.raise_()
        self.refreshButton.raise_()
        self.listWidget.raise_()
        self.volumeSlider.raise_()
        self.volumeLabel.raise_()
        self.playButton.raise_()
        self.prevButton.raise_()
        self.nextButton.raise_()
        self.musicSlider.raise_()
        self.infoLabel.raise_()
        self.repeatOnce.raise_()
        self.shuffleButton.raise_()
        self.repeatThis.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.durationLabel.setText(_translate("MainWindow", "0.00 / 0.00"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume:"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.prevButton.setText(_translate("MainWindow", "<<"))
        self.nextButton.setText(_translate("MainWindow", ">>"))
        self.repeatOnce.setText(_translate("MainWindow", "Repeat Once: Off"))
        self.shuffleButton.setText(_translate("MainWindow", "Shuffle: Off"))
        self.repeatThis.setText(_translate("MainWindow", "Repeat This: Off"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
