from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox, QCompleter, QListWidgetItem , QLabel
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import re
import StyleSheetForButtons
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
from collections import OrderedDict

def addFavorite(name,fav):
    fav.setStyleSheet('background-color: #696d6d')
    without_brackets =re.sub(r"[\(\)]","", str(name.text()))
    print(without_brackets[:-4])
    a=getFilmID(str(without_brackets[:-4]),str(without_brackets[-4:]))

def addLater(name,later):
    later.setStyleSheet('background-color: #696d6d')
    without_brackets = re.sub(r"[\(\)]", "", str(name.text()))
    print(without_brackets[:-4])
    a = getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:]))

def addwatched(name,his):
    his.setStyleSheet('background-color: #696d6d')
    without_brackets = re.sub(r"[\(\)]", "", str(name.text()))
    print(without_brackets[:-4])
    a = getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:]))


