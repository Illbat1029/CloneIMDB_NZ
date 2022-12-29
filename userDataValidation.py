from DB_connector import *
import mysql.connector
import bcrypt
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
from datetime import datetime, date
import base64
from PIL import Image
import io
import imdb
from imdb import Cinemagoer
import requests
import urllib
import os

def checkUsernameExist(username):
    con = createConnection()
    cur = con.cursor()
    existUsernameSQL = """
        SELECT * FROM user WHERE username =%s"""
    cur.execute(existUsernameSQL, [username])
    existUsername = cur.fetchone()
    if existUsername != None:
        return True
    if len(username) > 4 and len(username) < 18:
        return False
    return True

def validatePassword(password):
    l,u,p,d = 0,0,0,0
    capitAlalphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallAlphabets = "abcdefghijklmnopqrstuvwxyz"
    specialChar = "!@#$%^&*()_+=-/><"
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
        return True
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
    con = createConnection()
    cur = con.cursor()
    createAcconutSQL = """INSERT INTO user (username, email, password) VALUES (%s, %s, %s)"""
    if checkUsernameExist(username) == False and checkEmailExist(email) == False and validatePassword(password) and password == repeatPassword:
        cur.execute(createAcconutSQL, [(username), (email), (bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))])
        con.commit()
        print ("Account has been created!")
    else:
        print("User exist!")

def gennerateVereficationCodeEmail():
    code = ''
    for i in range(6):
        code = code + random.choice(list('1234567890'))
    return code
verCode = gennerateVereficationCodeEmail()

def sendMailForgoutPassword(userEmail):
    global verCode
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
    con = createConnection()
    cur = con.cursor()
    sqlGetDataUser = """
    SELECT * FROM user WHERE username = %s"""
    cur.execute(sqlGetDataUser, username)
    userData = cur.fetchone()
    return userData

def updateLastVisitDataTime (id):
    con = createConnection()
    cur = con.cursor()
    sqlUpdateData = """
    UPDATE user SET lastvisitdata = %s WHERE id = %s"""
    cur.execute(sqlUpdateData, [(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), (id)])
    con.commit()
    print ("Update last visit data successful!")


def createFilm(filmname, description, country, genre, language, releasedata, runtime, score, vote, director, actors):
    file = open("Images_Film/1.png", 'rb').read()
    file = base64.b64encode(file)
    con = createConnection()
    cur = con.cursor()
    sqlInsertFim = """
    INSERT INTO films (filmname, description, country, gen, language, releasedata, runtime, score, vote, director, actors, picture) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
    """
    args = (filmname,
            description,
            country,
            genre,
            language,
            releasedata,
            runtime,
            score,
            vote,
            director,
            actors,
            file)
    cur.execute(sqlInsertFim,args)
    con.commit()
def getfilm():
    con = createConnection()
    cur = con.cursor()
    sqlGetFilm ="""
    SELECT picture FROM films WHERE id = 3"""
    cur.execute(sqlGetFilm)
    data = cur.fetchall()
    image = data[0][0]
    binary_data = base64.b64decode(image)
    image = Image.open(io.BytesIO(binary_data))
    image.show()

def downloadImages(imURL):
    urllib.request.urlretrieve(imURL, "Images_Film/1.png")
def getDataFilmIMDB():
    ia = imdb.IMDb()
    code = "0133093"

    ib = Cinemagoer()
    movie = ia.get_movie(code)

    #name film and all data
    series = ia.get_movie(code)
    print("NAME:")
    print(series)

    # description
    outline = series.data['plot outline']
    print("Description:")
    print(outline)

    #countries
    country = "" #series.data['countries'][0]
    for c in series.data['countries']:
        country = country+c+";"
    print("Country:")
    print(country)

    # genre
    print("GENRE:")
    genre = ""
    for i in series.data['genres']:
        genre = genre + i+";"
    print(genre)

    #language
    print("Language:")
    lang = ""
    for lan in movie['language']:
        lang = lang +lan+";"
    print(lang)

    #release data
    year = series.data['year']
    print("RELEASE:")
    print(year)

    #runtime
    runtimes = series.data['runtimes'][0]
    print("RUNTIME:")
    print(runtimes)

    #director
    print("DIRECTOR:")
    directorS = ""
    try:
        for director in movie['director']:
            directorS = directorS + str(director) +";"
    except:
        directorS = ""
        print("BRAK")
    print(directorS)


    #actor
    print("ACTORS:")
    cast = ""
    c = series.data['cast']
    for i in range(len(c)):
        cast = cast +str(c[i])+";"
    print(cast)

    #images
    print("IMAGES URL:")
    cover = series.data['cover url']
    #downloadImages(cover)
    print(cover)

    if directorS == "":
        directorS = "BRAK"
    #createFilm(str(series), outline, country, genre, lang,year,runtimes,0,0,dir,cast)





