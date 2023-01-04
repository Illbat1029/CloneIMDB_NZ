from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox, QCompleter, QListWidgetItem
from PyQt5.QtGui import QIcon
from LogicApplication.getAndSetScoreFilms import *
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
def setScoreFromDataBase(user,score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name):

    dataUserId = getDataUser([user.text()])
    without_brackets = re.sub(r"[\(\)]", "", str(name.text()))
    a = selectScoreFromDB(dataUserId[0], getFilmID(str(without_brackets[:-4]),str(without_brackets[-4:])))
    a = str(a)
    a = a.replace('(', '')
    a = a.replace(')', '')
    a = a.replace(',', '')
    a = a.replace('[', '')
    a = a.replace(']', '')
    print(a)

    if a=='1':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    elif a=='2':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    elif a=='3':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_3_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    elif a=='4':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_3_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_4_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    elif a=='5':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_3_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_4_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_5_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    elif a=='':
        score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        score_1_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_2_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_3_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_4_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_5_button.setIcon(QIcon(('star-empty-icon.webp')))



def swap_star_and_get_score1_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year,user,name):
    dataUserId = getDataUser([user.text()])
    without_brackets = re.sub(r"[\(\)]", "", str(name.text()))
    a = selectScoreFromDB(dataUserId[0], getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:])))
    a = str(a)
    a = a.replace('(', '')
    a = a.replace(')', '')
    a = a.replace(',', '')
    a = a.replace('[', '')
    a = a.replace(']', '')
    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
    score = 1
    score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    a=addVotesAndScoreUser()



def swap_star_and_get_score2_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year):
    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
    score = 2
    score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)


def swap_star_and_get_score3_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year):
    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_3_button.setIcon(QIcon(('icons8-star-filled-48')))
    score = 3
    score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)


def swap_star_and_get_score4_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year):
    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_3_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_4_button.setIcon(QIcon(('icons8-star-filled-48')))
    score = 4
    score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)


def swap_star_and_get_score5_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year):
    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_3_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_4_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_5_button.setIcon(QIcon(('icons8-star-filled-48')))
    score = 5
    score_1_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_2_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_3_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    score_4_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    Mscore_5_button.setAttribute(Qt.WA_TransparentForMouseEvents, True)