from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt,QSize
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox, QCompleter, QListWidgetItem , QLabel, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import re
import StyleSheetForButtons
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
import collections



def searchFilm(actors,language,country,runtime,date_from,date_to,filter,stackedWidget,buttonsAndLabel,film):
    try:
        if actors.text() !='':

            a= getListAllFilmsWithPeopleUser(actors.text())
        elif int(date_from.text()) !=2000 and int(date_to.text())!=2000:

            a = getAllDataFilmByReleaseDataBetween(str(date_from.text()),str(date_to.text()))

        elif language.text()!= '':

            a = getAllDataFilmByLanguage(language.text())
        elif country.text() !='':

            a = getAllDataFilmByCountry(country.text())
        elif film.text()!='':
            pass
            #фильмы
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

            a = getListAllFilmWithGenresUser(genersList)
    except:
        pass

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
            binary_data = base64.b64decode(a[i].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(a[i].name)
            bttn.setEnabled(True)
    except:

        for i in range(len(a)):
            bttn=(dict2.get(int(i)+1))
            label=labelDict.get(int(i)+1)
            binary_data = base64.b64decode(a[i].images)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(binary_data)
            bttn.setIconSize(QSize(100, 140))
            bttn.setIcon(QIcon(pixmap))
            label.setText(a[i].name)
            bttn.setEnabled(True)
        for i in range(len(a),18):
            bttn = (dict2.get(int(i) + 1))
            label = labelDict.get(int(i) + 1)

            label.setText('')
            bttn.setIconSize(QSize(0, 0))
            bttn.setEnabled(False)




