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
from LogicApplication.getAndSetDataFilmStatusUser import *
from collections import OrderedDict

def addFavorite(name,fav,user):
    dataUserId = getDataUser([user.text()])
    fav.setStyleSheet('background-color: #696d6d')
    without_brackets =re.sub(r"[\(\)]","", str(name.text()))

   # a=getFilmID(str(without_brackets[:-4]),str(without_brackets[-4:]))
#  b=insertIntoFavoriteFilms(dataUserId[0],a)

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


