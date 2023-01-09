from LogicApplication.userDataValidation import *
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox
def page_to_sign(stackedWidget):
    stackedWidget.setCurrentIndex(0)
    print('asadas')

def page_to_login(stackedWidget,wrong_pass_repeat_reg,wrong_pass_reg,wrong_username_reg,worng_email_reg):
    stackedWidget.setCurrentIndex(1)
    wrong_pass_repeat_reg.setFixedSize(0, 0)
    wrong_pass_reg.setFixedSize(0, 0)
    worng_email_reg.setFixedSize(0, 0)
    wrong_username_reg.setFixedSize(0, 0)

def registration_function(stackedWidget,username,email,password_sign,reapet_passwd,user_or_email,wrong_pass_repeat_reg,wrong_pass_reg,wrong_username_reg,worng_email_reg):
    def bttn_in_messege_box():
        stackedWidget.setCurrentIndex(1)

        wrong_pass_repeat_reg.setFixedSize(0, 0)
        wrong_pass_reg.setFixedSize(0, 0)
        worng_email_reg.setFixedSize(0, 0)
        wrong_username_reg.setFixedSize(0, 0)
    try:
        RegistrationUser(username.text(), email.text(), password_sign.text(),reapet_passwd.text())
            # Окно успешной регистрации с кнопкой
        success_mess_box = QMessageBox()
        success_mess_box.setWindowTitle("Info")
        success_mess_box.setText("Successful registration")
        success_mess_box.setIcon(QMessageBox.Information)
        success_mess_box.buttonClicked.connect(bttn_in_messege_box)
        success_mess_box.exec_()
            # Автоматическое вписание юзернейма после регистрации
        user_or_email.setText(username.text())

    except:
        #Красная подсветка, если данные не правильны
        wrong_pass_repeat_reg.setFixedSize(276, 10)
        wrong_pass_reg.setFixedSize(276, 10)
        worng_email_reg.setFixedSize(276, 10)
        wrong_username_reg.setFixedSize(276, 10)


