from LogicApplication.DB_connector import *
import mysql.connector
import bcrypt
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
from datetime import datetime, date


def checkUsernameExist(username):
    con = createConnection()
    cur = con.cursor()
    existUsernameSQL = """
        SELECT * FROM user WHERE username =%s"""
    cur.execute(existUsernameSQL, [username])
    existUsername = cur.fetchone()
    if existUsername != None:
        return True
    if len(username) > 4 and len(username) <= 18:
        return False
    return True
def validatePassword(password):
    l,u,p,d = 0,0,0,0
    capitAlalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallAlphabets = "abcdefghijklmnopqrstuvwxyz"
    specialChar = "!@#$%^&*()_+=-/><.,"
    digits = "0123456789"
    if(len(password)>=8):
        for i in password:
            if(i in smallAlphabets):
                l+=1
            if (i in capitAlalphabets):
                u+=1
            if (i in digits):
                d+=1
            if (i in specialChar):
                p+=1
    if(l>=1 and u>=1 and p>=1 and d >=1 and l+p+u+d==len(password)):
        return True
    else:
        print( "Bad password. Your password must be at least 8 characters including a lowercase letter, an uppercase letter, a number, and a special char!")
        return False
def AuthenticateUser (login, password):
    stime = datetime.now()
    sqlAuthenticateUser = """
    SELECT password FROM user WHERE username = %s 
    """
    con = createConnection()
    cur = con.cursor()
    cur.execute(sqlAuthenticateUser,[login])
    for row in cur.fetchall():
        hashDataBase = row[0]
        #hashDataBase = hashDataBase.replace('b', '',1)
        hashDataBase = hashDataBase.replace("'", "")
    if bcrypt.checkpw(password.encode('utf-8'), hashDataBase.encode('utf-8')):
        print("Authinticate user = ", datetime.now() - stime)
        return True
    print("Authinticate user = ", datetime.now() - stime)
    return False
def checkEmailExist(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    con = createConnection()
    cur = con.cursor()
    existMailSQL = """
    SELECT * FROM user WHERE "email" =%s"""
    cur.execute(existMailSQL,[email])
    existMail = cur.fetchone()
    if existMail != None:
        return True
    if re.match(pattern,email):
        return False
    return True

def checkEmailForgoutPassword(email):
    con = createConnection()
    cur = con.cursor()
    chekEmailSQL = """
    SELECT * FROM user WHERE email = %s"""
    cur.execute(chekEmailSQL, [email])
    existMailForgoutPassword = cur.fetchone()
    if existMailForgoutPassword != None:
        return True
    return False
def RegistrationUser(username, email, password, repeatPassword):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    createAcconutSQL = """INSERT INTO user (username, email, password) VALUES (%s, %s, %s)"""
    if checkUsernameExist(username) == False and checkEmailExist(email) == False and validatePassword(password) and password == repeatPassword:
        cur.execute(createAcconutSQL, [(username), (email), (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))])
        con.commit()
        print("Registrate user user = ", datetime.now() - stime)
        print ("Account has been created!")
    else:
        print("Registrate user user = ", datetime.now() - stime)
        print("User exist!")

def gennerateVereficationCodeEmail():
    code = ''
    for i in range(6):
        code = code + random.choice(list('1234567890'))
    return code
verCode = gennerateVereficationCodeEmail()

def sendMailForgoutPassword(userEmail):
    global verCode
    verCode = gennerateVereficationCodeEmail()
    if checkEmailForgoutPassword(userEmail)!=True:
        print("This is email in not exist")
        return 0
    msg = MIMEMultipart()
    message = "Your verecication code is: " + verCode + "\nPlese, enter this code in application!"
    passwordEmail = "gdqmnzokxrktxbok"
    msg['From'] = "srmp.app@gmail.com"
    msg['To'] = userEmail
    msg['Subject'] = "Verefication code"

    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], passwordEmail)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("Email send successfully!")


def ForgoutPassword(email, verificationCode, password, repeatPassword):
    global verCode
    con = createConnection()
    cur = con.cursor()
    sqlUpdatePassword = """
    UPDATE user SET password = %s WHERE email =%s"""
    if verificationCode == verCode and password == repeatPassword and validatePassword(password):
        value = (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()), email)
        cur.execute(sqlUpdatePassword,value)
        con.commit()
        print("Your password has been successfully changed")
        return True
    elif verificationCode != verCode:
        print("Bad verefication code!")
    elif password!=repeatPassword:
        print("Password and confirm password does not match.")
    else:
        print("Bad password!")
    return False

def getDataUser (username):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlGetDataUser = """
    SELECT * FROM user WHERE username = %s"""
    cur.execute(sqlGetDataUser, username)
    userData = cur.fetchone()
    print("Get data user = ", datetime.now() - stime)
    return userData

def updateLastVisitDataTime (id):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlUpdateData = """
    UPDATE user SET lastvisitdata = %s WHERE id = %s"""
    cur.execute(sqlUpdateData, [(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), (id)])
    con.commit()
    print ("Update last visit data successful!")
    print("Update last visit data = ", datetime.now() - stime)








