from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton,  QLabel, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import time
from LogicApplication.userDataValidation import *

from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *



def searchFilm(actors,language,country,runtime,date_from,date_to,filter,stackedWidget,buttonsAndLabel,film):
    global aad

    start_time = time.time()
    try:
        if actors.text() !='':

            aad= getListAllFilmsWithPeopleUser(actors.text())
        elif int(date_from.text()) !=1800 and int(date_to.text())!=1800:

            aad = getAllDataFilmByReleaseDataBetween(str(date_from.text()),str(date_to.text()))

        elif language.text()!= '':

            aad = getAllDataFilmByLanguage(language.text())
        elif country.text() !='':

            aad = getAllDataFilmByCountry(country.text())
        elif film.text()!='':
            aad=getAllDataFilmByCountry('Japan')
        else:
            genersList = []
            checkbox = filter.findChildren(QCheckBox)

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

            aad = getListAllFilmWithGenresUser(genersList)

        end_time = time.time()
        print('время сбора данных для поиска:'+str(end_time-start_time))
        button = buttonsAndLabel.findChildren(QPushButton)
        labels = buttonsAndLabel.findChildren(QLabel)
        stackedWidget.setCurrentIndex(7)
        dict2={}
        labelDict={}
        for i in range(18):
            bttn_number = re.sub("[^0-9]", "", button[i].objectName())
            label_number = re.sub("[^0-9]", "", labels[i].objectName())
            dict2[int(bttn_number)]=button[i]
            labelDict[int(label_number)]=labels[i]
        dict2=dict(sorted(dict2.items()))
        labelDict=dict(sorted(labelDict.items()))

        try:
            for i in range(18):
                bttn=(dict2.get(int(i)+1))
                label=labelDict.get(int(i)+1)
                binary_data = base64.b64decode(aad[i].images)

                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(binary_data)
                bttn.setIconSize(QSize(100, 140))
                bttn.setIcon(QIcon(pixmap))
                label.setText(aad[i].name)
                bttn.setEnabled(True)
        except:

            for i in range(len(a)):
                bttn=(dict2.get(int(i)+1))
                label=labelDict.get(int(i)+1)
                binary_data = base64.b64decode(aad[i].images)

                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(binary_data)
                bttn.setIconSize(QSize(100, 140))
                bttn.setIcon(QIcon(pixmap))
                label.setText(aad[i].name)
                bttn.setEnabled(True)
            for i in range(len(aad),18):
                bttn = (dict2.get(int(i) + 1))
                label = labelDict.get(int(i) + 1)

                label.setText('')
                bttn.setIconSize(QSize(0, 0))
                bttn.setEnabled(False)

    except:
        pass


