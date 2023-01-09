
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
from LogicApplication.getAndSetDataFilmStatusUser import *
from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt ,QSize
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton ,QLabel , QCheckBox
from math import ceil
a = getListAllDataAllFilms()


def next_page_home(current_page_home,all_button_name,next_button):
    if current_page_home.text() != str(ceil(len(a)/18)):

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


def next(current_page,all_button_name,next_button,userid):
    stranica = int(current_page.text()) + 1
    curr = stranica - 1
    current_page.setText(str(stranica))

    userid1 = re.sub("[^0-9]", "", userid.text())
    if current_page.objectName()=='current_page_favorite':
        filmID = getUsersFavoriteFilms(userid1)
    elif current_page.objectName()=='current_page_history':
        filmID = getUsersWatchedFilms(userid1)
    elif current_page.objectName()=='current_page_watch_later':
        filmID = getUsersWatchLaterFilms(userid1)
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

        for i in range(curr * 18, curr * 18 + 18):
            if len(filmID) >=(curr + 1) * 18:
                pop = False

                bttn = (dict2.get(int(i) % 18 + 1))

                label = labelDict.get(int(i) % 18 + 1)
                while pop == False:
                    try:
                        binary_data = base64.b64decode(a[filmID[i] - 1].images)
                        label.setText(a[filmID[i] - 1].name)
                        pop = True
                        continue
                    except:
                        for j in range(100):
                            try:
                                binary_data = base64.b64decode(a[filmID[i] - j].images)
                                label.setText(a[filmID[i] - j].name)
                                pop = True
                                break
                            except:
                                pop = False

                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(binary_data)
                bttn.setIconSize(QSize(100, 140))
                bttn.setIcon(QIcon(pixmap))
                print(len(filmID),(curr+1)*18)


            else:


                for i in range(curr * 18, len(filmID)):
                    pop = False
                    bttn = (dict2.get(int(i) % 18 + 1))

                    label = labelDict.get(int(i) % 18 + 1)
                    while pop == False:
                        try:
                            binary_data = base64.b64decode(a[filmID[i] - 1].images)
                            label.setText(a[filmID[i] - 1].name)
                            pop = True

                            continue
                        except:
                            for j in range(100):
                                try:
                                    binary_data = base64.b64decode(a[filmID[i] - j].images)
                                    label.setText(a[filmID[i] - j].name)

                                    pop = True
                                    break
                                except:
                                    pop = False

                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(binary_data)
                    bttn.setIconSize(QSize(100, 140))
                    bttn.setIcon(QIcon(pixmap))

                    bttn.setEnabled(True)
                next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)

                if filmID[i] == filmID[-1]:
                    for j in range(len(filmID) % 18, 18):
                        bttn = (dict2.get(int(j) + 1))
                        print(j)
                        label = labelDict.get(int(j) + 1)
                        bttn.setIconSize(QSize(0, 0))
                        label.setText('')
                        bttn.setEnabled(False)


    except:
        current_page.setText(str(stranica-1))
        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        pass

def back(current_page,all_button_name,next_button,userid):
    stranica = int(current_page.text()) - 1
    curr = stranica - 1
    current_page.setText(str(stranica))

    userid1 = re.sub("[^0-9]", "", userid.text())
    if current_page.objectName() == 'current_page_favorite':
        filmID = getUsersFavoriteFilms(userid1)


    elif current_page.objectName() == 'current_page_history':
        filmID = getUsersWatchedFilms(userid1)
    elif current_page.objectName() == 'current_page_watch_later':
        filmID = getUsersWatchLaterFilms(userid1)
    button = all_button_name.findChildren(QPushButton)
    labels = all_button_name.findChildren(QLabel)
    print(button)
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

            bttn = (dict2.get(int(i) % 18 + 1))

            label = labelDict.get(int(i) % 18 + 1)
            pop = False
            while pop == False:
                try:
                    binary_data = base64.b64decode(a[filmID[i] - 1].images)
                    label.setText(a[filmID[i] - 1].name)
                    pop = True

                    continue
                except:
                    for j in range(100):
                        try:
                            binary_data = base64.b64decode(a[filmID[i] - j].images)
                            label.setText(a[filmID[i] - j].name)

                            pop = True
                            break
                        except:
                            pop = False

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))

            bttn.setEnabled(True)

        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
    #
    except:
        pass
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





def next_page_search(current_page_search,all_button_name,next_button,actor,language,country,run,date_from,date_to,filter):
    if current_page_search.text() != 'last':
            try:
                if actor.text() != '':
                    b = getListAllFilmsWithPeopleUser(actor.text())
                elif int(date_from.text()) != 2000 and int(date_to.text()) != 2000:

                    b = getAllDataFilmByReleaseDataBetween(str(date_from.text()), str(date_to.text()))

                elif language.text() != '':
                    b = getAllDataFilmByLanguage(language.text())
                elif country.text() != '':
                    b = getAllDataFilmByCountry(country.text())

                else:
                    genersList = []
                    checkbox = filter.findChildren(QCheckBox)

                    for i in range(len(checkbox)):
                        print(checkbox[i].objectName())
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
                    b = getListAllFilmWithGenresUser(genersList)
            except:
                pass



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
                            print(j)
                            label = labelDict.get(int(j) + 1)
                            bttn.setIconSize(QSize(0, 0))
                            label.setText('')
                            bttn.setEnabled(False)
                        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)

            except:
                pass
def back_page_search(current_page_search,all_button_name,next_button,actor,language,country,run,date_from,date_to,filter):
    if current_page_search.text() != '1':
            try:
                if actor.text() != '':
                    b = getListAllFilmsWithPeopleUser(actor.text())
                elif int(date_from.text()) != 2000 and int(date_to.text()) != 2000:

                    b = getAllDataFilmByReleaseDataBetween(str(date_from.text()), str(date_to.text()))

                elif language.text() != '':
                    b = getAllDataFilmByLanguage(language.text())
                elif country.text() != '':
                    b = getAllDataFilmByCountry(country.text())

                else:
                    genersList = []
                    checkbox = filter.findChildren(QCheckBox)

                    for i in range(len(checkbox)):
                        print(checkbox[i].objectName())
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
                    b = getListAllFilmWithGenresUser(genersList)
            except:
                pass



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
                        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
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
                    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)

                    if b[i] == b[-1]:
                        for j in range(len(b) % 18, 18):
                            bttn = (dict2.get(int(j) + 1))
                            print(j)
                            label = labelDict.get(int(j) + 1)
                            bttn.setIconSize(QSize(0, 0))
                            label.setText('')
                            bttn.setEnabled(True)
                        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)

            except:
                pass