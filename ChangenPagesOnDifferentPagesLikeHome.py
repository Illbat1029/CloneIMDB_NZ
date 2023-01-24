
from LogicApplication.userDataValidation import *
from functools import cache
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
from LogicApplication.getAndSetDataFilmStatusUser import *
from PyQt5.QtCore import  Qt ,QSize
from PyQt5 import QtGui
from functools import lru_cache
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton ,QLabel , QCheckBox
from math import ceil
from SwapPagesMainMenuFunctions import alldata
import time
from SearchFilmByGenresNameIDT import *
import SearchFilmByGenresNameIDT
import SwapPagesMainMenuFunctions
@lru_cache()
def cache(id):
    return getAllDataFilmByID(id)
def next_page_home(current_page_home,all_button_name,next_button):
    if current_page_home.text() != str(ceil(len(alldata)/18)):

            stranica = int(current_page_home.text()) + 1
            current_page_home.setText(str(stranica))

            button=all_button_name.findChildren(QPushButton)
            labels = all_button_name.findChildren(QLabel)


            for i in range(18):
                bttn_number=re.sub("[^0-9]", "", button[i].objectName())
                label_number = re.sub("[^0-9]", "", labels[i].objectName())
                try:
                    binary_data = base64.b64decode(alldata[(int(bttn_number)-1)+18*(stranica-1)].images)
                    labels[i].setText(alldata[(int(bttn_number)-1)+18*(stranica-1)].name)
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


        stranica = int(current_page_home.text())

        current_page_home.setText(str(stranica - 1))
        button = all_button_name.findChildren(QPushButton)
        labels = all_button_name.findChildren(QLabel)
        for i in range(18):
            bttn_number = re.sub("[^0-9]", "", button[i].objectName())
            label_number = re.sub("[^0-9]", "", labels[i].objectName())
            binary_data = base64.b64decode(alldata[(stranica-2)*18+int(bttn_number)-1].images)
            labels[i].setText(alldata[(stranica-2)*18+int(bttn_number)-1].name)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            button[i].setIconSize(QSize(100, 140))
            button[i].setIcon(QIcon(pixmap))


def next(current_page,all_button_name,next_button,userid):
    start_time=time.time()
    stranica = int(current_page.text()) + 1
    curr = stranica - 1
    current_page.setText(str(stranica))

    userid1 = re.sub("[^0-9]", "", userid.text())
    if current_page.objectName()=='current_page_favorite':
        filmID=SwapPagesMainMenuFunctions.filmIDFavorite
    elif current_page.objectName()=='current_page_history':
        filmID = SwapPagesMainMenuFunctions.filmIDHistory
    elif current_page.objectName()=='current_page_watch_later':
        filmID = SwapPagesMainMenuFunctions.filmIDLater
    button = all_button_name.findChildren(QPushButton)
    labels = all_button_name.findChildren(QLabel)

    dict2 = {}
    buf = 0

    labelDict = {}
    for i in range(18):
        bttn_number = re.sub("[^0-9]", "", button[i].objectName())
        label_number = re.sub("[^0-9]", "", labels[i].objectName())
        dict2[int(bttn_number)] = button[i]
        labelDict[int(label_number)] = labels[i]
    dict2 = dict(sorted(dict2.items()))

    labelDict = dict(sorted(labelDict.items()))
    try:
        if len(filmID) >= (curr + 1) * 18:
            for i in range(curr * 18, curr * 18 + 18):
                k = 1
                filminxed = str(filmID[i])
                filminxed2 = str(filmID[i])
                #x = (alldata[int(filminxed) - 1].id)
                buf=False
                while buf==False:
                    try:
                        while alldata[int(filminxed) - k].id != int(filminxed2):
                            k += 1
                        buf=True
                    except:
                        k += 1
                        buf=False


                bttn = (dict2.get(int(i) % 18 + 1))

                label = labelDict.get(int(i) % 18 + 1)


                binary_data = base64.b64decode(alldata[int(filminxed) - k].images)
                label.setText(alldata[int(filminxed) - k].name)


                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(binary_data)
                bttn.setIconSize(QSize(100, 140))
                bttn.setIcon(QIcon(pixmap))

        else:
                for i in range(curr * 18, len(filmID)):

                    bttn = (dict2.get(int(i) % 18 + 1))
                    k = 1
                    filminxed = str(filmID[i])
                    filminxed2 = str(filmID[i])
                    buf = False
                    while buf == False:
                        try:
                            while alldata[int(filminxed) - k].id != int(filminxed2):
                                k += 1
                            buf = True
                        except:
                            k += 1
                            buf = False


                    label = labelDict.get(int(i) % 18 + 1)

                    binary_data = base64.b64decode(alldata[int(filminxed) - k].images)
                    label.setText(alldata[int(filminxed) - k].name)



                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(binary_data)
                    bttn.setIconSize(QSize(100, 140))
                    bttn.setIcon(QIcon(pixmap))
                    bttn.setEnabled(True)
                next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
                if filmID[i] == filmID[-1] and len(filmID)!=18:
                    for j in range(len(filmID) % 18, 18):
                        bttn = (dict2.get(int(j) + 1))

                        label = labelDict.get(int(j) + 1)
                        bttn.setIconSize(QSize(0, 0))
                        label.setText('')
                        bttn.setEnabled(False)
                else:
                    current_page.setText(str(stranica-1))
    except:
        current_page.setText(str(stranica-1))
        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        pass
    end_time = time.time()
    #print('Время переключение страниц вперед:'+str(end_time-start_time))

def back(current_page,all_button_name,next_button,userid):
    start_time = time.time()
    stranica = int(current_page.text()) - 1
    curr = stranica - 1
    current_page.setText(str(stranica))
    userid1 = re.sub("[^0-9]", "", userid.text())
    if current_page.objectName() == 'current_page_favorite':
        filmID = SwapPagesMainMenuFunctions.filmIDFavorite
    elif current_page.objectName() == 'current_page_history':
        filmID = SwapPagesMainMenuFunctions.filmIDHistory
    elif current_page.objectName() == 'current_page_watch_later':
        filmID = SwapPagesMainMenuFunctions.filmIDLater
    button = all_button_name.findChildren(QPushButton)
    labels = all_button_name.findChildren(QLabel)

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
        for i in range(curr * 18, curr * 18 + 18):
            k = 1
            filminxed = str(filmID[i])
            filminxed2 = str(filmID[i])
            buf = False
            while buf == False:
                try:
                    while alldata[int(filminxed) - k].id != int(filminxed2):
                        k += 1
                    buf = True
                except:
                    k += 1
                    buf = False
            bttn = (dict2.get(int(i) % 18 + 1))

            label = labelDict.get(int(i) % 18 + 1)
           # b = cache(filmID[i])

            binary_data = base64.b64decode(alldata[int(filminxed) - k].images)
            label.setText(alldata[int(filminxed) - k].name)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            bttn.setEnabled(True)
        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
    except:
        pass
    end_time = time.time()
    #print('Время переключение страниц вперед:' + str(end_time - start_time))
# переключает след старницу в разедле фаворит
def next_page_favorite(current_page_favorite,all_button_name,next_button,userid):
    if current_page_favorite.text() != 'last':

        next(current_page_favorite,all_button_name,next_button,userid)



def back_page_favorite(current_page_favorite,all_button_name,next_button,userid):
    if current_page_favorite.text() != '1':
        back(current_page_favorite,all_button_name,next_button,userid)


def next_page_later(current_page_watch_later,all_button_name,next_button,userid):
    if current_page_watch_later.text() != 'last':
        next(current_page_watch_later,all_button_name,next_button,userid)


def back_page_later(current_page_watch_later,all_button_name,next_button,userid):
    if current_page_watch_later.text() != '1':
        back(current_page_watch_later, all_button_name, next_button, userid)


def next_page_history(current_page_history,all_button_name,next_button,userid):
    if current_page_history.text() != 'last':
        next(current_page_history,all_button_name,next_button,userid)


def back_page_history(current_page_history,all_button_name,next_button,userid):
    if current_page_history.text() != '1':
        back(current_page_history, all_button_name, next_button, userid)





def next_page_search(current_page_search,all_button_name,next_button,actor,language,country,run,date_from,date_to,filter,film):
    b=SearchFilmByGenresNameIDT.aad
    if current_page_search.text() != 'last':
           # try:

               # if actor.text() != '':
                  #  b = getListAllFilmsWithPeopleUser(actor.text())
               # elif int(date_from.text()) != 1800 and int(date_to.text()) != 1800:

                  #  b = getAllDataFilmByReleaseDataBetween(str(date_from.text()), str(date_to.text()))

               # elif language.text() != '':
                #    b = getAllDataFilmByLanguage(language.text())
               # elif country.text() != '':
                #    b = getAllDataFilmByCountry(country.text())
              #  elif film.text() != '':
                #    b = getAllDataFilmByCountry('Japan')
              #  else:
                #    genersList = []
                 #   checkbox = filter.findChildren(QCheckBox)
#
                  #  for i in range(len(checkbox)):

                   #     if checkbox[i].isChecked():
                      #      if checkbox[i].objectName() == 'checkBoxGameShow':
                       #         genersList.append('Game-Show')
                       #     elif checkbox[i].objectName() == 'checkBoxRealityTV':
                        #        genersList.append('Reality-TV')
                        #    elif checkbox[i].objectName() == 'checkBoxTalkShow':
                       #         genersList.append('Talk-Show')
                        #    elif checkbox[i].objectName() == 'checkBoxFilmNoir':
                        #        genersList.append('Film-Noir')
                        #    else:
                       #         genersList.append((checkbox[i].objectName()).replace('checkBox', ''))
                    #b = getListAllFilmWithGenresUser(genersList)
            #except:
            #    pass



            stranica = int(current_page_search.text()) + 1
            curr = stranica - 1
            current_page_search.setText(str(stranica))

            button = all_button_name.findChildren(QPushButton)
            labels = all_button_name.findChildren(QLabel)

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
                try:
                    for i in range(curr * 18, curr * 18 + 18):
                        bttn = (dict2.get(int(i) % 18 + 1))

                        label = labelDict.get(int(i) % 18 + 1)
                        binary_data = base64.b64decode(b[i].images)

                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(binary_data)
                        bttn.setIconSize(QSize(100, 140))
                        bttn.setIcon(QIcon(pixmap))
                        label.setText(b[i].name)
                except:
                    for i in range(curr * 18, len(b)):
                        bttn = (dict2.get(int(i) % 18 + 1))

                        label = labelDict.get(int(i) % 18 + 1)
                        binary_data = base64.b64decode(b[i].images)

                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(binary_data)
                        bttn.setIconSize(QSize(100, 140))
                        bttn.setIcon(QIcon(pixmap))
                        label.setText(b[i].name)

                    bttn.setEnabled(True)
                    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)

                    if b[i] == b[-1]:
                        for j in range(len(b) % 18, 18):
                            bttn = (dict2.get(int(j) + 1))

                            label = labelDict.get(int(j) + 1)
                            bttn.setIconSize(QSize(0, 0))
                            label.setText('')
                            bttn.setEnabled(False)
                        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)

            except:
                current_page_search.setText(str(stranica-1))
                pass
def back_page_search(current_page_search,all_button_name,next_button,actor,language,country,run,date_from,date_to,filter,film,nxt):
    if current_page_search.text() != '1':
            b = SearchFilmByGenresNameIDT.aad
           # try:
            #    if actor.text() != '':
        #            b = getListAllFilmsWithPeopleUser(actor.text())
         #       elif int(date_from.text()) != 1800 and int(date_to.text()) != 1800:
#
            #        b = getAllDataFilmByReleaseDataBetween(str(date_from.text()), str(date_to.text()))

           #     elif language.text() != '':
              #      b = getAllDataFilmByLanguage(language.text())
             #   elif country.text() != '':
              #      b = getAllDataFilmByCountry(country.text())
              #  elif film.text() != '':
              #      b = getAllDataFilmByCountry('Japan')
             #   else:
                #    genersList = []
                #    checkbox = filter.findChildren(QCheckBox)

                  #  for i in range(len(checkbox)):

                   #     if checkbox[i].isChecked():
                   #         if checkbox[i].objectName() == 'checkBoxGameShow':
                         #       genersList.append('Game-Show')
                        #    elif checkbox[i].objectName() == 'checkBoxRealityTV':
                        #        genersList.append('Reality-TV')
                       #     elif checkbox[i].objectName() == 'checkBoxTalkShow':
                      #          genersList.append('Talk-Show')
                       ##     elif checkbox[i].objectName() == 'checkBoxFilmNoir':
                         #       genersList.append('Film-Noir')
                       #     else:
                           #     genersList.append((checkbox[i].objectName()).replace('checkBox', ''))
                 #   b = getListAllFilmWithGenresUser(genersList)
          #  except:
           #     pass
#


            stranica = int(current_page_search.text()) - 1
            curr = stranica - 1
            current_page_search.setText(str(stranica))

            button = all_button_name.findChildren(QPushButton)
            labels = all_button_name.findChildren(QLabel)

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
                try:
                    for i in range(curr * 18, curr * 18 + 18):
                        bttn = (dict2.get(int(i) % 18 + 1))

                        label = labelDict.get(int(i) % 18 + 1)
                        binary_data = base64.b64decode(b[i].images)

                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(binary_data)
                        bttn.setIconSize(QSize(100, 140))
                        bttn.setIcon(QIcon(pixmap))
                        label.setText(b[i].name)
                        bttn.setEnabled(True)

                        nxt.setAttribute(Qt.WA_TransparentForMouseEvents, False)
                except:
                    for i in range(curr * 18, len(b)):
                        bttn = (dict2.get(int(i) % 18 + 1))

                        label = labelDict.get(int(i) % 18 + 1)
                        binary_data = base64.b64decode(b[i].images)

                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(binary_data)
                        bttn.setIconSize(QSize(100, 140))
                        bttn.setIcon(QIcon(pixmap))
                        label.setText(b[i].name)

                    bttn.setEnabled(True)
                    nxt.setAttribute(Qt.WA_TransparentForMouseEvents, False)

                    if b[i] == b[-1]:
                        for j in range(len(b) % 18, 18):
                            bttn = (dict2.get(int(j) + 1))

                            label = labelDict.get(int(j) + 1)
                            bttn.setIconSize(QSize(0, 0))
                            label.setText('')
                            bttn.setEnabled(True)
                        nxt.setAttribute(Qt.WA_TransparentForMouseEvents, False)

            except:
                pass
            nxt.setAttribute(Qt.WA_TransparentForMouseEvents, False)
