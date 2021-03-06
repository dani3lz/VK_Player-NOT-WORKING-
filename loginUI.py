# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(513, 513)
        login.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        login.setStyleSheet("QWidget\n"
"{\n"
"    background: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(65, 65, 65, 255), stop:1 rgba(0, 0, 0, 255));\n"
"    color: #000000;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")

        self.titleBarLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleBarLabel.setGeometry(QtCore.QRect(0, 0, 469, 30))
        font = QtGui.QFont("Impact")
        font.setPointSize(13)
        self.titleBarLabel.setFont(font)
        self.titleBarLabel.setStyleSheet("background: #070707;\n"
                                         "color: #CDCDCD;")
        self.titleBarLabel.setObjectName("titleBarLabel")

        self.closeButton = QtWidgets.QPushButton(login)
        self.closeButton.setGeometry(QtCore.QRect(469, 0, 44, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton\n"
                                       "{\n"
                                       "    background: #070707;\n"
                                       "    color: #cdcdcd;\n"
                                       "    border-style: solid;\n"
                                       "    border-width: 1px;\n"
                                       "    border-color: transparent;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton::hover\n"
                                       "{\n"
                                       "    background-color: #E81123;\n"
                                       "    color: #fff;\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "QPushButton::pressed\n"
                                       "{\n"
                                       "    background-color: #7D0913;\n"
                                       "    color: #fff;\n"
                                       "}")
        self.closeButton.setObjectName("closeButton")



        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 380, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(98, 9, 54, 180), stop:1 rgba(33, 13, 68, 180));\n"
"    color: #cdcdcd;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-radius: 17px;\n"
"    border-color: transparent;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.5, stop:0 rgba(98, 9, 54, 255), stop:1 rgba(33, 13, 68, 255));\n"
"    color: #fff;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #202020;\n"
"    color: #fff;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.userEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.userEdit.setGeometry(QtCore.QRect(30, 160, 440, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.userEdit.setFont(font)
        self.userEdit.setStyleSheet("QLineEdit{\n"
"    background-color: transparent;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 10px;\n"
"\n"
"}")
        self.userEdit.setText("")
        self.userEdit.setObjectName("userEdit")
        self.passEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passEdit.setGeometry(QtCore.QRect(30, 230, 440, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.passEdit.setFont(font)
        self.passEdit.setStyleSheet("QLineEdit{\n"
"    background-color: transparent;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 10px;\n"
"\n"
"}")
        self.passEdit.setText("")
        self.passEdit.setObjectName("passEdit")
        self.vkidEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.vkidEdit.setGeometry(QtCore.QRect(30, 300, 440, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.vkidEdit.setFont(font)
        self.vkidEdit.setStyleSheet("QLineEdit{\n"
"    background-color: transparent;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-top: 0px;\n"
"    border-left: 0px;\n"
"    border-right: 0px;\n"
"    border-color: #b9b9bb;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 10px;\n"
"\n"
"}")
        self.vkidEdit.setText("")
        self.vkidEdit.setPlaceholderText("VK ID (only numbers)")
        self.vkidEdit.setObjectName("vkidEdit")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(20, 450, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: red;\n"
"background: transparent;")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 30, 531, 91))
        self.groupBox.setStyleSheet("border: none; background: rgb(24, 24 ,24);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 10, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"background: transparent;\n"
"")
        self.label.setObjectName("label")
        self.titleBarLabel.raise_()
        self.closeButton.raise_()
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.userEdit.raise_()
        self.passEdit.raise_()
        self.vkidEdit.raise_()
        self.errorLabel.raise_()
        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.closeButton.setText(_translate("MainWindow", "???"))
        self.pushButton.setText(_translate("login", "Login"))
        self.userEdit.setPlaceholderText(_translate("login", "Username"))
        self.passEdit.setPlaceholderText(_translate("login", "Password"))
        self.label.setText(_translate("login", "VK Authorization"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
