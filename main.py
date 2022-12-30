
import sys
import os
from datetime import datetime, timedelta

from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QPushButton, QSizePolicy

from Login_page import *
from main_page import *
from forgot_GUI import *
from search_field import *
from userDataValidation import *
from DB_connector import *


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    #homepage index=0
    #favorite_page index=1
    #about film index=3


    #создает окно логованя и регистрации
    Log_page_form = QtWidgets.QWidget()
    Log_page = Ui_Form()
    Log_page.setupUi(Log_page_form)

    #Показывает окно логованя или регистрации
    Log_page_form.show()

    # создает главное окно
    Main_page_form = QtWidgets.QWidget()
    Main_page = Main_page()
    Main_page.setupUi(Main_page_form)

    #Создает окно забыл пароль
    Fogort_page_from=QtWidgets.QWidget()
    Fogort_page=Forgot_page()
    Fogort_page.setupUi(Fogort_page_from)


    #переключает на страницу где регистрация
    def page_sign():
        Log_page.stackedWidget.setCurrentIndex(0)
    #переключает на страницу где логоване
    def page_log():
        Log_page.stackedWidget.setCurrentIndex(1)
    def login():

        if len(Log_page.user_or_email.text()) != 0 and len(Log_page.password.text()) != 0 and AuthenticateUser(Log_page.user_or_email.text(), Log_page.password.text()):
            dataUser = getDataUser([Log_page.user_or_email.text()])
            updateLastVisitDataTime(dataUser[0])
            Main_page_form.show()
            Log_page_form.close()
        else:
            Log_page.push_up_login_notifikation.setFixedSize(276,10)
    def addFilms():
        a = 1
        stime = datetime.now()
        for i in range(112031, 112032):  # 112161
            try:
                getDataFilmIMDB(i, a)
                a = a + 1
                print(50 * "=")
            except:
                print("BAD URL")
                continue
        print("TIME ADDED FILMS = ", datetime.now() - stime)
        print(50 * "=")
        print(50 * "-")
        print("FILMS COUNT = ", a)
        print(50 * "-")
    def register():
        #sendMailForgoutPassword(Log_page.email.text())
        RegistrationUser(Log_page.username.text(), Log_page.email.text(), Log_page.password_sign.text(), Log_page.reapet_passwd.text())
    def fogort():
        Fogort_page_from.show()
    def slide_menu():

        width = Main_page.left_menu.width()

        if width == 50:

            newWidth = 160
        else:

            newWidth = 50

        animation = QPropertyAnimation(Main_page.left_menu, b"maximumWidth")

        animation.setDuration(1000)

        animation.setStartValue(newWidth)
        animation.setEndValue(width)
        animation.setEasingCurve(QEasingCurve.InCurve)
        animation.start()



    #Переключает на домашнию страницу
    def home():

        Main_page.stackedWidget.setCurrentIndex(0)
        Main_page.pushButton_6.setIcon(QtGui.QIcon(('C:/Users/nikitos/Documents/baza/arrow-down')))


    # Переключает на страницу любимое
    def favorite():
        Main_page.stackedWidget.setCurrentIndex(1)
        Main_page.pushButton_6.setIcon(QtGui.QIcon(('C:/Users/nikitos/Documents/baza/arrow-down')))


    # Переключает на страницу позже
    def later():
        Main_page.stackedWidget.setCurrentIndex(3)
        Main_page.pushButton_6.setIcon(QtGui.QIcon(('C:/Users/nikitos/Documents/baza/arrow-down')))


    # Переключает на страницу история
    def history():
        Main_page.stackedWidget.setCurrentIndex(4)
        Main_page.pushButton_6.setIcon(QtGui.QIcon(('C:/Users/nikitos/Documents/baza/arrow-down')))


    # Переключает на страницу настроек
    def settings():
        Main_page.stackedWidget.setCurrentIndex(6)
        Main_page.pushButton_6.setIcon(QtGui.QIcon(('C:/Users/nikitos/Documents/baza/arrow-down')))


    # Переключает на страницу с фильтром фильмов
    def filter_on():
        global index
        index = Main_page.stackedWidget.currentIndex()
        Main_page.stackedWidget.setCurrentIndex(5)
        Main_page.pushButton_6.setIcon(QtGui.QIcon(('C:/Users/nikitos/Documents/baza/arrow-up')))

    #отключает страницу с фильтром фильмов
    def filter_off():

        Main_page.stackedWidget.setCurrentIndex(index)
        Main_page.pushButton_6.setIcon(QtGui.QIcon(('C:/Users/nikitos/Documents/baza/arrow-down')))

    #страничка в которой содержиться инфа о фильме
    def about_film():
        global index
        index = Main_page.stackedWidget.currentIndex()
       # Main_page.Name_of_film_and_year.setText(str) поле с названием фильма и сразу же год
        #Main_page.date_country_genres_runtime.setText(str) после с временем старнйо жанрмами и длительностью
        #Main_page.Score_of_film.setText(str) поле с оценкой
       # Main_page.Tags_for_film.setText(str) тэги
        #Main_page.Overview_text.setText(str) овервью тьоесть описание
       # Main_page.first_actor_name.setText(str)
        #Main_page.second_actor_name.setText(str)
        #Main_page.third_actor_name.setText(str)
        #Main_page.fourth_actor_name.setText(str) с фото то же самое

        Main_page.stackedWidget.setCurrentIndex(2)

    #возвращает на прошулую страницу со страницы о фильме
    def back():

        Main_page.stackedWidget.setCurrentIndex(index)



    def sent_forgot():


        Fogort_page.wrong_email.setFixedSize(276, 10)
        Fogort_page.wrong_code.setFixedSize(276, 10)
        Fogort_page.wrong_password.setFixedSize(276, 10)
        Fogort_page.confirm_password_error.setFixedSize(276, 10)






    film_bttn = []
    film_bttn_not_text = []
    buttons = Main_page.widget.findChildren(QPushButton)
    for button in buttons:

        for i in range(40):
            if button.objectName() == 'home_film_bttn' + str(i):
                film_bttn.append(button.objectName())
                print(button.objectName())
                film_bttn_not_text.append(button)
                # print(button.objectName())
                png = "border-image: url(Film_" + str(i) + ".jpg);"
                button.setStyleSheet(png)


    #переключает след старницу в разедле хоум
    def next_page_home():

        if Main_page.current_page_home.text() != 'last':
            x = 0

            # Print the button's name

            stranica = int(Main_page.current_page_home.text()) + 1
            Main_page.current_page_home.setText(str(stranica))
            Main_page.pagr_next_button_home.setText(str(int(Main_page.pagr_next_button_home.text()) + 1))
            Main_page.page_next2_button_home.setText(str(int(Main_page.page_next2_button_home.text()) + 1))

            for i in film_bttn:
                i = i[14:]

                #сюда подставить фото с базы данных потом
                png = "border-image: url(Film_" + str(int(i) + (stranica - 1) * 18) + ".jpg);"
                film_bttn_not_text[x].setStyleSheet(png)
                x += 1

    #Страница нахад в разделе хоум
    def back_page_home():

        if Main_page.current_page_home.text() != '1':
            x = 0

            # Print the button's name
            Main_page.pagr_next_button_home.setText(str(int(Main_page.pagr_next_button_home.text()) - 1))
            Main_page.page_next2_button_home.setText(str(int(Main_page.page_next2_button_home.text()) -1))
            stranica = int(Main_page.current_page_home.text())

            Main_page.current_page_home.setText(str(stranica - 1))

            for i in film_bttn:
                i = i[14:]

                #Подставить фото
                png = "border-image: url(Film_" + str((stranica - 2) * 18 + (int(i))) + ".jpg);"
                film_bttn_not_text[x].setStyleSheet(png)
                x += 1

    # переключает след старницу в разедле фаворит
    def next_page_favorite():

        if Main_page.current_page_favorite.text() != 'last':
            x = 0

            # Print the button's name

            stranica = int(Main_page.current_page_favorite.text()) + 1
            Main_page.current_page_favorite.setText(str(stranica))
            Main_page.pagr_next_button_favorite.setText(str(int(Main_page.pagr_next_button_favorite.text()) + 1))
            Main_page.page_next2_button_favorite.setText(str(int(Main_page.page_next2_button_favorite.text()) + 1))

            for i in film_bttn:
                i = i[14:]

                #сюда подставить фото с базы данных потом
                png = "border-image: url(Film_" + str(int(i) + (stranica - 1) * 18) + ".jpg);"
                film_bttn_not_text[x].setStyleSheet(png)
                x += 1

    def back_page_favorite():

        if Main_page.current_page_favorite.text() != '1':
            x = 0

            # Print the button's name
            Main_page.pagr_next_button_favorite.setText(str(int(Main_page.pagr_next_button_favorite.text()) - 1))
            Main_page.page_next2_button_favorite.setText(str(int(Main_page.page_next2_button_favorite.text()) - 1))
            stranica = int(Main_page.current_page_favorite.text())

            Main_page.current_page_favorite.setText(str(stranica - 1))

            for i in film_bttn:
                i = i[14:]

                # Подставить фото
                png = "border-image: url(Film_" + str((stranica - 2) * 18 + (int(i))) + ".jpg);"
                film_bttn_not_text[x].setStyleSheet(png)
                x += 1

    def next_page_later():

        if Main_page.current_page_watch_later.text() != 'last':
            x = 0

            # Print the button's name

            stranica = int(Main_page.current_page_watch_later.text()) + 1
            Main_page.current_page_watch_later.setText(str(stranica))
            Main_page.pagr_next_button_watch_later.setText(str(int(Main_page.pagr_next_button_watch_later.text()) + 1))
            Main_page.page_next2_button_watch_later.setText(str(int(Main_page.page_next2_button_watch_later.text()) + 1))

            for i in film_bttn:
                i = i[14:]

                #сюда подставить фото с базы данных потом
                png = "border-image: url(Film_" + str(int(i) + (stranica - 1) * 18) + ".jpg);"
                film_bttn_not_text[x].setStyleSheet(png)
                x += 1

    def back_page_later():

        if Main_page.current_page_watch_later.text() != '1':
            x = 0

            # Print the button's name
            Main_page.pagr_next_button_watch_later.setText(str(int(Main_page.pagr_next_button_watch_later.text()) - 1))
            Main_page.page_next2_button_watch_later.setText(str(int(Main_page.page_next2_button_watch_later.text()) - 1))
            stranica = int(Main_page.current_page_watch_later.text())

            Main_page.current_page_watch_later.setText(str(stranica - 1))

            for i in film_bttn:
                i = i[14:]

                # Подставить фото
                png = "border-image: url(Film_" + str((stranica - 2) * 18 + (int(i))) + ".jpg);"
                film_bttn_not_text[x].setStyleSheet(png)
                x += 1

    def next_page_history():

        if Main_page.current_page_history.text() != 'last':
            x = 0

            # Print the button's name

            stranica = int(Main_page.current_page_history.text()) + 1
            Main_page.current_page_history.setText(str(stranica))
            Main_page.pagr_next_button_history.setText(str(int(Main_page.pagr_next_button_history.text()) + 1))
            Main_page.page_next2_button_history.setText(str(int(Main_page.page_next2_button_history.text()) + 1))

            for i in film_bttn:
                i = i[14:]

                #сюда подставить фото с базы данных потом
                png = "border-image: url(Film_" + str(int(i) + (stranica - 1) * 18) + ".jpg);"
                film_bttn_not_text[x].setStyleSheet(png)
                x += 1

    def back_page_history():

        if Main_page.current_page_history.text() != '1':
            x = 0

            # Print the button's name
            Main_page.pagr_next_button_history.setText(str(int(Main_page.pagr_next_button_history.text()) - 1))
            Main_page.page_next2_button_history.setText(str(int(Main_page.page_next2_button_history.text()) - 1))
            stranica = int(Main_page.current_page_history.text())

            Main_page.current_page_history.setText(str(stranica - 1))

            for i in film_bttn:
                i = i[14:]

                # Подставить фото
                png = "border-image: url(Film_" + str((stranica - 2) * 18 + (int(i))) + ".jpg);"
                film_bttn_not_text[x].setStyleSheet(png)
                x += 1

    #открытие фильтра поиска
    def IsPress():

        Main_page.pushButton_6.setCheckable(True)
        Main_page.pushButton_6.toggle()

        if Main_page.pushButton_6.isChecked():
            if Main_page.stackedWidget.currentIndex() != 5 and Main_page.stackedWidget.currentIndex() != 2:

                filter_on()

            elif Main_page.stackedWidget.currentIndex() == 2:
                pass
            else:

                filter_off()



    # кнопка фильтра проверка
    Main_page.pushButton_6.clicked.connect(IsPress)

    # кнопка страница вперед в разделе хоум
    Main_page.next_button_home.clicked.connect(next_page_home)

    #кнопка страница назад в разделе хоум
    Main_page.previos_page_button_home.clicked.connect(back_page_home)

    # кнопка страница вперед в разделе фаворит
    Main_page.next_button_favorite.clicked.connect(next_page_favorite)

    # кнопка страница назад в разделе фаворит
    Main_page.previos_page_button_favorite.clicked.connect(back_page_favorite)

    # кнопка страница вперед в разделе позже
    Main_page.next_button_watch_later.clicked.connect(next_page_later)

    # кнопка страница назад в разделе позже
    Main_page.previos_page_button_watch_later.clicked.connect(back_page_later)

    # кнопка страница вперед в разделе история
    Main_page.next_button_history.clicked.connect(next_page_history)

    # кнопка страница назад в разделе истроия
    Main_page.previos_page_button_history.clicked.connect(back_page_history)

    #переключится на сраницу логованя
    Log_page.to_login_2.clicked.connect(page_log)

    # кнопки регистрации и логирования
    Log_page.bttn_forgort.clicked.connect(fogort)
    Log_page.bttn_login.clicked.connect(login)

    #удлинение рассширение территории меню
    Main_page.menu_buttn.clicked.connect(slide_menu)

    #кнопка домой
    Main_page.home_button.clicked.connect(home)

    #кнопка любимое
    Main_page.favorite_button.clicked.connect(favorite)

    #кнопка посже
    Main_page.watch_later_button.clicked.connect(later)

    #кнопка история
    Main_page.histor_button.clicked.connect(history)

    #кнопка настрйокми
    Main_page.settings_button.clicked.connect(settings)

    #кнопка про информацию о фильме
    for button in buttons:

        if button.objectName()[:9] == 'home_film' or button.objectName()[:13]=='favorite_film' or button.objectName()[:16 ]=='watch_later_film' or button.objectName()[:12 ]=='history_film':
            if "border-image" in  button.styleSheet():

                button.clicked.connect(about_film)


    #кнопка назад из онка с инфой о фильме
    Main_page.back_buttn.clicked.connect(back)

    Fogort_page.sent_forgot_page.clicked.connect(sent_forgot)

    # переключение между логирование и регитсрациец
    Log_page.to_register.clicked.connect(page_sign)
    sys.exit(app.exec_())