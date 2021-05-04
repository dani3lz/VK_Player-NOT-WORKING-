# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(592, 364)
        SecondWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(-10, -10, 701, 721))
        self.groupBox.setStyleSheet("background: rgb(2,0,36);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.captchaEdit = QtWidgets.QLineEdit(self.groupBox)
        self.captchaEdit.setGeometry(QtCore.QRect(150, 540, 331, 41))
        self.captchaEdit.setStyleSheet("background: white;\n"
"")
        self.captchaEdit.setObjectName("captchaEdit")
        self.errorLabel = QtWidgets.QLabel(self.groupBox)
        self.errorLabel.setGeometry(QtCore.QRect(40, 300, 521, 51))
        self.errorLabel.setStyleSheet("color:red;\n"
"font-size: 25px;")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(40, 20, 531, 281))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loginLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.loginLabel.setFont(font)
        self.loginLabel.setStyleSheet("color: white")
        self.loginLabel.setObjectName("loginLabel")
        self.horizontalLayout_3.addWidget(self.loginLabel)
        self.userEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.userEdit.setFont(font)
        self.userEdit.setStyleSheet("background: white;")
        self.userEdit.setObjectName("userEdit")
        self.horizontalLayout_3.addWidget(self.userEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.passLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.passLabel.setFont(font)
        self.passLabel.setStyleSheet("color: white;")
        self.passLabel.setObjectName("passLabel")
        self.horizontalLayout_4.addWidget(self.passLabel)
        self.passEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.passEdit.setFont(font)
        self.passEdit.setStyleSheet("background: white\n"
"")
        self.passEdit.setObjectName("passEdit")
        self.horizontalLayout_4.addWidget(self.passEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(88)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.vkidLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.vkidLabel.setFont(font)
        self.vkidLabel.setStyleSheet("color: white;")
        self.vkidLabel.setObjectName("vkidLabel")
        self.horizontalLayout_5.addWidget(self.vkidLabel)
        self.vkidEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.vkidEdit.setFont(font)
        self.vkidEdit.setStyleSheet("background: white\n"
"")
        self.vkidEdit.setObjectName("vkidEdit")
        self.horizontalLayout_5.addWidget(self.vkidEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"background-color: #4CAF50;\n"
"  color: white;\n"
"  border: 2px solid #4CAF50;\n"
"  padding: 16px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  font-size: 25px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: #4CAF35;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "Authorization"))
        self.loginLabel.setText(_translate("SecondWindow", "Username"))
        self.userEdit.setPlaceholderText(_translate("SecondWindow", "Your mobile (+373...)"))
        self.passLabel.setText(_translate("SecondWindow", "Password"))
        self.passEdit.setPlaceholderText(_translate("SecondWindow", "Your password"))
        self.vkidLabel.setText(_translate("SecondWindow", "VK ID"))
        self.vkidEdit.setPlaceholderText(_translate("SecondWindow", "Your ID (only numbers)"))
        self.pushButton.setText(_translate("SecondWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
