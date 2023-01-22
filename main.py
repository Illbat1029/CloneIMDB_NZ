import sys
import os
from PIL.ImageQt import ImageQt

from PyQt5.QtCore import  QPropertyAnimation, QEasingCurve, Qt ,QSize
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QMessageBox, QCompleter, QListWidgetItem,QLabel
from PyQt5.QtGui import QIcon

import StyleSheetForButtons

from Login_page import *
from main_page import *
from forgot_GUI import *
#from search_field import *
from LogicApplication.userDataValidation import *
from LogicApplication.DB_connector import *
from LogicApplication.getFilmsDataFromDB import *
from LogicApplication.getAndSetDataFilmStatusUser import *
from LogicApplication.getAndSetScoreFilms import *
from LogicApplication.getAndSetReviews import *
from LogicApplication.methodsAdminAndModerator import *
from LogicApplication.reviewLogic import *

if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    Log_page_form = QtWidgets.QWidget()
    Log_page = Login()
    Log_page.setupUi(Log_page_form)
    Log_page_form.show()


    Main_page_form = QtWidgets.QWidget()
    Main_page = Main_page()
    Main_page.setupUi(Main_page_form)

    Fogort_page_from=QtWidgets.QWidget()
    Fogort_page=Forgot_page()
    Fogort_page.setupUi(Fogort_page_from)

    def login():
        #getListAllDataAllFilms()
       #a=getListAllFilmWithGenresUser(["Adventure", "Comedy"])
       #for i in range(len(a)):
        #   print(a[i].name, a[i].genres)
        #createReportReview(4, 9, 2)
        #getListAllFilmsWithPeopleUserAndStatus("Matthias Schweighöfer")
        #getListAllFilmsWithPeopleUserAndStatus("Frank Darabont")
        #addFilmsAdmin(993840)
        #getListAllFilmsWithPeopleUser("Matthias Schweighöfer")
        #getAllDataFilmByID(1)
        #getAllDataFilmByReleaseDataBetween(2000, 2010)
        #getAllDataFilmByReleaseDataBetween()
        #getAllDataFilmByLanguage("Spanish")
        #getAllDataFilmByCountry("Israel")
        #getAllDataFilmByScoreBetween(1,2) //POKA NETU NI 1 FILMA SO SCORE
        #a= getFilmByFilmname("The Shawshank Redemption")
        #for i in range(len(a)):
            #print(a[i].id ,a[i].name, a[i].genres)
        #updateEmailUser(6, "maks@gmaillllll.lll")
        #updatePasswordUser(22, "Ha!2.324345m,@")
        #updatateUserUsername(22, "Kalycz")
        #a = getViewFilmDataWhereUserNotLogin()

        try:
            if len(Log_page.user_or_email.text()) != 0 and len(Log_page.password.text()) != 0 and AuthenticateUser(Log_page.user_or_email.text(), Log_page.password.text()):
                dataUser = getDataUser([Log_page.user_or_email.text()])
                updateLastVisitDataTime(dataUser[0])
                Main_page_form.show()
                Log_page_form.close()
                Main_page.username_lable.setText(Log_page.user_or_email.text())
                Main_page.id_label.setText('ID: '+  str(dataUser[0]))
                if (Main_page.username_lable.text())[:14] == 'adminCloneImdb':
                     Main_page.adminPageBttn.setMaximumSize(25,25)
                     Main_page.moderatorPageBttn.setMaximumSize(25, 25)
                elif (Main_page.username_lable.text())[:18] == 'moderatorCloneImdb':
                    Main_page.moderatorPageBttn.setMaximumSize(25,25)
            else:
                Log_page.push_up_login_notifikation.setFixedSize(276, 10)
        except:
            Log_page.push_up_login_notifikation.setFixedSize(276,10)
        Main_page.stackedWidget.setCurrentIndex(0)
        Main_page.home_button.setStyleSheet(StyleSheetForButtons.home_pressed)
    def fogort():
        Fogort_page.wrong_email.setFixedSize(0, 0)
        Fogort_page.wrong_code.setFixedSize(0, 0)
        Fogort_page.wrong_password.setFixedSize(0, 0)
        Fogort_page.wrongPassword2.setFixedSize(0, 0)
        Fogort_page_from.show()
    def sent_forgot():
        Fogort_page.wrong_email.setFixedSize(276, 13)
        Fogort_page.wrong_code.setFixedSize(276, 13)
        Fogort_page.wrong_password.setFixedSize(276, 13)
        Fogort_page.wrongPassword2.setFixedSize(276, 13)
    film_bttn ={}
    film_bttn_not_text = {}
    film_name = {}
    film_name_not_text = {}
    buttons = Main_page.widget.findChildren(QPushButton)
    Labels = Main_page.widget.findChildren(QLabel)
    for button in buttons:
        for i in range(19):
            if button.objectName() == 'home_film_bttn' + str(i):
                film_bttn[i]=button.objectName()
                film_bttn_not_text[i]=button
    for label in Labels:
        for i in range(19):
            if label.objectName() == 'home_name_film' + str(i):

                film_name_not_text[i]=label
    a = getListAllDataAllFilms()
    x=0
    for i in film_bttn_not_text.keys():
        binary_data = base64.b64decode(a[i-1 ].images)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(binary_data)
        film_name_not_text[i].setText(a[i-1].name)
        film_bttn_not_text[i].setIconSize(QSize(100, 140))
        film_bttn_not_text[i].setIcon(QIcon(pixmap))
    Log_page.bttn_forgot.clicked.connect(fogort)
    Log_page.bttn_login.clicked.connect(login)
    Fogort_page.sentCodelForgotBttn.clicked.connect(sent_forgot)
    sys.exit(app.exec_())