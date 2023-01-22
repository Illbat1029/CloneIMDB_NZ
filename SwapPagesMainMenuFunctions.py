import time

from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt,QSize
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox, QCompleter, QListWidgetItem , QLabel , QCheckBox, QLineEdit,QDateEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from functools import lru_cache
import StyleSheetForButtons
from LogicApplication.userDataValidation import *

from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
from LogicApplication.getAndSetDataFilmStatusUser import *
start_time=time.time()
alldata=getListAllDataAllFilms()
end_time=time.time()
print(end_time-start_time)
@lru_cache()
def cache(id):

    return getAllDataFilmByID(id)

def homePage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6, admin_button, moder_button,home_page,current_page):
    stackedWidget.setCurrentIndex(0)
    current_page.setText('1')
    home_button.setStyleSheet(StyleSheetForButtons.home_pressed)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    moder_button.setStyleSheet(StyleSheetForButtons.moder_default)
    admin_button.setStyleSheet(StyleSheetForButtons.admin_default)
    film_bttn ={}
    film_bttn_not_text = {}
    film_name = {}
    film_name_not_text = {}
    buttons = home_page.findChildren(QPushButton)
    Labels = home_page.findChildren(QLabel)
    for button in buttons:
        for i in range(19):
            if button.objectName() == 'home_film_bttn' + str(i):
                film_bttn[i]=button.objectName()
                film_bttn_not_text[i]=button
    for label in Labels:
        for i in range(19):
            if label.objectName() == 'home_name_film' + str(i):

                film_name_not_text[i]=label




    x=0
    for i in film_bttn_not_text.keys():
        binary_data = base64.b64decode(alldata[i-1].images)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(binary_data)
        film_name_not_text[i].setText(alldata[i-1].name)
        film_bttn_not_text[i].setIconSize(QSize(100, 140))
        film_bttn_not_text[i].setIcon(QIcon(pixmap))

def favoritePage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6, admin_button, moder_button, allbutton,userid,currentPage,next_button):
    time_start1 = time.time()
    global filmIDFavorite
    stackedWidget.setCurrentIndex(1)
    currentPage.setText('1')
    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_pressed)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    moder_button.setStyleSheet(StyleSheetForButtons.moder_default)
    admin_button.setStyleSheet(StyleSheetForButtons.admin_default)
    userid1 = re.sub("[^0-9]", "", userid.text())

    filmIDFavorite = getUsersFavoriteFilms(userid1)

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
        time_start = time.time()
        for i in range(18):
            k=1
            filminxed = str(filmIDFavorite[i])
            filminxed2 = str(filmIDFavorite[i])
            x = (alldata[int(filminxed) - 1].id)
            while alldata[int(filminxed) - k].id != int(filminxed2):
                k+=1
            bttn=(dict2.get(int(i)+1))
            label=labelDict.get(int(i)+1)

          #  b=cache(filmID[i])
            binary_data = base64.b64decode(alldata[int(filminxed) - k].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[int(filminxed) - k].name)
            bttn.setEnabled(True)
            end_start = time.time()
        print(end_start - time_start)
    except:

        for i in range(len(filmIDFavorite)):
            k = 1
            filminxed = str(filmIDFavorite[i])
            filminxed2 = str(filmIDFavorite[i])
            x = (alldata[int(filminxed) - 1].id)
            while alldata[int(filminxed) - k].id != int(filminxed2):
                k += 1
            bttn=(dict2.get(int(i)+1))
            label=labelDict.get(int(i)+1)
            binary_data = base64.b64decode(alldata[int(filminxed) - k].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[int(filminxed) - k].name)
            bttn.setEnabled(True)
        for i in range(len(filmIDFavorite),18):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            bttn.setIconSize(QSize(0, 0))
            label.setText('')
            bttn.setEnabled(False)
    end_start1 = time.time()
    print("открытие вкладки любимое "+str(end_start1 - time_start1))

def laterPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6, admin_button, moder_button, allbutton,userid,currentPage,next_button):
    time_start1 = time.time()
    global filmIDLater
    stackedWidget.setCurrentIndex(3)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_pressed)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    moder_button.setStyleSheet(StyleSheetForButtons.moder_default)
    admin_button.setStyleSheet(StyleSheetForButtons.admin_default)
    currentPage.setText('1')
    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
    userid1 = re.sub("[^0-9]", "", userid.text())
    filmIDLater = getUsersWatchLaterFilms(userid1)
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
            #b=cache(filmID[i])
            k = 1
            filminxed = str(filmIDLater[i])
            filminxed2 = str(filmIDLater[i])
            x = (alldata[int(filminxed) - 1].id)
            while alldata[int(filminxed) - k].id != int(filminxed2):
                k += 1
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            binary_data = base64.b64decode(alldata[int(filminxed) - k].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[int(filminxed) - k].name)
            bttn.setEnabled(True)
    except:

        for i in range(len(filmIDLater)):
            bttn = (dict2.get(int(i) + 1))
           # b=cache(filmID[i])
            k = 1
            filminxed = str(filmIDLater[i])
            filminxed2 = str(filmIDLater[i])
            x = (alldata[int(filminxed) - 1].id)
            while alldata[int(filminxed) - k].id != int(filminxed2):
                k += 1
            label = labelDict.get(int(i) + 1)
            binary_data = base64.b64decode(alldata[int(filminxed) - k].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[int(filminxed) - k].name)
            bttn.setEnabled(True)
        for i in range(len(filmIDLater), 18):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)

            bttn.setIconSize(QSize(0, 0))
            label.setText('')
            bttn.setEnabled(False)
    end_start1 = time.time()
    print("открытие вкладки позже " + str(end_start1 - time_start1))
def histroyPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6, admin_button, moder_button, allbutton,userid,currentPage,next_button):
    time_start1 = time.time()
    global filmIDHistory
    stackedWidget.setCurrentIndex(4)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_pressed)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    moder_button.setStyleSheet(StyleSheetForButtons.moder_default)
    admin_button.setStyleSheet(StyleSheetForButtons.admin_default)
    currentPage.setText('1')
    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
    userid1 = re.sub("[^0-9]", "", userid.text())
    filmIDHistory = getUsersWatchedFilms(userid1)
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
            k = 1
            filminxed = str(filmIDHistory[i])
            filminxed2 = str(filmIDHistory[i])
            x = (alldata[int(filminxed) - 1].id)
            while alldata[int(filminxed) - k].id != int(filminxed2):
                k += 1
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
           # b=cache(filmID[i])
            binary_data = base64.b64decode(alldata[int(filminxed) - k].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[int(filminxed) - k].name)
            bttn.setEnabled(True)
    except:

        for i in range(len(filmIDHistory)):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)
            k = 1
            filminxed = str(filmIDHistory[i])
            filminxed2 = str(filmIDHistory[i])
            x = (alldata[int(filminxed) - 1].id)
            while alldata[int(filminxed) - k].id != int(filminxed2):
                k += 1
            binary_data = base64.b64decode(alldata[int(filminxed) - k].images)
            #b=cache(filmID[i])
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(alldata[int(filminxed) - k].name)
            bttn.setEnabled(True)
        for i in range(len(filmIDHistory), 18):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)

            bttn.setIconSize(QSize(0, 0))
            label.setText('')
            bttn.setEnabled(False)
    end_start1 = time.time()
    print("открытие вкладки история " + str(end_start1 - time_start1))
def settingsPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6, admin_button, moder_button, username,email,id,setuser,setid):
    time_start1 = time.time()
    k=getDataUser([setuser.text()])
    stackedWidget.setCurrentIndex(6)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_pressed)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    moder_button.setStyleSheet(StyleSheetForButtons.moder_default)
    admin_button.setStyleSheet(StyleSheetForButtons.admin_default)
    username.setText(str(k[1]))
    id.setText(str(k[0]))
    email.setText(str(k[2]))
    end_start1 = time.time()
    print("открытие вкладки настройки " + str(end_start1 - time_start1))

def collectInfoForAutoCompleter(film):
    list_of_films = []
    for i in range(len(alldata)):
        list_of_films.append(alldata[i].name)
    completer = QCompleter(list_of_films, film)
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    film.setCompleter(completer)

def filter_on(pushButton_6,stackedWidget,actorSearch,country,language,runtime,film,filter):

    time_start1 = time.time()
    pushButton_6.setIcon(QIcon(('arrow-up')))
    actorSearch.setText('')
    country.setText('')
    language.setText('')
    film.setText('')
    checkbox = filter.findChildren(QCheckBox)
    for i in range(len(checkbox)):
        checkbox[i].setChecked(False)

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

    end_start1 = time.time()
    print("открытие вкладки поиск " + str(end_start1 - time_start1))


def filter_off(pushButton_6,stackedWidget):
    global index

    stackedWidget.setCurrentIndex(index)
    pushButton_6.setIcon(QIcon(('arrow-down')))



def IsPressSearchButton(pushButton_6,stackedWidget,actorSearch,country,language,runtime,film,filter):

    pushButton_6.setCheckable(True)
    pushButton_6.toggle()

    if pushButton_6.isChecked():
        if stackedWidget.currentIndex() != 5 and stackedWidget.currentIndex() != 2:

            filter_on(pushButton_6,stackedWidget,actorSearch,country,language,runtime,film,filter)

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
        filminxed2 = str(int(id) + (int(current_page.text()) - 1) * 18)
        x=(alldata[int(filminxed)-1].id)
        while alldata[int(filminxed)-1].id != int(filminxed2):

            filminxed2=str(int(filminxed2)+1)
        filmid=0
        pop=False

        while pop==False:
            try:

                    a =cache(filminxed2)
                    pop=True
                    filmid=filminxed2

            except:

                pass
        start_time=time.time()
        favfilm = getUsersFavoriteFilms(userid1)
        latfilm = getUsersWatchLaterFilms(userid1)
        hisfilm = getUsersWatchedFilms(userid1)
        end_time=time.time()
        print('сбор инфы по поводу того является ли фильм где либо в любимом и так далее(входит в состав времени инфы о фильме): '+str(end_time-start_time))
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


        if int(filmid) in favfilm:
            favorite.setStyleSheet('background-color: #696d6d')
        elif int(filmid) in latfilm:
            lat.setStyleSheet('background-color: #696d6d')
        elif int(filmid) in hisfilm:
            his.setStyleSheet('background-color: #696d6d')

    except:
        pass

def aboutFilmFromNotHome(stackedWidget, button_name,Name_of_film, Overview_text,date_country_genres_runtime,image, actors,score, current_page_home,favorite,userid,lat,his,frame,current_page,idFilmFromHome,frameForFilter,actor,language,country,run,date_from,date_to,name):

        userid1 = re.sub("[^0-9]", "", userid.text())
        id =re.sub("[^0-9]", "", button_name)
        page=int(current_page.text())-1



        filmId=0
        start_time=time.time()

        if frame.objectName() =='frame_where_all_films_favorite':
            filmsID = getUsersFavoriteFilms(userid1)

            filmId = filmsID[int(id)-1+page*18]
            b = cache(filmId)
        elif frame.objectName() =='frame_where_all_films_watch_later':
            filmsID = getUsersWatchLaterFilms(userid1)
            filmId = filmsID[int(id)-1+page*18]
            b = cache(filmId)
        elif frame.objectName() =='frame_where_all_films_history_page':
            filmsID = getUsersWatchedFilms(userid1)
            filmId = filmsID[int(id)-1+page*18]
            b = cache(filmId)
        else:
            try:
                if actor.text() != '':
                    filmsID = getListAllFilmsWithPeopleUser(actor.text())
                elif int(date_from.text()) != 1800 and int(date_to.text()) != 1800:
                    filmsID = getAllDataFilmByReleaseDataBetween(str(date_from.text()), str(date_to.text()))
                elif language.text() != '':
                    filmsID = getAllDataFilmByLanguage(language.text())
                elif country.text() != '':
                    filmsID = getAllDataFilmByCountry(country.text())
                elif name.text()!='':
                    filmsID=getFilmByFilmname(name.text())
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

                filmsID= getListAllFilmWithGenresUser(genersList)

            except:
                pass
            filmId = int(filmsID[int(id) - 1 + page * 18].id)
            b = cache(filmId)
        end_time = time.time()
        print("сбор фльмов изходя из того где они находяться (любимое , история ,позже или поиск): " + str(end_time - start_time))
        idFilmFromHome.setText(str(filmId))
        idFilmFromHome.setStyleSheet('color:rgb(42, 54, 63)')


        global index
        index = stackedWidget.currentIndex()
        try:
            actors.setText(str(b.actors).replace(';',', '))
        except:
            pop =False
            while pop==False:
                for i in range(100):
                    try:
                        actors.setText(str(b.actors).replace(';', ', '))
                        filmId=filmId-i
                        pop=True
                        break
                    except:
                        pop = False
            filmId+=1
            pop = True
        binary_data = base64.b64decode(b.images)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(binary_data)
        score.setText(str(str(b.score)))
        image.setScaledContents(True)
        image.setPixmap((pixmap))
        Name_of_film.setText(str(b.name)+' '+'('+str(b.release)+')')
        without_brackets = re.sub(r"[\(\)]", "", str(Name_of_film.text()))



        Overview_text.setText(str((b.description)))
        date_country_genres_runtime.setText(str((b.country)).replace(';','')+"("+str(b.lang).replace(';','')+")"+" | "+str(b.genres).replace(';',', ')+" | "+str(b.runtime)+" min ")
        stackedWidget.setCurrentIndex(2)
        favorite.setStyleSheet('background-color: rgb(42, 54, 63)')
        lat.setStyleSheet('background-color: rgb(42, 54, 63)')
        his.setStyleSheet('background-color: rgb(42, 54, 63)')
        if filmId in filmsID:
            favorite.setStyleSheet('background-color: #696d6d')

        elif filmId in filmsID:
            lat.setStyleSheet('background-color: #696d6d')
        elif filmId in filmsID:
            his.setStyleSheet('background-color: #696d6d')

def adminPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6,admin_button, moder_button):
    stackedWidget.setCurrentIndex(8)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    moder_button.setStyleSheet(StyleSheetForButtons.moder_default)
    admin_button.setStyleSheet(StyleSheetForButtons.admin_pressed)

def moderPage(stackedWidget,home_button,favorite_button,histor_button,settings_button,watch_later_button,pushButton_6, admin_button, moder_button):
    stackedWidget.setCurrentIndex(9)
    home_button.setStyleSheet(StyleSheetForButtons.home_default)
    favorite_button.setStyleSheet(StyleSheetForButtons.favorite_default)
    histor_button.setStyleSheet(StyleSheetForButtons.history_default)
    settings_button.setStyleSheet(StyleSheetForButtons.settings_default)
    watch_later_button.setStyleSheet(StyleSheetForButtons.later_default)
    pushButton_6.setIcon(QIcon(('arrow-down')))
    moder_button.setStyleSheet(StyleSheetForButtons.moder_pressed)
    admin_button.setStyleSheet(StyleSheetForButtons.admin_default)


def backFromAbout(stackedWidget):
    global index
    stackedWidget.setCurrentIndex(index)