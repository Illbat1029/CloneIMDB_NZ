

from LogicApplication.userDataValidation import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLabel, QComboBox
from LogicApplication.getAndSetReviews import *
from PyQt5.QtCore import QDate

from main_page import *
from LogicApplication.reviewLogic import *
from LogicApplication.methodsAdminAndModerator import *




def addReviewToDB(idUser,filmId, reviewText, stackedWidget, yourReviewLabel):
    if(reviewText!=""):
        userid1 = re.sub("[^0-9]", "", idUser.text())
        stackedWidget.setCurrentIndex(1)
        yourReviewLabel.setText(reviewText)
        addReview(userid1,filmId,reviewText)

def setReview(idUser,filmId,userName1,reviewText1,userName2,reviewText2, userName3,
              reviewText3,userName4, reviewText4,userName5,
              reviewText5,stackedWidgetReview,userReviewLabel, frame1, frame2,frame3,frame4,frame5,
              reviewScore1, reviewScore2, reviewScore3,reviewScore4,reviewScore5, idReview1, idReview2, idReview3, idReview4, idReview5, currentPage, reviewCount, mainFrame):
    userid1 = re.sub("[^0-9]", "", idUser.text())
    allReviews = getAllReviewsForFilm(filmId)
    allLikes= getLikesListForThisFilmReviews(filmId)
    allIdReview= [idReview1, idReview2, idReview3, idReview4, idReview5]
    frameButtons =mainFrame.findChildren(QPushButton)
    frameLikeButtons=[]
    for button in frameButtons:
        if button.objectName()[:10] == 'likeReview':
                frameLikeButtons.append(button)


    frameButtons =mainFrame.findChildren(QPushButton)
    frameDislikeButtons=[]
    for button in frameButtons:
        if button.objectName()[:13] == 'dislikeReviwe':
                frameDislikeButtons.append(button)

    for i in range(5):
        frameLikeButtons[i].setStyleSheet("image: url(:/icon/plus.svg);")
        frameDislikeButtons[i].setStyleSheet("image: url(:/icon/minus.svg);")


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


    for like in allLikes:
        if like[0]==int(userid1):
            for i in range(len(allIdReview)):
                if allIdReview[i].text()!="":
                    if int(allIdReview[i].text())== like[1]:
                        if like[2]==1:
                            frameLikeButtons[i].setStyleSheet("image: url(:/icon/plus.svg); background-color: rgb(0, 255, 0);")
                            frameDislikeButtons[i].setStyleSheet("image: url(:/icon/minus.svg);")
                        elif like[2]==-1:
                            frameDislikeButtons[i].setStyleSheet("image: url(:/icon/minus.svg); background-color: rgb(255, 0, 0);")
                            frameLikeButtons[i].setStyleSheet("image: url(:/icon/plus.svg);")


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
        send_buttons[int(buttonName[-1]) - 1].setGeometry(QtCore.QRect(855, 80, 55, 40))
        send_buttons[int(buttonName[-1]) - 1].setGeometry(QtCore.QRect(860, 80, 61, 40))
    else:
        allComboBox[0].setMaximumSize(QtCore.QSize(200, 50))
        allComboBox[0].setGeometry(QtCore.QRect(700, 94, 150, 20))
        send_buttons[0].setGeometry(QtCore.QRect(855, 80, 55, 40))

def sendRep(buttonName, allComboBoxes, idReviews, idUser, all_buttons):
    userid1 = re.sub("[^0-9]", "", idUser.text())
    for c in buttonName:
        if c.isnumeric():
            allComboBoxes[int(c) - 1].setMaximumSize(QtCore.QSize(200, 0))
            all_buttons[int(c) - 1].setGeometry(QtCore.QRect(855, 80, 55, 0))
            reviewId=idReviews[int(c)-1]
            createReportReview(int(reviewId),int(userid1) ,(allComboBoxes[int(c) - 1].currentIndex()+1))

def changePPage(reviewCount, currPage, allComboBox, allButtons):
    k=int(reviewCount.text())
    for comboBox in allComboBox:
        comboBox.setMaximumSize(QtCore.QSize(200, 0))
    for button in allButtons:
        button.setGeometry(QtCore.QRect(855, 80, 55, 0))
    if (int(currPage.text())>1):
        currPage.setText(str(int(currPage.text())-1))
        reviewCount.setText(str(k+5))
def changeNPage(reviewCount, currPage, allComboBox, allButtons):
    k=int(reviewCount.text())
    for comboBox in allComboBox:
        comboBox.setMaximumSize(QtCore.QSize(200, 0))
    for button in allButtons:
        button.setGeometry(QtCore.QRect(855, 80, 55, 0))

    if k>5:
        currPage.setText(str(int(currPage.text()) + 1))
        reviewCount.setText(str(k-5))

def setCount(filmId, countLabel):
    allReviews = getAllReviewsForFilm(filmId)
    countLabel.setText(str(len(allReviews)))

def addFilmToDB(lineEdit):
    a=lineEdit.text()
    if "-" in a:
        indexes = a.split("-")
        if int(indexes[0])<int(indexes[1]):
            addFilmsAdmin(int(indexes[0]),int(indexes[1]))
            lineEdit.setText("")
    else:
        addFilmsAdmin(int(a))
        lineEdit.setText("")

def deleteFilmFromDBUI(lineEdit):
    deleteFilmFromDB(lineEdit.text())
    lineEdit.setText("")


def refreshReviewCheck(userName1,reviewText1,userName2,reviewText2, userName3,
              reviewText3, frame1, frame2,frame3,
              reportType1, reportType2, reportType3,idReview1, idReview2, idReview3, currentPage, reviewRepCount):
    allReports=getAllReportReviews()
    if reviewRepCount.text()=="":
        reviewRepCount.setText(str(len(allReports)))
    k=int(reviewRepCount.text())
    cp=(int(currentPage)-1)*3

    if(k==1):
        userName1.setText(allReports[cp].username)
        reviewText1.setText(allReports[cp].review)
        reportType1.setText(str(allReports[cp].type))
        idReview1.setText(str(allReports[cp].review_id))

        frame1.setMaximumSize(QtCore.QSize(970, 400))
        frame1.setGeometry(QtCore.QRect(10, 50, 927, 160)   )
        frame2.setMaximumSize(QtCore.QSize(0, 0))
        frame2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        frame3.setMaximumSize(QtCore.QSize(0, 0))
        frame3.setGeometry(QtCore.QRect(0, 0, 0, 0))

    elif(k==2):
        userName1.setText(allReports[cp].username)
        reviewText1.setText(allReports[cp].review)
        reportType1.setText(str(allReports[cp].type))
        idReview1.setText(str(allReports[cp].review_id))

        userName2.setText(allReports[cp+1].username)
        reviewText2.setText(allReports[cp+1].review)
        reportType2.setText(str(allReports[cp+1].type))
        idReview2.setText(str(allReports[cp+1].review_id))

        frame1.setMaximumSize(QtCore.QSize(970, 400))
        frame1.setGeometry(QtCore.QRect(10, 50, 927, 160))
        frame2.setMaximumSize(QtCore.QSize(970, 400))
        frame2.setGeometry(QtCore.QRect(10, 200, 927, 160))
        frame3.setMaximumSize(QtCore.QSize(0, 0))
        frame3.setGeometry(QtCore.QRect(0, 0, 0, 0))


    elif(k>=3):
        userName1.setText(allReports[cp].username)
        reviewText1.setText(allReports[cp].review)
        reportType1.setText(str(allReports[cp].type))
        idReview1.setText(str(allReports[cp].review_id))

        userName2.setText(allReports[cp+1].username)
        reviewText2.setText(allReports[cp+1].review)
        reportType2.setText(str(allReports[cp+1].type))
        idReview2.setText(str(allReports[cp+1].review_id))

        userName3.setText(allReports[cp+2].username)
        reviewText3.setText(allReports[cp+2].review)
        reportType3.setText(str(allReports[cp+2].type))
        idReview3.setText(str(allReports[cp+2].review_id))

        frame1.setMaximumSize(QtCore.QSize(970, 400))
        frame1.setGeometry(QtCore.QRect(10, 50, 927, 160))
        frame2.setMaximumSize(QtCore.QSize(970, 400))
        frame2.setGeometry(QtCore.QRect(10, 200, 927, 160))
        frame3.setMaximumSize(QtCore.QSize(970, 400))
        frame3.setGeometry(QtCore.QRect(10, 350, 927, 160))



    elif(k==0):
        frame1.setMaximumSize(QtCore.QSize(0, 0))
        frame2.setMaximumSize(QtCore.QSize(0, 0))
        frame3.setMaximumSize(QtCore.QSize(0, 0))



def deleteRep(buttonName, idReviews):
    c=int(buttonName[-1])
    deleteReviewAfterValidation(int(idReviews[c-1].text()))

def deleteOkRep(buttonName, idReviews):
    c=int(buttonName[-1])
    deleteReviewFromAdminTableWhereReviewGood(int(idReviews[c-1].text()))
