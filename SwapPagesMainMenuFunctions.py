from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox, QCompleter, QListWidgetItem , QLabel
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import re
import StyleSheetForButtons
from userDataValidation import *
from DB_connector import *
from getFilmsDataFromDB import *
from getDataFromIMDB import *

def homePage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6):
    stackedWidget.setCurrentIndex(0)
    home_button.setStyleSheet(StyleSheetForButtons.home_pressed)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
def favoritePage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6):
    stackedWidget.setCurrentIndex(1)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_pressed)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))

def laterPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6):
    stackedWidget.setCurrentIndex(3)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_pressed)
    pushButton_6.setIcon(QIcon(('arrow-down')))


def histroyPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6):
    stackedWidget.setCurrentIndex(4)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_pressed)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))

def settingsPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6,username,email,id):
    stackedWidget.setCurrentIndex(6)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_pressed)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))

b=getListAllDataAllFilms()
def filter_on(pushButton_6,stackedWidget,actorSearch,country,language,runtime,film):
    pushButton_6.setIcon(QIcon(('arrow-up')))

    global index
    index = stackedWidget.currentIndex()
    list_of_films=[]
    list_of_language=[]
    listOfPeople=[]
    listOfCountries= []
    stackedWidget.setCurrentIndex(5)
    for i in range(len(b)):
        listOfCountries += b[i].country
        listOfPeople+=b[i].actors
        list_of_films.append(b[i].name)
        list_of_language+=b[i].lang


    completer = QCompleter(set(listOfPeople), actorSearch)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    actorSearch.setCompleter(completer)

    completer = QCompleter(set(listOfCountries), country)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    country.setCompleter(completer)

    completer = QCompleter(list_of_films,film)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    film.setCompleter(completer)

    completer = QCompleter(set(list_of_language), language)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    language.setCompleter(completer)




def filter_off(pushButton_6,stackedWidget):
    global index
    print(index)
    stackedWidget.setCurrentIndex(index)
    pushButton_6.setIcon(QIcon(('arrow-down')))



def IsPressSearchButton(pushButton_6,stackedWidget,actorSearch,country,language,runtime,film):

    pushButton_6.setCheckable(True)
    pushButton_6.toggle()

    if pushButton_6.isChecked():
        if stackedWidget.currentIndex() != 5 and stackedWidget.currentIndex() != 2:

            filter_on(pushButton_6,stackedWidget,actorSearch,country,language,runtime,film)

        elif stackedWidget.currentIndex() == 2:
            pass
        else:

            filter_off(pushButton_6,stackedWidget)


def about_film_page(stackedWidget,button_name,Name_of_film,Overview_text,date_country_genres_runtime,image,actors,score,current_page):
    try:
        id =re.sub("[^0-9]", "", button_name)
        print(type(id))
        a = getAllDataFilmByID(str(int(id)+(int(current_page.text())-1)*18))

        global index
        index = stackedWidget.currentIndex()
        actors.setText(a.actors.replace(';',', '))
        binary_data = base64.b64decode(a.images)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(binary_data)
        score.setText(str(a.score))
        image.setScaledContents(True)
        image.setPixmap((pixmap))
        Name_of_film.setText(a.name+' '+'('+str(a.release)+')')
        Overview_text.setText(a.description)
        date_country_genres_runtime.setText((a.country).replace(';','')+"("+(a.lang).replace(';','')+")"+" | "+(a.genres).replace(';',', ')+" | "+str(a.runtime)+" min ")
        stackedWidget.setCurrentIndex(2)
    except:
        pass








def back(stackedWidget):
    global index
    stackedWidget.setCurrentIndex(index)