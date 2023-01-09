from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox, QCompleter, QListWidgetItem
from PyQt5.QtGui import QIcon
from LogicApplication.getAndSetScoreFilms import *
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
def setScoreFromDataBase(userid,score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name,idfilm):

    userid1 = re.sub("[^0-9]", "", userid.text())
    without_brackets = re.sub(r"[\(\)]", "", str(name.text()))

    a = selectScoreFromDB(userid1, idfilm.text())
    a = str(a)
    a = a.replace('(', '')
    a = a.replace(')', '')
    a = a.replace(',', '')
    a = a.replace('[', '')
    a = a.replace(']', '')
    print(a)

    if a=='1':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_2_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_3_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_4_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_5_button.setIcon(QIcon(('star-empty-icon.webp')))

    elif a=='2':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_2_button.setIcon(QIcon(('icons8-star-filled-48')))

        score_3_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_4_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_5_button.setIcon(QIcon(('star-empty-icon.webp')))
    elif a=='3':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_3_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_4_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_5_button.setIcon(QIcon(('star-empty-icon.webp')))
    elif a=='4':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_3_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_4_button.setIcon(QIcon(('icons8-star-filled-48')))

        score_5_button.setIcon(QIcon(('star-empty-icon.webp')))


    elif a=='5':
        score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_3_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_4_button.setIcon(QIcon(('icons8-star-filled-48')))
        score_5_button.setIcon(QIcon(('icons8-star-filled-48')))

    elif a=='':

        score_1_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_2_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_3_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_4_button.setIcon(QIcon(('star-empty-icon.webp')))
        score_5_button.setIcon(QIcon(('star-empty-icon.webp')))



def swap_star_and_get_score1_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year,userid):
    userid1=re.sub("[^0-9]", "", userid.text())
    without_brackets = re.sub(r"[\(\)]", "", str(name_year.text()))
    filmId =getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:]))

    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))

    score_2_button.setIcon(QIcon(('star-empty-icon.webp')))
    score_3_button.setIcon(QIcon(('star-empty-icon.webp')))
    score_4_button.setIcon(QIcon(('star-empty-icon.webp')))
    score_5_button.setIcon(QIcon(('star-empty-icon.webp')))

    score = 1
    deleteScoreUser(int(userid1),filmId)
    addVotesAndScoreUser(int(userid1),filmId,score)



def swap_star_and_get_score2_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year,userid):


    score = 2
    userid1 = re.sub("[^0-9]", "", userid.text())
    without_brackets = re.sub(r"[\(\)]", "", str(name_year.text()))
    filmId = getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:]))

    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_3_button.setIcon(QIcon(('star-empty-icon.webp')))
    score_4_button.setIcon(QIcon(('star-empty-icon.webp')))
    score_5_button.setIcon(QIcon(('star-empty-icon.webp')))


    deleteScoreUser(int(userid1), filmId)
    addVotesAndScoreUser(int(userid1), filmId, score)


def swap_star_and_get_score3_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year,userid):

    userid1 = re.sub("[^0-9]", "", userid.text())
    without_brackets = re.sub(r"[\(\)]", "", str(name_year.text()))
    filmId = getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:]))

    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_3_button.setIcon(QIcon(('icons8-star-filled-48')))

    score_4_button.setIcon(QIcon(('star-empty-icon.webp')))
    score_5_button.setIcon(QIcon(('star-empty-icon.webp')))
    score = 3


    deleteScoreUser(int(userid1), filmId)
    addVotesAndScoreUser(int(userid1), filmId, score)


def swap_star_and_get_score4_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year,userid):
    userid1 = re.sub("[^0-9]", "", userid.text())
    without_brackets = re.sub(r"[\(\)]", "", str(name_year.text()))
    filmId = getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:]))

    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_3_button.setIcon(QIcon(('icons8-star-filled-48')))

    score_4_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_5_button.setIcon(QIcon(('star-empty-icon.webp')))
    score = 4

    deleteScoreUser(int(userid1), filmId)
    addVotesAndScoreUser(int(userid1), filmId, score)



def swap_star_and_get_score5_icon(score_1_button,score_2_button,score_3_button,score_4_button,score_5_button,name_year,userid):
    userid1 = re.sub("[^0-9]", "", userid.text())
    without_brackets = re.sub(r"[\(\)]", "", str(name_year.text()))
    filmId = getFilmID(str(without_brackets[:-4]), str(without_brackets[-4:]))

    score_1_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_2_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_3_button.setIcon(QIcon(('icons8-star-filled-48')))

    score_4_button.setIcon(QIcon(('icons8-star-filled-48')))
    score_5_button.setIcon(QIcon(('icons8-star-filled-48')))
    score = 5

    deleteScoreUser(int(userid1), filmId)
    addVotesAndScoreUser(int(userid1), filmId, score)
