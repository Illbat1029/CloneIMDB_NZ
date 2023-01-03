import base64
from PIL import Image
import io
import imdb
from imdb import Cinemagoer
import requests
import urllib
import os
from LogicApplication.DB_connector import *
from datetime import datetime, timedelta

def addFilms(filmIDStart, filmIDEnd):
    a = 1
    stime = datetime.now()
    for i in range(filmIDStart, filmIDEnd):  # 112161
        try:
            getDataFilmIMDB(i, a)
            a = a + 1
            print(50 * "=")
        except:
            print("BAD URL")
            continue
    print("TIME ADDED FILMS = ", datetime.now() - stime)
    print(50 * "=")
    print(50 * "-")
    print("FILMS COUNT = ", a)
    print(50 * "-")
def existFilmDatabase(nameFilm, release):
    con = createConnection()
    cur = con.cursor()
    sqlIsFilmExist = """
    SELECT EXISTS(SELECT id FROM films WHERE filmname =%s  AND releasedata =%s)
    """
    arg = (
        nameFilm,
        release
    )
    cur.execute(sqlIsFilmExist, arg)
    isExist = cur.fetchone()
    isExist = isExist[0]
    return isExist
def createFilm(filmname, description, country, genre, language, releasedata, runtime, score, vote, director, actors):
    file = open("../Images_Film/1.png", 'rb').read()
    file = base64.b64encode(file)
    con = createConnection()
    cur = con.cursor()
    sqlInsertFim = """
    INSERT INTO films (filmname, description, country, gen, language, releasedata, runtime, score, vote, director, actors, picture) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
    """
    args = (filmname,
            description[0],
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
#download images
def downloadImagesPeop(imURL):
    urllib.request.urlretrieve(imURL, "Images_People/1.png")
def downloadImages(imURL):
    urllib.request.urlretrieve(imURL, "Images_Film/1.png")
def getDataFilmIMDB(code, num):
    print(30*"*")
    print("FILM NUMBER = ", num)
    code = str(code)
    if len(code) <7 :
        while len(code) != 7:
            code = '0' + code
    ia = imdb.IMDb()
    ib = Cinemagoer()
    movie = ia.get_movie(code)
    try:
    # name film and all data
        series = ia.get_movie(code)
    # description
        outline=[]
        outline = series.data['plot']
    # countries
        country = ""  # series.data['countries'][0]
        for c in series.data['countries']:
            country = country + c + ";"
    # genre
        genre = ""
        for i in series.data['genres']:
            genre = genre + i + ";"
    # language
        lang = ""
        for lan in movie['language']:
            lang = lang + lan + ";"
    # release data
        year = str(series.data['year'])
        if(len(year)) >4:
            year=year[4:]
    # runtime
        runtimes = series.data['runtimes'][0]
    # director
        directorS = ""
        for director in movie['director']:
            directorS = directorS + str(director) + ";"
    # actor
        cast = ""
        c = series.data['cast']
        for i in range(len(c)):
            cast = cast + str(c[i]) + ";"
    # images
        cover = series.data['cover url']
        downloadImages(cover)
        if existFilmDatabase(str(series), year) != 1:
            createFilm(str(series), outline, country, genre, lang, year, runtimes, 0, 0, directorS, cast)
            newFilmID = getFilmID(str(series), int(year))
            genresDataInsert(series.data['genres'], newFilmID)
            peopleDataInsert(movie['director'], series.data['cast'], newFilmID)
            print("Films added to DB")
    except:
        print("Films NOT added to DB")
def getGenresID(genresList):
    con = createConnection()
    cur = con.cursor()
    for i in range(len(genresList)):
        if genresList[i] == "Sci-Fi":
            genresList[i] = 'Science Fiction'
    qr = 'SELECT id FROM genres WHERE genre in ({0})'.format(', '.join('%s' for _ in genresList))
    cur.execute(qr, genresList)
    genIDList = cur.fetchall()
    if len(genIDList) != len(genresList):
        genIDList.append((27,))
    print("List genres has been created")
    return genIDList
def genresDataInsert(genresList, filmID):
    con = createConnection()
    cur = con.cursor()
    genIDList = getGenresID(genresList)
    dir = []
    for i in range(len(genIDList)):
        dir.append(
            (genIDList[i][0], filmID)
        )
    sqlFilmGenresJoin = """
    INSERT INTO films_genres (id_genres, id_films) VALUES (%s, %s)"""
    cur.executemany(sqlFilmGenresJoin, dir)
    con.commit()
    print("All genres succeeful added to films_genres")
def peopleDataInsert(directors, cast, filmID):
    ia = imdb.IMDb()
    con = createConnection()
    cur = con.cursor()
    newPeopleList = []
    dictionary = dict((x, y) for y, x in getIDAllPeople())
    for i in directors:
        if str(i) not in dictionary:
            try:
                actor = ia.get_person(i.personID)
                imA = actor['headshot']
                downloadImagesPeop(imA)
                file = open("../Images_People/1.png", 'rb').read()
                file = base64.b64encode(file)
            except:
                file = open("../Images_People/noFoto.png", 'rb').read()
                file = base64.b64encode(file)
            newPeopleList.append((str(i), file))
    for i in cast:
        #and (str(i),) not in newPeopleList
        if str(i) not in dictionary:
            check = 0
            for j in newPeopleList:
                if str(i) in j[0]:
                    check += 1
                    break
            if check == 0:
                try:
                    actor = ia.get_person(i.personID)
                    imA = actor['headshot']
                    downloadImagesPeop(imA)
                    file = open("../Images_People/1.png", 'rb').read()
                    file = base64.b64encode(file)
                except:
                    file = open("../Images_People/noFoto.png", 'rb').read()
                    file = base64.b64encode(file)
                newPeopleList.append((str(i), file))
    sqlAddPeople = """
    INSERT INTO people (fullname, peopleIMG) VALUES (%s, %s) 
    """
    cur.executemany(sqlAddPeople, newPeopleList)
    con.commit()
    print("All  new people succeeful added to people table!")
    filmStatusPeopleJoin(directors,cast, filmID)
def filmStatusPeopleJoin(directors, actors, filmID):
    con = createConnection()
    cur = con.cursor()
    peopleArr = getIDAllPeople()
    dir = []
    dictionary = dict((y, x) for x, y in getIDAllPeople())
    for stri in directors:
        num = dictionary.get(str(stri))
        dir.append(
            (filmID, num, 1)
        )
    for stri in actors:
        num = dictionary.get(str(stri))
        dir.append(
            (filmID, num, 2)
        )
    sqlFilmPeopleJoin = """
    INSERT INTO films_people_status (id_film, id_people, id_status) VALUES (%s,%s,%s)
    """
    cur.executemany(sqlFilmPeopleJoin, dir)
    con.commit()
    print("People and films joined succeeful!")
def getIDAllPeople():
    con = createConnection()
    cur = con.cursor()
    sqlIDAllPeople = """
    SELECT id, fullname FROM people
    """
    cur.execute(sqlIDAllPeople)
    personsData = cur.fetchall()
    return personsData
def getFilmID(name, year):
    con = createConnection()
    cur = con.cursor()
    sqlGetFilmID = """
        SELECT id FROM films WHERE filmname = %s AND releasedata = %s"""
    args = (
        name,
        year
    )
    cur.execute(sqlGetFilmID, args)
    filmID = cur.fetchone()
    return filmID[0]

def getfilmImage():
    con = createConnection()
    cur = con.cursor()
    sqlGetFilm ="""
    SELECT peopleIMG FROM people WHERE id = 11933"""
    cur.execute(sqlGetFilm)
    data = cur.fetchall()
    image = data[0][0]
    binary_data = base64.b64decode(image)
    image = Image.open(io.BytesIO(binary_data))

