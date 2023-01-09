from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt,QSize
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox, QCompleter, QListWidgetItem , QLabel , QCheckBox, QLineEdit,QDateEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import re
import time
from multiprocessing import Process
import StyleSheetForButtons
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
from LogicApplication.getAndSetDataFilmStatusUser import *
from LogicApplication.getAndSetReviews import *
alldata=getListAllDataAllFilms()
def getfav(id):
    global favfilm
    favfilm=getUsersFavoriteFilms(id)
def getlat(id):
    global latfilm
    latfilm = getUsersWatchLaterFilms(id)
def gethis(id):
    global hisfilm
    hisfilm = getUsersWatchedFilms(id)
def homePage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6):
    stackedWidget.setCurrentIndex(0)
    home_button.setStyleSheet(StyleSheetForButtons.home_pressed)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
def favoritePage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6,allbutton,userid,currentPage,next_button):
    stackedWidget.setCurrentIndex(1)
    currentPage.setText('1')
    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_pressed)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    userid1 = re.sub("[^0-9]", "", userid.text())

    filmID = getUsersFavoriteFilms(userid1)


    button = allbutton.findChildren(QPushButton)
    labels = allbutton.findChildren(QLabel)
    dict2 = {}
    labelDict = {}
    for i in range(18):
        bttn_number = re.sub("[^0-9]", "", button[i].objectName())
        label_number = re.sub("[^0-9]", "", labels[i].objectName())
        dict2[int(bttn_number)] = button[i]
        labelDict[int(label_number)] = labels[i]
    dict2 = dict(sorted(dict2.items()))
    labelDict = dict(sorted(labelDict.items()))
    try:
        for i in range(18):
            bttn=(dict2.get(int(i)+1))
            label=labelDict.get(int(i)+1)
            binary_data = base64.b64decode(alldata[filmID[i]-1].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[filmID[i]-1].name)
            bttn.setEnabled(True)
    except:

        for i in range(len(filmID)):
            bttn=(dict2.get(int(i)+1))
            label=labelDict.get(int(i)+1)
            binary_data = base64.b64decode(alldata[filmID[i]-1].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[filmID[i]-1].name)
            bttn.setEnabled(True)
        for i in range(len(filmID),18):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            bttn.setIconSize(QSize(0, 0))
            label.setText('')
            bttn.setEnabled(False)

def laterPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6,allbutton,userid,currentPage,next_button):
    stackedWidget.setCurrentIndex(3)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_pressed)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    currentPage.setText('1')
    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
    userid1 = re.sub("[^0-9]", "", userid.text())
    filmID = getUsersWatchLaterFilms(userid1)
    button = allbutton.findChildren(QPushButton)
    labels = allbutton.findChildren(QLabel)
    dict2 = {}
    labelDict = {}
    for i in range(18):
        bttn_number = re.sub("[^0-9]", "", button[i].objectName())
        label_number = re.sub("[^0-9]", "", labels[i].objectName())
        dict2[int(bttn_number)] = button[i]
        labelDict[int(label_number)] = labels[i]
    dict2 = dict(sorted(dict2.items()))
    labelDict = dict(sorted(labelDict.items()))
    try:
        for i in range(18):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            binary_data = base64.b64decode(alldata[filmID[i] - 1].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[filmID[i] - 1].name)
            bttn.setEnabled(True)
    except:

        for i in range(len(filmID)):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            binary_data = base64.b64decode(alldata[filmID[i] - 1].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[filmID[i] - 1].name)
            bttn.setEnabled(True)
        for i in range(len(filmID), 18):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            print((int(i) + 1))
            bttn.setIconSize(QSize(0, 0))
            label.setText('')
            bttn.setEnabled(False)

def histroyPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6,allbutton,userid,currentPage,next_button):
    stackedWidget.setCurrentIndex(4)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_pressed)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    currentPage.setText('1')
    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
    userid1 = re.sub("[^0-9]", "", userid.text())
    filmID = getUsersWatchedFilms(userid1)
    button = allbutton.findChildren(QPushButton)
    labels = allbutton.findChildren(QLabel)
    dict2 = {}
    labelDict = {}
    for i in range(18):
        print(labels[i].objectName())
        bttn_number = re.sub("[^0-9]", "", button[i].objectName())
        label_number = re.sub("[^0-9]", "", labels[i].objectName())
        dict2[int(bttn_number)] = button[i]
        labelDict[int(label_number)] = labels[i]
    dict2 = dict(sorted(dict2.items()))
    labelDict = dict(sorted(labelDict.items()))
    try:
        for i in range(18):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            binary_data = base64.b64decode(alldata[filmID[i] - 1].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[filmID[i] - 1].name)
            bttn.setEnabled(True)
    except:

        for i in range(len(filmID)):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            binary_data = base64.b64decode(alldata[filmID[i] - 1].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[filmID[i] - 1].name)
            bttn.setEnabled(True)
        for i in range(len(filmID), 18):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            print((int(i) + 1))
            bttn.setIconSize(QSize(0, 0))
            label.setText('')
            bttn.setEnabled(False)
def settingsPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6,username,email,id,setuser,setid):
    stackedWidget.setCurrentIndex(6)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_pressed)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    username.setText(str(setuser))
    id.setText(str(setid))



def filter_on(pushButton_6,stackedWidget,actorSearch,country,language,runtime,film):
    pushButton_6.setIcon(QIcon(('arrow-up')))

    global index
    index = stackedWidget.currentIndex()
    list_of_films=[]
    list_of_language=[]
    listOfPeople=[]
    listOfCountries= []
    stackedWidget.setCurrentIndex(5)
    for i in range(len(alldata)):
        listOfCountries += alldata[i].country
        listOfPeople+=alldata[i].actors
        list_of_films.append(alldata[i].name)
        list_of_language+=alldata[i].lang


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


def about_film_page(stackedWidget,button_name,Name_of_film,Overview_text,date_country_genres_runtime,image,actors,score,current_page,favorite,userid,idFilmFromHome,lat,his):
    try:
        userid1 = re.sub("[^0-9]", "", userid.text())
        id =re.sub("[^0-9]", "", button_name)
        idFilmFromHome.setText(str(int(id)+(int(current_page.text())-1)*18))
        idFilmFromHome.setStyleSheet('color:rgb(42, 54, 63)')
        filminxed=str(int(id)+(int(current_page.text())-1)*18)



        s = Process(target=getfav, args=(userid1))
        s2 = Process(target=getlat, args=(userid1))
        s3 = Process(target=gethis, args=(userid1))

        s.start()
        s2.start()
        s3.start()
        pop=False

        while pop==False:
            try:
                a = getAllDataFilmByID(filminxed)
                pop=True
            except:

                for i in range(int(filminxed),int(filminxed)+20):
                    try:
                        a = getAllDataFilmByID(i)
                        pop=True
                        break
                    except:
                        pop = False







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
        date_country_genres_runtime.setText(
            (a.country).replace(';', '') + "(" + (a.lang).replace(';', '') + ")" + " | " + (a.genres).replace(';',
                                                                                                              ', ') + " | " + str(
                a.runtime) + " min ")
        stackedWidget.setCurrentIndex(2)
        favorite.setStyleSheet('background-color: rgb(42, 54, 63)')
        lat.setStyleSheet('background-color: rgb(42, 54, 63)')
        his.setStyleSheet('background-color: rgb(42, 54, 63)')
        filmid = int(int(id)+(int(current_page.text())-1)*18)






        if filmid in favfilm:
            favorite.setStyleSheet('background-color: #696d6d')
        elif filmid in latfilm:
            lat.setStyleSheet('background-color: #696d6d')
        elif filmid in hisfilm:
            his.setStyleSheet('background-color: #696d6d')







    except:
        pass



def aboutFilmFromNotHome(stackedWidget, button_name,Name_of_film, Overview_text,date_country_genres_runtime,image, actors,score, current_page_home,favorite,userid,lat,his,frame,current_page,idFilmFromHome,frameForFilter,actor,language,country,run,date_from,date_to):

        userid1 = re.sub("[^0-9]", "", userid.text())
        id =re.sub("[^0-9]", "", button_name)
        page=int(current_page.text())-1



        filmId=0
        if frame.objectName() =='frame_where_all_films_favorite':
            filmsID = getUsersFavoriteFilms(userid1)

            filmId = filmsID[int(id)-1+page*18]
        elif frame.objectName() =='frame_where_all_films_watch_later':
            filmsID = getUsersWatchLaterFilms(userid1)
            filmId = filmsID[int(id)-1+page*18]
        elif frame.objectName() =='frame_where_all_films_history_page':
            filmsID = getUsersWatchedFilms(userid1)
            filmId = filmsID[int(id)-1+page*18]
        else:
            try:
                if actor.text() != '':
                    a = getListAllFilmsWithPeopleUser(actor.text())
                elif int(date_from.text()) != 2000 and int(date_to.text()) != 2000:
                    a = getAllDataFilmByReleaseDataBetween(str(date_from.text()), str(date_to.text()))
                elif language.text() != '':
                    a = getAllDataFilmByLanguage(language.text())
                elif country.text() != '':
                    a = getAllDataFilmByCountry(country.text())

                else:
                    genersList = []
                    checkbox = frameForFilter.findChildren(QCheckBox)

                    for i in range(len(checkbox)):

                        if checkbox[i].isChecked():
                            if checkbox[i].objectName() == 'checkBoxGameShow':
                                genersList.append('Game-Show')
                            elif checkbox[i].objectName() == 'checkBoxRealityTV':
                                genersList.append('Reality-TV')
                            elif checkbox[i].objectName() == 'checkBoxTalkShow':
                                genersList.append('Talk-Show')
                            elif checkbox[i].objectName() == 'checkBoxFilmNoir':
                                genersList.append('Film-Noir')
                            else:
                                genersList.append((checkbox[i].objectName()).replace('checkBox', ''))
                a = getListAllFilmWithGenresUser(genersList)

            except:
                pass




            filmId = int(a[int(id) - 1 + page * 18].id)








        idFilmFromHome.setText(str(filmId))
        idFilmFromHome.setStyleSheet('color:rgb(42, 54, 63)')


        global index
        index = stackedWidget.currentIndex()
        try:
            actors.setText(str(alldata[filmId-1].actors).replace(';',', '))
        except:
            pop =False
            while pop==False:
                for i in range(100):
                    try:
                        actors.setText(str(alldata[filmId - i].actors).replace(';', ', '))
                        filmId=filmId-i
                        pop=True
                        break
                    except:
                        pop = False
            filmId+=1
            pop = True
        binary_data = base64.b64decode(alldata[filmId-1].images)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(binary_data)
        score.setText(str(str(alldata[filmId-1].score)))
        image.setScaledContents(True)
        image.setPixmap((pixmap))
        Name_of_film.setText(str(alldata[filmId-1].name)+' '+'('+str(alldata[filmId-1].release)+')')
        without_brackets = re.sub(r"[\(\)]", "", str(Name_of_film.text()))



        Overview_text.setText(str((alldata[filmId-1].description)))
        date_country_genres_runtime.setText(str((alldata[filmId-1].country)).replace(';','')+"("+str(alldata[filmId-1].lang).replace(';','')+")"+" | "+str(alldata[filmId-1].genres).replace(';',', ')+" | "+str(alldata[filmId-1].runtime)+" min ")
        stackedWidget.setCurrentIndex(2)
        favorite.setStyleSheet('background-color: rgb(42, 54, 63)')
        lat.setStyleSheet('background-color: rgb(42, 54, 63)')
        his.setStyleSheet('background-color: rgb(42, 54, 63)')
        if filmId in getUsersFavoriteFilms(userid1):
            favorite.setStyleSheet('background-color: #696d6d')

        elif filmId in getUsersWatchLaterFilms(userid1):
            lat.setStyleSheet('background-color: #696d6d')
        elif filmId in getUsersWatchedFilms(userid1):
            his.setStyleSheet('background-color: #696d6d')





def back(stackedWidget):
    global index
    stackedWidget.setCurrentIndex(index)