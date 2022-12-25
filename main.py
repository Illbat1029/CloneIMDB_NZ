
import sys
import os
import bcrypt
from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve


from Login_page import *
from main_page import *
from fogort_GUI import *
from search_field import *
from userDataValidation import *
from DB_connector import *


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    window = QtWidgets.QWidget()
    menu=Main_page()
    menu.setupUi(window)
    Form.show()
    window2=QtWidgets.QWidget()
    search=Filter()
    search.setupUi(window2)


    def page_sign():
        ui.stackedWidget.setCurrentIndex(0)

    def page_log():
        ui.stackedWidget.setCurrentIndex(1)


    def login():
        #DONTUSE ="""
        #CREATE TABLE user (
        #id INT AUTO_INCREMENT PRIMARY KEY,
        #username VARCHAR(30),
        #email VARCHAR(30),
        #password CHAR(60)
        #)
        #"""
        if len(ui.user_or_email.text())!=0 and len(ui.password.text()) !=0 and AuthenticateUser(ui.user_or_email.text(), ui.password.text()):
            window.show()


    def fogort():

        ui.openFogortPage()
    #переключение между логирование и регитсрациец
    ui.to_register.clicked.connect(page_sign)




    def slide_menu():

        width = menu.left_menu.width()

        if width == 50:

            newWidth = 160
        else:

            newWidth = 50

        animation = QPropertyAnimation(menu.left_menu, b"maximumWidth")

        animation.setDuration(1000)

        animation.setStartValue(newWidth)
        animation.setEndValue(width)
        animation.setEasingCurve(QEasingCurve.InCurve)
        animation.start()


    def asd():
        menu.stackedWidget.setCurrentIndex(0)
    def asd2():
        menu.stackedWidget.setCurrentIndex(1)
    def asd3():
        menu.stackedWidget.setCurrentIndex(2)
    def asd4():
        menu.stackedWidget.setCurrentIndex(3)
    def asd5():
        menu.stackedWidget.setCurrentIndex(4)
    def filter_on():

        window2.show()
        menu.pushButton_6.setIcon(QtGui.QIcon(('C:/Users/nikitos/Documents/baza/arrow-up')))


    def filter_off():
        print('asdsad')
        window2.hide()
        print(window2.isActiveWindow())
        menu.pushButton_6.setIcon(QtGui.QIcon(('C:/Users/nikitos/Documents/baza/arrow-down')))

    menu.menu_buttn.clicked.connect(slide_menu)
    menu.pushButton.clicked.connect(asd)
    menu.pushButton_2.clicked.connect(asd2)
    menu.pushButton_3.clicked.connect(asd3)
    menu.pushButton_4.clicked.connect(asd4)
    menu.pushButton_5.clicked.connect(asd5)

    def IsPress():
        print(menu.stackedWidget.currentIndex())
        menu.pushButton_6.setCheckable(True)
        menu.pushButton_6.toggle()
        if menu.pushButton_6.isChecked():
            if window2.isHidden():

                filter_on()
            else:

                filter_off()
    menu.pushButton_6.clicked.connect(IsPress)






    ui.to_login_2.clicked.connect(page_log)




    #кнопки регистрации и логирования
    ui.bttn_forgort.clicked.connect(fogort)
    ui.bttn_login.clicked.connect(login)
    ui.bttn_login.clicked.connect(Form.close)




    sys.exit(app.exec_())
