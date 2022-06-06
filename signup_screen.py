# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateAccountWindow(object):
    def setupUi(self, CreateAccountWindow):
        CreateAccountWindow.setObjectName("CreateAccountWindow")
        CreateAccountWindow.resize(680, 600)
        CreateAccountWindow.setMinimumSize(QtCore.QSize(680, 600))
        CreateAccountWindow.setMaximumSize(QtCore.QSize(680, 600))
        CreateAccountWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.034, y1:0.563, x2:0.982955, y2:0.46, stop:0 rgba(85, 85, 127, 255), stop:1 rgba(0, 85, 127, 255));")
        self.centralwidget = QtWidgets.QWidget(CreateAccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_singUp = QtWidgets.QLabel(self.centralwidget)
        self.label_singUp.setGeometry(QtCore.QRect(170, 80, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(35)
        self.label_singUp.setFont(font)
        self.label_singUp.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_singUp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_singUp.setObjectName("label_singUp")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(180, 190, 321, 31))
        self.lineEdit_username.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(249, 45, 239);\n"
"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55, 255, 0);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(0, 255, 255);\n"
"}")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password_1_reg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password_1_reg.setGeometry(QtCore.QRect(180, 280, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.lineEdit_password_1_reg.setFont(font)
        self.lineEdit_password_1_reg.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(249, 45, 239);\n"
"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55, 255, 0);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(0, 255, 255);\n"
"}")
        self.lineEdit_password_1_reg.setText("")
        self.lineEdit_password_1_reg.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_password_1_reg.setObjectName("lineEdit_password_1_reg")
        self.signup_btn = QtWidgets.QPushButton(self.centralwidget)
        self.signup_btn.setGeometry(QtCore.QRect(180, 470, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.signup_btn.setFont(font)
        self.signup_btn.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"border-radius: 10px;")
        self.signup_btn.setObjectName("signup_btn")
        self.lineEdit_password_2_reg = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password_2_reg.setGeometry(QtCore.QRect(180, 360, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.lineEdit_password_2_reg.setFont(font)
        self.lineEdit_password_2_reg.setStyleSheet("QLineEdit {\n"
"border: 2px solid rgb(249, 45, 239);\n"
"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55, 255, 0);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(0, 255, 255);\n"
"}")
        self.lineEdit_password_2_reg.setText("")
        self.lineEdit_password_2_reg.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_password_2_reg.setObjectName("lineEdit_password_2_reg")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(180, 420, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_error.setText("")
        self.label_error.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_error.setObjectName("label_error")
        CreateAccountWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateAccountWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateAccountWindow)

    def retranslateUi(self, CreateAccountWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateAccountWindow.setWindowTitle(_translate("CreateAccountWindow", "CreateAccount"))
        self.label_singUp.setText(_translate("CreateAccountWindow", "<html><head/><body><p>Create Account</p><p><br/></p></body></html>"))
        self.lineEdit_username.setPlaceholderText(_translate("CreateAccountWindow", "Username"))
        self.lineEdit_password_1_reg.setPlaceholderText(_translate("CreateAccountWindow", "Password"))
        self.signup_btn.setText(_translate("CreateAccountWindow", "SignUp"))
        self.lineEdit_password_2_reg.setPlaceholderText(_translate("CreateAccountWindow", "Retype Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateAccountWindow = QtWidgets.QMainWindow()
    ui = Ui_CreateAccountWindow()
    ui.setupUi(CreateAccountWindow)
    CreateAccountWindow.show()
    sys.exit(app.exec_())
