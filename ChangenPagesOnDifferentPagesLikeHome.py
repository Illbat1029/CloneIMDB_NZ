
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt ,QSize
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton ,QLabel

a = getListAllDataAllFilms()
def next_page_home(current_page_home,all_button_name,next_button):
    if current_page_home.text() != 'last':

            stranica = int(current_page_home.text()) + 1
            current_page_home.setText(str(stranica))

            button=all_button_name.findChildren(QPushButton)
            labels = all_button_name.findChildren(QLabel)


            for i in range(18):
                bttn_number=re.sub("[^0-9]", "", button[i].objectName())
                label_number = re.sub("[^0-9]", "", labels[i].objectName())
                try:
                    binary_data = base64.b64decode(a[(int(bttn_number)-1)+18*(stranica-1)].images)
                    labels[i].setText(a[(int(bttn_number)-1)+18*(stranica-1)].name)
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(binary_data)
                    button[i].setIconSize(QSize(100, 140))
                    button[i].setIcon(QIcon(pixmap))
                except:
                    button[i].setIconSize(QSize(0, 0))
                    labels[i].setText('')
                    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)





# Страница нахад в разделе хоум
def back_page_home(current_page_home,all_button_name,next_button):
    if current_page_home.text() != '1':
        x = 0
        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        # Print the button's name

        stranica = int(current_page_home.text())

        current_page_home.setText(str(stranica - 1))
        button = all_button_name.findChildren(QPushButton)
        labels = all_button_name.findChildren(QLabel)
        for i in range(18):
            bttn_number = re.sub("[^0-9]", "", button[i].objectName())
            label_number = re.sub("[^0-9]", "", labels[i].objectName())
            binary_data = base64.b64decode(a[(stranica-2)*18+int(bttn_number)-1].images)
            labels[i].setText(a[(stranica-2)*18+int(bttn_number)-1].name)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            button[i].setIconSize(QSize(100, 140))
            button[i].setIcon(QIcon(pixmap))
#

# переключает след старницу в разедле фаворит
def next_page_favorite(current_page_favorite,pagr_next_button_favorite,page_next2_button_favorite):
    if current_page_favorite.text() != 'last':
        x = 0

        # Print the button's name

        stranica = int(current_page_favorite.text()) + 1
        current_page_favorite.setText(str(stranica))
        pagr_next_button_favorite.setText(str(int(pagr_next_button_favorite.text()) + 1))
        page_next2_button_favorite.setText(str(int(page_next2_button_favorite.text()) + 1))

       # for i in film_bttn:
        #    i = i[14:]

         #   # сюда подставить фото с базы данных потом
         #   png = "border-image: url(Film_" + str(int(i) + (stranica - 1) * 18) + ".jpg);"
          #  film_bttn_not_text[x].setStyleSheet(png)
          #  x += 1


def back_page_favorite(current_page_favorite,pagr_next_button_favorite,page_next2_button_favorite):
    if current_page_favorite.text() != '1':
        x = 0

        # Print the button's name
        pagr_next_button_favorite.setText(str(int(pagr_next_button_favorite.text()) - 1))
        page_next2_button_favorite.setText(str(int(page_next2_button_favorite.text()) - 1))
        stranica = int(current_page_favorite.text())

        current_page_favorite.setText(str(stranica - 1))

       # for i in film_bttn:
         #   i = i[14:]

          #  # Подставить фото
           # png = "border-image: url(Film_" + str((stranica - 2) * 18 + (int(i))) + ".jpg);"
           # film_bttn_not_text[x].setStyleSheet(png)
           # x += 1


def next_page_later(current_page_watch_later,pagr_next_button_watch_later,page_next2_button_watch_later):
    if current_page_watch_later.text() != 'last':
        x = 0

        # Print the button's name

        stranica = int(current_page_watch_later.text()) + 1
        current_page_watch_later.setText(str(stranica))
        pagr_next_button_watch_later.setText(str(int(pagr_next_button_watch_later.text()) + 1))
        page_next2_button_watch_later.setText(str(int(page_next2_button_watch_later.text()) + 1))

       # for i in film_bttn:
        #    i = i[14:]
#
        #    # сюда подставить фото с базы данных потом
         #   png = "border-image: url(Film_" + str(int(i) + (stranica - 1) * 18) + ".jpg);"
         #   film_bttn_not_text[x].setStyleSheet(png)
         #   x += 1


def back_page_later(current_page_watch_later,pagr_next_button_watch_later,page_next2_button_watch_later):
    if current_page_watch_later.text() != '1':
        x = 0

        # Print the button's name
        pagr_next_button_watch_later.setText(str(int(pagr_next_button_watch_later.text()) - 1))
        page_next2_button_watch_later.setText(str(int(page_next2_button_watch_later.text()) - 1))
        stranica = int(current_page_watch_later.text())

        current_page_watch_later.setText(str(stranica - 1))

        #for i in film_bttn:
        #    i = i[14:]

            # Подставить фото
        #    png = "border-image: url(Film_" + str((stranica - 2) * 18 + (int(i))) + ".jpg);"
        #    film_bttn_not_text[x].setStyleSheet(png)
         #   x += 1


def next_page_history(current_page_history,pagr_next_button_history,page_next2_button_history):
    if current_page_history.text() != 'last':
        x = 0

        # Print the button's name

        stranica = int(current_page_history.text()) + 1
        current_page_history.setText(str(stranica))
        pagr_next_button_history.setText(str(int(pagr_next_button_history.text()) + 1))
        page_next2_button_history.setText(str(int(page_next2_button_history.text()) + 1))

      #  for i in film_bttn:
        #    i = i[14:]

        #    # сюда подставить фото с базы данных потом
         #   png = "border-image: url(Film_" + str(int(i) + (stranica - 1) * 18) + ".jpg);"
          ##  film_bttn_not_text[x].setStyleSheet(png)
         #   x += 1


def back_page_history(current_page_history,pagr_next_button_history,page_next2_button_history):
    if current_page_history.text() != '1':
        x = 0

        # Print the button's name
        pagr_next_button_history.setText(str(int(pagr_next_button_history.text()) - 1))
        page_next2_button_history.setText(str(int(page_next2_button_history.text()) - 1))
        stranica = int(current_page_history.text())

        current_page_history.setText(str(stranica - 1))

        #for i in film_bttn:
          #  i = i[14:]

            # Подставить фото
           # png = "border-image: url(Film_" + str((stranica - 2) * 18 + (int(i))) + ".jpg);"
          #  film_bttn_not_text[x].setStyleSheet(png)
          #  x += 1
