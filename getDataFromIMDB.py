import base64
from PIL import Image
import io
import imdb
from imdb import Cinemagoer
import requests
import urllib
import os
from DB_connector import *
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
    isExist=cur.fetchone()
    isExist=isExist[0]
    return isExist
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
def downloadImages(imURL):
    urllib.request.urlretrieve(imURL, "Images_Film/1.png")
def getDataFilmIMDB():
    ia = imdb.IMDb()
    ib = Cinemagoer()
    for i in range(30):
        a= 111161+i
        code ="0"+str(a)
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
            year = series.data['year']
    # runtime
            runtimes = series.data['runtimes'][0]
    # director
            directorS = ""
            try:
                for director in movie['director']:
                    directorS = directorS + str(director) + ";"
            except:
                directorS = ""
    # actor
            cast = ""
            c = series.data['cast']
            for i in range(len(c)):
                cast = cast + str(c[i]) + ";"
    # images
            cover = series.data['cover url']
            downloadImages(cover)
            if directorS == "":
                directorS = "BRAK"
            if existFilmDatabase(str(series), year)!=1:
                createFilm(str(series), outline, country, genre, lang, year, runtimes, 0, 0, directorS, cast)
                #ADD METHOD TO ADD GENRES FILMS DB TABLE
                #ADD METHOD TO HUMANS (MINECRAFT xd) FILMS DB TABLE
                print("ZAJEBOK!")
        except:
            print("HUJNIA")
            continue
def getfilmImage():
    con = createConnection()
    cur = con.cursor()
    sqlGetFilm ="""
    SELECT picture FROM films WHERE id = 1"""
    cur.execute(sqlGetFilm)
    data = cur.fetchall()
    image = data[0][0]
    binary_data = base64.b64decode(image)
    image = Image.open(io.BytesIO(binary_data))

