from LogicApplication.userDataValidation import *

def sent(email,wrong_email):
    if sendMailForgoutPassword(email.text())==1:
        pass
        wrong_email.setFixedSize(0, 0)
    else:
        wrong_email.setFixedSize(276, 13)

def newpassword(code,newpass,confirmpass,email,wrong_email,wrong_password,wrong_code,wrongPassword2):
    if ForgoutPassword(email.text(),code.text(),newpass.text(),confirmpass.text()):
        print('nice')
        wrong_code.setFixedSize(0, 0)
        wrong_password.setFixedSize(0, 0)
        wrongPassword2.setFixedSize(0, 0)
    else:

        wrong_code.setFixedSize(276, 13)
        wrong_password.setFixedSize(276, 13)
        wrongPassword2.setFixedSize(276, 13)