
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
from LogicApplication.getAndSetDataFilmStatusUser import *
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
def next_page_favorite(current_page_favorite,all_button_name,next_button,userid):
    if current_page_favorite.text() != 'last':

        stranica = int(current_page_favorite.text()) + 1
        curr = stranica - 1
        current_page_favorite.setText(str(stranica))


        userid1 = re.sub("[^0-9]", "", userid.text())
        filmID = getUsersFavoriteFilms(userid1)
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
        print(len(filmID))
        labelDict = dict(sorted(labelDict.items()))
        try:
            try:
                for i in range(curr*18,curr*18+18):

                    bttn = (dict2.get(int(i)%18 + 1))

                    label = labelDict.get(int(i)%18 + 1)
                    binary_data = base64.b64decode(a[filmID[i] - 1].images)

                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(binary_data)
                    bttn.setIconSize(QSize(100, 140))
                    bttn.setIcon(QIcon(pixmap))
                    label.setText(a[filmID[i] - 1].name)
            except:
                for i in range(curr * 18,len(filmID)):
                    bttn = (dict2.get(int(i) % 18 + 1))

                    label = labelDict.get(int(i) % 18 + 1)
                    binary_data = base64.b64decode(a[filmID[i] - 1].images)

                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(binary_data)
                    bttn.setIconSize(QSize(100, 140))
                    bttn.setIcon(QIcon(pixmap))
                    label.setText(a[filmID[i] - 1].name)

                bttn.setEnabled(True)
                next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
                current_page_favorite.setText(str(stranica-1))
                if filmID[i] == filmID[-1]:
                    for j in range(len(filmID)%18,18):
                        bttn = (dict2.get(int(j)  + 1))
                        print(j)
                        label = labelDict.get(int(j)  + 1)
                        bttn.setIconSize(QSize(0, 0))
                        label.setText('')
                        bttn.setEnabled(False)


        except:
            pass


def back_page_favorite(current_page_favorite,all_button_name,next_button,userid):
    if current_page_favorite.text() != '1':
        stranica = int(current_page_favorite.text()) - 1
        curr = stranica - 1
        current_page_favorite.setText(str(stranica))

        userid1 = re.sub("[^0-9]", "", userid.text())
        filmID = getUsersFavoriteFilms(userid1)
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
            for i in range(curr * 18,curr * 18+18 ):

                bttn = (dict2.get(int(i) % 18 + 1))

                label = labelDict.get(int(i) % 18 + 1)
                binary_data = base64.b64decode(a[filmID[i] - 1].images)

                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(binary_data)
                bttn.setIconSize(QSize(100, 140))
                bttn.setIcon(QIcon(pixmap))
                label.setText(a[filmID[i] - 1].name)
                bttn.setEnabled(True)

            next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        #
        except:
            pass


def next_page_later(current_page_watch_later,all_button_name,next_button,userid):
    if current_page_watch_later.text() != 'last':
        userid1 = re.sub("[^0-9]", "", userid.text())
        filmID = getUsersWatchLaterFilms(userid1)
        if len(filmID) >18:

            stranica = int(current_page_watch_later.text()) + 1
            curr = stranica - 1
            current_page_watch_later.setText(str(stranica))



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
            print(len(filmID))
            labelDict = dict(sorted(labelDict.items()))
            try:
                try:
                    for i in range(curr * 18, curr * 18 + 18):
                        bttn = (dict2.get(int(i) % 18 + 1))

                        label = labelDict.get(int(i) % 18 + 1)
                        binary_data = base64.b64decode(a[filmID[i] - 1].images)

                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(binary_data)
                        bttn.setIconSize(QSize(100, 140))
                        bttn.setIcon(QIcon(pixmap))
                        label.setText(a[filmID[i] - 1].name)
                except:
                    for i in range(curr * 18, len(filmID)):
                        bttn = (dict2.get(int(i) % 18 + 1))

                        label = labelDict.get(int(i) % 18 + 1)
                        binary_data = base64.b64decode(a[filmID[i] - 1].images)

                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(binary_data)
                        bttn.setIconSize(QSize(100, 140))
                        bttn.setIcon(QIcon(pixmap))
                        label.setText(a[filmID[i] - 1].name)

                    bttn.setEnabled(True)
                    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
                    current_page_watch_later.setText(str(stranica - 1))
                    if filmID[i] == filmID[-1]:
                        for j in range(len(filmID) % 18, 18):
                            bttn = (dict2.get(int(j) + 1))
                            print(j)
                            label = labelDict.get(int(j) + 1)
                            bttn.setIconSize(QSize(0, 0))
                            label.setText('')
                            bttn.setEnabled(False)
                        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)

            except:
                pass


def back_page_later(current_page_watch_later,all_button_name,next_button,userid):
    if current_page_watch_later.text() != '1':
        stranica = int(current_page_watch_later.text()) - 1
        curr = stranica - 1
        current_page_watch_later.setText(str(stranica))

        userid1 = re.sub("[^0-9]", "", userid.text())
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
                binary_data = base64.b64decode(a[filmID[i] - 1].images)

                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(binary_data)
                bttn.setIconSize(QSize(100, 140))
                bttn.setIcon(QIcon(pixmap))
                label.setText(a[filmID[i] - 1].name)
                bttn.setEnabled(True)

            next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        #
        except:
            pass


def next_page_history(current_page_history,all_button_name,next_button,userid):
    if current_page_history.text() != 'last':
        userid1 = re.sub("[^0-9]", "", userid.text())
        filmID = getUsersWatchedFilms(userid1)
        if len(filmID) > 18:

            stranica = int(current_page_history.text()) + 1
            curr = stranica - 1
            current_page_history.setText(str(stranica))

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
            print(len(filmID))
            labelDict = dict(sorted(labelDict.items()))
            try:
                try:
                    for i in range(curr * 18, curr * 18 + 18):
                        bttn = (dict2.get(int(i) % 18 + 1))

                        label = labelDict.get(int(i) % 18 + 1)
                        binary_data = base64.b64decode(a[filmID[i] - 1].images)

                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(binary_data)
                        bttn.setIconSize(QSize(100, 140))
                        bttn.setIcon(QIcon(pixmap))
                        label.setText(a[filmID[i] - 1].name)
                except:
                    for i in range(curr * 18, len(filmID)):
                        bttn = (dict2.get(int(i) % 18 + 1))

                        label = labelDict.get(int(i) % 18 + 1)
                        binary_data = base64.b64decode(a[filmID[i] - 1].images)

                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(binary_data)
                        bttn.setIconSize(QSize(100, 140))
                        bttn.setIcon(QIcon(pixmap))
                        label.setText(a[filmID[i] - 1].name)

                    bttn.setEnabled(True)
                    next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
                    current_page_history.setText(str(stranica - 1))
                    if filmID[i] == filmID[-1]:
                        for j in range(len(filmID) % 18, 18):
                            bttn = (dict2.get(int(j) + 1))
                            print(j)
                            label = labelDict.get(int(j) + 1)
                            bttn.setIconSize(QSize(0, 0))
                            label.setText('')
                            bttn.setEnabled(False)
                        next_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)

            except:
                pass


def back_page_history(current_page_history,all_button_name,next_button,userid):
    if current_page_history.text() != '1':
        stranica = int(current_page_history.text()) - 1
        curr = stranica - 1
        current_page_history.setText(str(stranica))

        userid1 = re.sub("[^0-9]", "", userid.text())
        filmID = getUsersWatchedFilms(userid1)
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
                binary_data = base64.b64decode(a[filmID[i] - 1].images)

                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(binary_data)
                bttn.setIconSize(QSize(100, 140))
                bttn.setIcon(QIcon(pixmap))
                label.setText(a[filmID[i] - 1].name)
                bttn.setEnabled(True)

            next_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        #
        except:
            pass
