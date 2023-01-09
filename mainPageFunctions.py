from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox, QCompleter, QListWidgetItem
from PyQt5.QtGui import QIcon

from LogicApplication.getAndSetScoreFilms import *
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getDataFromIMDB import *
from LogicApplication.getAndSetReviews import *
from main_page import *
from LogicApplication.reviewLogic import *




def addReviewToDB(idUser,filmId, reviewText, stackedWidget, yourReviewLabel):
    if(reviewText!=""):
        userid1 = re.sub("[^0-9]", "", idUser.text())
        stackedWidget.setCurrentIndex(1)
        yourReviewLabel.setText(reviewText)
        addReview(userid1,filmId,reviewText)

def setReview(idUser,filmId,userName1,reviewText1,userName2,reviewText2, userName3,
              reviewText3,userName4, reviewText4,userName5,
              reviewText5,stackedWidgetReview,userReviewLabel, frame1, frame2,frame3,frame4,frame5,
              reviewScore1, reviewScore2, reviewScore3,reviewScore4,reviewScore5, idReview1, idReview2, idReview3, idReview4, idReview5, currentPage, reviewCount):
    userid1 = re.sub("[^0-9]", "", idUser.text())
    allReviews = getAllReviewsForFilm(filmId)
    k=int(reviewCount.text())
    cp=(int(currentPage)-1)*5
    if len(allReviews)==0:
        stackedWidgetReview.setCurrentIndex(0)

    for row in allReviews:
        if str(row.idUser) == userid1:
            stackedWidgetReview.setCurrentIndex(1)
            userReviewLabel.setText(row.review)
            break
        else:
            stackedWidgetReview.setCurrentIndex(0)

    if(k==1):
        userName1.setText(allReviews[cp].username)
        reviewText1.setText(allReviews[cp].review)
        reviewScore1.setText(str(allReviews[cp].scoreReview))
        idReview1.setText(str(allReviews[cp].review_id))

        frame1.setMaximumSize(QtCore.QSize(970, 400))
        frame2.setMaximumSize(QtCore.QSize(0, 0))
        frame3.setMaximumSize(QtCore.QSize(0, 0))
        frame4.setMaximumSize(QtCore.QSize(0, 0))
        frame5.setMaximumSize(QtCore.QSize(0, 0))

    elif(k==2):
        userName1.setText(allReviews[cp].username)
        reviewText1.setText(allReviews[cp].review)
        reviewScore1.setText(str(allReviews[cp].scoreReview))
        idReview1.setText(str(allReviews[cp].review_id))

        userName2.setText(allReviews[cp+1].username)
        reviewText2.setText(allReviews[cp+1].review)
        reviewScore2.setText(str(allReviews[cp+1].scoreReview))
        idReview2.setText(str(allReviews[cp+1].review_id))

        frame1.setMaximumSize(QtCore.QSize(970, 400))
        frame2.setMaximumSize(QtCore.QSize(970, 400))
        frame3.setMaximumSize(QtCore.QSize(0, 0))
        frame4.setMaximumSize(QtCore.QSize(0, 0))
        frame5.setMaximumSize(QtCore.QSize(0, 0))

    elif(k==3):
        userName1.setText(allReviews[cp].username)
        reviewText1.setText(allReviews[cp].review)
        reviewScore1.setText(str(allReviews[cp].scoreReview))
        idReview1.setText(str(allReviews[cp].review_id))

        userName2.setText(allReviews[cp+1].username)
        reviewText2.setText(allReviews[cp+1].review)
        reviewScore2.setText(str(allReviews[cp+1].scoreReview))
        idReview2.setText(str(allReviews[cp+1].review_id))

        userName3.setText(allReviews[cp+2].username)
        reviewText3.setText(allReviews[cp+2].review)
        reviewScore3.setText(str(allReviews[cp+2].scoreReview))
        idReview3.setText(str(allReviews[cp+2].review_id))

        frame1.setMaximumSize(QtCore.QSize(970, 400))
        frame2.setMaximumSize(QtCore.QSize(970, 400))
        frame3.setMaximumSize(QtCore.QSize(970, 400))
        frame4.setMaximumSize(QtCore.QSize(0, 0))
        frame5.setMaximumSize(QtCore.QSize(0, 0))

    elif(k==4):
        userName1.setText(allReviews[cp].username)
        reviewText1.setText(allReviews[cp].review)
        reviewScore1.setText(str(allReviews[cp].scoreReview))
        idReview1.setText(str(allReviews[cp].review_id))

        userName2.setText(allReviews[cp+1].username)
        reviewText2.setText(allReviews[cp+1].review)
        reviewScore2.setText(str(allReviews[cp+1].scoreReview))
        idReview2.setText(str(allReviews[cp+1].review_id))

        userName3.setText(allReviews[cp+2].username)
        reviewText3.setText(allReviews[cp+2].review)
        reviewScore3.setText(str(allReviews[cp+2].scoreReview))
        idReview3.setText(str(allReviews[cp+2].review_id))

        userName3.setText(allReviews[cp+3].username)
        reviewText3.setText(allReviews[cp+3].review)
        reviewScore3.setText(str(allReviews[cp+3].scoreReview))
        idReview3.setText(str(allReviews[cp+3].review_id))

        frame1.setMaximumSize(QtCore.QSize(970, 400))
        frame2.setMaximumSize(QtCore.QSize(970, 400))
        frame3.setMaximumSize(QtCore.QSize(970, 400))
        frame4.setMaximumSize(QtCore.QSize(970, 400))
        frame5.setMaximumSize(QtCore.QSize(0, 0))

    elif (k>=5):
        userName1.setText(allReviews[cp].username)
        reviewText1.setText(allReviews[cp].review)
        reviewScore1.setText(str(allReviews[cp].scoreReview))
        idReview1.setText(str(allReviews[cp].review_id))

        userName2.setText(allReviews[cp+1].username)
        reviewText2.setText(allReviews[cp+1].review)
        reviewScore2.setText(str(allReviews[cp+1].scoreReview))
        idReview2.setText(str(allReviews[cp+1].review_id))

        userName3.setText(allReviews[cp+2].username)
        reviewText3.setText(allReviews[cp+2].review)
        reviewScore3.setText(str(allReviews[cp+2].scoreReview))
        idReview3.setText(str(allReviews[cp+2].review_id))

        userName4.setText(allReviews[cp+3].username)
        reviewText4.setText(allReviews[cp+3].review)
        reviewScore4.setText(str(allReviews[cp+3].scoreReview))
        idReview4.setText(str(allReviews[cp+3].review_id))

        userName5.setText(allReviews[cp+4].username)
        reviewText5.setText(allReviews[cp+4].review)
        reviewScore5.setText(str(allReviews[cp+4].scoreReview))
        idReview5.setText(str(allReviews[cp+4].review_id))


        frame1.setMaximumSize(QtCore.QSize(970, 400))
        frame2.setMaximumSize(QtCore.QSize(970, 400))
        frame3.setMaximumSize(QtCore.QSize(970, 400))
        frame4.setMaximumSize(QtCore.QSize(970, 400))
        frame5.setMaximumSize(QtCore.QSize(970, 400))

    elif(k==0):
        frame1.setMaximumSize(QtCore.QSize(0, 0))
        frame2.setMaximumSize(QtCore.QSize(0, 0))
        frame3.setMaximumSize(QtCore.QSize(0, 0))
        frame4.setMaximumSize(QtCore.QSize(0, 0))
        frame5.setMaximumSize(QtCore.QSize(0, 0))

def editReview(idUser,filmId,stackedWidgetReview, newReviewText, oldReviewText):
    userid1 = re.sub("[^0-9]", "", idUser.text())
    changeRivewText(userid1, filmId, newReviewText.toPlainText())
    stackedWidgetReview.setCurrentIndex(1)
    newReviewText.setText("")

def changingPageInEditing(stackedWidgetReview, newReviewText, oldReviewText):
    stackedWidgetReview.setCurrentIndex(2)
    newReviewText.setText(oldReviewText)

def deleteReviewFromDB(idUser,filmId):
    userid1 = re.sub("[^0-9]", "", idUser.text())
    deleteReview(userid1,filmId)

def changeScore(idUser,filmId, increment, button, allLabels):
    userid1 = re.sub("[^0-9]", "", idUser.text())
    allLikes=getLikesListForThisFilmReviews(filmId)
    for c in button:
        if c.isnumeric():
            reviewId=allLabels[int(c)-1]
        else:
            reviewId=allLabels[0]



    reviewScoreButton(int(userid1), int(reviewId), increment, allLikes)

def report(allComboBox, buttonName, send_buttons):
    reports= getAllReportTypes()
    allReports=[]
    for report in reports:
        allReports.append(''.join(report[1]))
    for comboBox in allComboBox:
        if comboBox.count() ==0:
            comboBox.addItems(allReports)


    if buttonName[-1].isnumeric():
        allComboBox[int(buttonName[-1]) - 1].setMaximumSize(QtCore.QSize(200, 50))
        allComboBox[int(buttonName[-1]) - 1].setGeometry(QtCore.QRect(700, 94, 150, 20))
        send_buttons[int(buttonName[-1]) - 1].setGeometry(QtCore.QRect(860, 80, 61, 40))


    else:
        allComboBox[0].setMaximumSize(QtCore.QSize(200, 50))
        allComboBox[0].setGeometry(QtCore.QRect(700, 94, 150, 20))
        send_buttons[0].setGeometry(QtCore.QRect(860, 80, 61, 40))

def sendRep(buttonName, allComboBoxes, idReviews, idUser, all_buttons):
    userid1 = re.sub("[^0-9]", "", idUser.text())


    for c in buttonName:
        if c.isnumeric():
            allComboBoxes[int(c) - 1].setMaximumSize(QtCore.QSize(200, 0))
            all_buttons[int(c) - 1].setGeometry(QtCore.QRect(860, 80, 61, 0))
            reviewId=idReviews[int(c)-1]
            createReportReview(int(reviewId),int(userid1) ,allComboBoxes[int(c) - 1].currentIndex())


def changePPage(reviewCount, currPage, allComboBox, allButtons):
    k=int(reviewCount.text())
    for comboBox in allComboBox:
        comboBox.setMaximumSize(QtCore.QSize(200, 0))
    for button in allButtons:
        button.setGeometry(QtCore.QRect(860, 80, 61, 0))
    if (int(currPage.text())>1):
        currPage.setText(str(int(currPage.text())-1))
        reviewCount.setText(str(k+5))

def changeNPage(reviewCount, currPage, allComboBox, allButtons):
    k=int(reviewCount.text())
    for comboBox in allComboBox:
        comboBox.setMaximumSize(QtCore.QSize(200, 0))
    for button in allButtons:
        button.setGeometry(QtCore.QRect(860, 80, 61, 0))

    if k>5:
        currPage.setText(str(int(currPage.text()) + 1))
        reviewCount.setText(str(k-5))

def setCount(filmId, countLabel):
    allReviews = getAllReviewsForFilm(filmId)
    countLabel.setText(str(len(allReviews)))
