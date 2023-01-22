import time
start_time = time.time()
import base64
import sys
import os


from PyQt5.QtCore import  QSize

from PyQt5.QtGui import QIcon

import StyleSheetForButtons

from Login_page import *
from main_page import *
from forgot_GUI import *
import time
from change_username import *
from change_email import *
from change_passwrod import *
from LogicApplication.userDataValidation import *

from LogicApplication.getFilmsDataFromDB import *


if __name__ == "__main__":

    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    Log_page_form = QtWidgets.QWidget()
    Log_page = Login()
    Log_page.setupUi(Log_page_form)

    Log_page_form.show()

#    addFilmsAdmin(2278388)

    Main_page_form = QtWidgets.QWidget()
    Main_page = Main_page()
    Main_page.setupUi(Main_page_form)

    change_username_form = QtWidgets.QWidget()
    change_username = change_username()
    change_username.setupUi(change_username_form)

    change_email_form = QtWidgets.QWidget()
    change_email = change_email()
    change_email.setupUi(change_email_form)

    change_passwrod_form = QtWidgets.QWidget()
    change_passwrod = change_passwrod()
    change_passwrod.setupUi(change_passwrod_form)

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

        #getListAllFilmsWithPeopleUser("Matthias Schweighöfer")
        #getAllDataFilmByID(1)
        #getAllDataFilmByReleaseDataBetween(2000, 2010)
        #getAllDataFilmByReleaseDataBetween()
        #getAllDataFilmByLanguage("Spanish")
        #getAllDataFilmByCountry("Israel")
        #getAllDataFilmByScoreBetween(1,2) //POKA NETU NI 1 FILMA SO SCORE
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
                elif (Main_page.username_lable.text())[:18] == 'moderatorCloneImdb':
                    Main_page.moderatorPageBttn.setMaximumSize(25,25)


            else:
                Log_page.push_up_login_notifikation.setFixedSize(276, 10)
        except:
            Log_page.push_up_login_notifikation.setFixedSize(276,10)
        Main_page.stackedWidget.setCurrentIndex(6)
        Main_page.settings_button.setStyleSheet(StyleSheetForButtons.settings_pressed)
    def fogort():
        Fogort_page.wrong_email.setFixedSize(0, 0)
        Fogort_page.wrong_code.setFixedSize(0, 0)
        Fogort_page.wrong_password.setFixedSize(0, 0)
        Fogort_page.wrongPassword2.setFixedSize(0, 0)
        Fogort_page.Email_forgot_password.setText('')
        Fogort_page.New_password.setText('')
        Fogort_page.Code_forgot_password.setText('')
        Fogort_page.Confirm_password_forgot_page.setText('')
        Fogort_page_from.show()
    def open_window_to_change_username():
        change_username_form.show()


    def open_window_to_change_email():
        change_email_form.show()
    def open_window_to_change_password():
        change_passwrod_form.show()
    def confirm_username():
        id = re.sub("[^0-9]", "", Main_page.id_label.text())
        newname=change_username.New_name.text()
        change_username.username_exist.setText('')
        change_username.username_exist.setFixedSize(0, 0)
        if updatateUserUsername(id, newname):
            print('good')
            Main_page.username_lable.setText(newname)
            change_username_form.close()
        else:
            change_username.username_exist.setFixedSize(276, 10)
            change_username.username_exist.setText('Already exists')
    def confirm_email():
        id = re.sub("[^0-9]", "", Main_page.id_label.text())
        newemail=change_email.New_email.text()
        change_email.wrong_email.setFixedSize(0, 0)
        change_email.wrong_email.setText('')
        if updateEmailUser(id, newemail):
            print('good')

            change_email_form.close()
        else:
            change_email.wrong_email.setFixedSize(276, 10)
            change_email.wrong_email.setText('Already exists')

    def confirm_pass():
        id = re.sub("[^0-9]", "", Main_page.id_label.text())
        newpass=change_passwrod.New_password.text()
        change_passwrod.wrong_password.setFixedSize(0, 0)
        change_passwrod.wrong_password.setText('')
        if updatePasswordUser(id,newpass):
            print('good')

            change_passwrod_form.close()
        else:
            change_passwrod.wrong_password.setFixedSize(276, 10)
            change_passwrod.wrong_password.setText('Incorrect')
    Main_page.change_username_bttn_sett.clicked.connect(open_window_to_change_username)
    Main_page.change_email_bttn_sett.clicked.connect(open_window_to_change_email)
    Main_page.change_pass_bttn_sett.clicked.connect(open_window_to_change_password)
    Log_page.bttn_forgot.clicked.connect(fogort)
    Log_page.bttn_login.clicked.connect(login)
    change_username.Confirm_Name.clicked.connect(confirm_username)
    change_email.Confirm_email.clicked.connect(confirm_email)
    change_passwrod.Confirm_password.clicked.connect(confirm_pass)
    end_time = time.time()
    print('время открытия приложения:' + str(end_time - start_time))
    sys.exit(app.exec_())