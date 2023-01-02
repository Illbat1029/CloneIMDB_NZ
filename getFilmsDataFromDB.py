from DB_connector import *
import mysql.connector
class Film:
    def __init__(self, id=0, filmname="", description="",
                 country="", genres="", language="", release=0,
                 runtime=0, score=0.0, vote=0, director="",
                 actors="", picture=b'/9'):
        self.id = id
        self.name = filmname
        self.description = description
        self.country = country
        self.genres = genres
        self.lang = language
        self.release = release
        self.runtime = runtime
        self.score = score
        self.vote = vote
        self.director = director
        self.actors = actors
        self.images = picture

def createList(data):
    listData = data.split(";")
    listData.remove("")
    return listData

def getListAllDataAllFilms():
    con = createConnection()
    cur = con.cursor()
    sqlGetAllFilms = """
    SELECT * FROM films
    """
    cur.execute(sqlGetAllFilms)
    allFilmData=cur.fetchall()
    dataRet = []
    for row in allFilmData:
        buff = list(row)
        film = Film(buff[0], buff[1], buff[2], createList(buff[3]), createList(buff[4]), createList(buff[5]),
                    buff[6], buff[7], buff[8], buff[9], createList(buff[10]), createList(buff[11]), buff[12])
        dataRet.append(film)
    return dataRet

def getAllUserGenresID(genresList):
    con = createConnection()
    cur = con.cursor()
    for i in range(len(genresList)):
        if genresList[i] == "Sci-Fi":
            genresList[i] = 'Science Fiction'
    qr = 'SELECT id FROM genres WHERE genre in ({0})'.format(', '.join('%s' for _ in genresList))
    cur.execute(qr, genresList)
    genIDList = cur.fetchall()
    return genIDList

def refractoringDataGenresFilm(data):
    retData = []
    for i in data:
        for j in i:
            filmData = Film()
            filmData.id = j[0]
            filmData.name = j[1]
            filmData.country = createList(j[2])
            filmData.genres = createList(j[3])
            filmData.lang = createList(j[4])
            filmData.release = j[5]
            filmData.score = j[6]
            filmData.images = j[7]
            retData.append(filmData)
    return retData

def refractoringDataPeopleFilm(data):
    retData = []
    for j in data:
        filmData = Film()
        filmData.id = j[0]
        filmData.name = j[1]
        filmData.country = createList(j[2])
        filmData.genres = createList(j[3])
        filmData.lang = createList(j[4])
        filmData.release = j[5]
        filmData.score = j[6]
        filmData.images = j[7]
        retData.append(filmData)
    return retData

def refractoringAllDataFilm(data):
    filmData = Film(
    data[0],
    data[1],
    data[2],
    data[3],
    data[4],
    data[5],
    data[6],
    data[7],
    data[8],
    data[9],
    data[10],
    data[11],
    data[12],
    )
    return filmData

def getListAllFilmWithGenresUser(genresList):
    con = createConnection()
    cur = con.cursor()
    genresIDUser = getAllUserGenresID(genresList)
    sqlGetDataFilm ="""
    SELECT films.id, films.filmname, films.country, films.gen, films.language, films.releasedata, films.score, films.picture
    FROM films
    JOIN films_genres
    ON films.id = films_genres.id_films AND films_genres.id_genres = %s
    """
    data = []
    for i in range(len(genresList)):
        cur.execute(sqlGetDataFilm, genresIDUser[i])
        data.append(cur.fetchall())
    data=refractoringDataGenresFilm(data)
    return data

def getListAllFilmsWithPeopleUserAndStatus(peopleFullName):
    con = createConnection()
    cur = con.cursor()
    sqlGetDataFilm = """
    SELECT filmname, status.status_name 
    FROM films
    JOIN films_people_status
    ON films.id = films_people_status.id_film AND (films_people_status.id_people = (SELECT id from people WHERE fullname=%s))
    JOIN status
    ON films_people_status.id_status = status.status_id"""
    cur.execute(sqlGetDataFilm,(peopleFullName,))
    data = cur.fetchall()
    return data

def getListAllFilmsWithPeopleUser(peopleFullName):
    con = createConnection()
    cur = con.cursor()
    sqlGetDataFilm = """
        SELECT films.id, films.filmname, films.country, films.gen, films.language, films.releasedata, films.score, films.picture
        FROM films
        JOIN films_people_status
        ON films.id = films_people_status.id_film AND (films_people_status.id_people = (SELECT id from people WHERE fullname=%s))
        """
    cur.execute(sqlGetDataFilm, (peopleFullName,))
    data = cur.fetchall()
    data=refractoringDataPeopleFilm(data)
    return data

def getAllDataFilmByID(idFilm):
    con = createConnection()
    cur = con.cursor()
    sqlGetAllDataFilm = """
    SELECT * FROM films WHERE id = %s"""
    cur.execute(sqlGetAllDataFilm, (idFilm,))
    data = cur.fetchone()
    data = refractoringAllDataFilm(data)
    return data

def getAllDataFilmByReleaseDataBetween(releaseStart = 0, releaseEnd=3000):
    con = createConnection()
    cur = con.cursor()
    sqlGetAllDataFilm = """
    SELECT films.id, films.filmname, films.country, films.gen, films.language, films.releasedata, films.score, films.picture 
    FROM films 
    WHERE releasedata BETWEEN %s AND %s"""
    cur.execute(sqlGetAllDataFilm, (releaseStart,releaseEnd))
    data = cur.fetchall()
    data = refractoringDataPeopleFilm(data)
    return data

def getAllDataFilmByLanguage(language):
    con = createConnection()
    cur = con.cursor()
    sqlGetAllDataFilm ="""
    SELECT films.id, films.filmname, films.country, films.gen, films.language, films.releasedata, films.score, films.picture 
    FROM films
    WHERE films.language LIKE %s
    """
    parameters = "%"+language+"%"
    cur.execute(sqlGetAllDataFilm, (parameters,))
    data=cur.fetchall()
    data = refractoringDataPeopleFilm(data)
    return data

def getAllDataFilmByCountry(country):
    con = createConnection()
    cur = con.cursor()
    sqlGetAllDataFilm = """
        SELECT films.id, films.filmname, films.country, films.gen, films.language, films.releasedata, films.score, films.picture 
        FROM films
        WHERE films.country LIKE %s
        """
    parameters = "%"+country+"%"
    cur.execute(sqlGetAllDataFilm, (parameters,))
    data = cur.fetchall()
    data = refractoringDataPeopleFilm(data)
    return data

def getAllDataFilmByScoreBetween(scoreStart = 0, scoreEnd = 5):
    con = createConnection()
    cur = con.cursor()
    sqlGetAllDataFilm="""
    SELECT films.id, films.filmname, films.country, films.gen, films.language, films.releasedata, films.score, films.picture 
    FROM films 
    WHERE score BETWEEN %s AND %s
    """
    cur.execute(sqlGetAllDataFilm,(scoreStart,scoreEnd))
    data = cur.fetchall()
    data = refractoringDataPeopleFilm(data)
    return data

def getUsersFavoriteFilms(id_user):
    con = createConnection()
    cur = con.cursor()
    exe = []
    sqlGetUsersFavorite = """
    SELECT id_films FROM favorite_films WHERE id_user = %s"""
    cur.execute(sqlGetUsersFavorite, (id_user,))
    exe.append(cur.fetchall())
    output = []
    for i in exe:
        for j in range(len(i)):
            output.append(exe[0][j][0])
    return output
def getUsersWatchedFilms(id_user):
    con = createConnection()
    cur = con.cursor()
    sqlGetUsersWatched = """   
    SELECT id_films FROM watched_films WHERE id_user = %s"""
    exe = []
    cur.execute(sqlGetUsersWatched, (id_user,))
    exe.append(cur.fetchall())
    output = []
    for i in exe:
        for j in range(len(i)):
            output.append(exe[0][j][0])
    return output
def getUsersWatchLaterFilms(id_user):
    con = createConnection()
    cur = con.cursor()
    sqlGetUsersWatch_later = """
    SELECT id_films FROM watchlater_films WHERE id_user = %s"""
    exe = []
    cur.execute(sqlGetUsersWatch_later, (id_user,))
    exe.append(cur.fetchall())
    output = []
    for i in exe:
        for j in range(len(i)):
            output.append(exe[0][j][0])
    return output
def addUserFavoriteFilm(id_user, id_film, userFavoriteFilmList, userWatchedFilmList, userWatchLaterFilmList):
    con = createConnection()
    cur = con.cursor()
    sqlAddToFavoriteFilms = """
    INSERT INTO favorite_films (id_user, id_films) VALUES (%s, %s)"""
    if id_film in userFavoriteFilmList:
        #ОБЕСЦВЕТИТЬ КНОПКУ FAVORITE
        print("Already in FavoriteFilm, deleting")
        sqlRemoveFromFavoriteFilms = """
        DELETE FROM favorite_films WHERE id_user = %s AND id_films = %s"""
        cur.execute(sqlRemoveFromFavoriteFilms, (id_user, id_film))
        con.commit()
    elif id_film in userWatchedFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHED/ЗАКРАСИТЬ КНОПКУ FAVORITE
        print("Already in WatchedFilm, deleting")
        sqlRemoveFromWatchedFilms = """
        DELETE FROM watched_films WHERE id_user = %s AND id_films = %s"""
        cur.execute(sqlRemoveFromWatchedFilms, (id_user, id_film))
        cur.execute(sqlAddToFavoriteFilms, (id_user, id_film))
        con.commit()
    elif id_film in userWatchLaterFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHE_LATER/ЗАКРАСИТЬ КНОПКУ FAVORITE
        print("Already in Watch LaterFilm, deleting")
        sqlRemoveFromWatchLaterFilms = """
        DELETE FROM watchlater_films WHERE id_user = %s AND id_films = %s"""
        cur.execute(sqlRemoveFromWatchLaterFilms, (id_user, id_film))
        cur.execute(sqlAddToFavoriteFilms, (id_user, id_film))
        con.commit()
    else:
        # ЗАКРАСИТЬ КНОПКУ FAVORITE
        print("No such film in users list, adding")
        cur.execute(sqlAddToFavoriteFilms, (id_user, id_film))
        con.commit()

def addUserWatchedFilm(id_user, id_film, userFavoriteFilmList, userWatchedFilmList, userWatchLaterFilmList):
    con = createConnection()
    cur = con.cursor()
    sqlAddToWatchedFilms = """
    INSERT INTO watched_films (id_user, id_films) VALUES (%s, %s)"""
    if id_film in userFavoriteFilmList:
        #ОБЕСЦВЕТИТЬ КНОПКУ FAVORITE/ЗАКРАСИТЬ КНОПКУ WATCHED
        print("Already in FavoriteFilm, deleting")
        sqlRemoveFromFavoriteFilms = """
        DELETE FROM favorite_films WHERE id_user = %s AND id_films = %s"""
        cur.execute(sqlRemoveFromFavoriteFilms, (id_user, id_film))
        cur.execute(sqlAddToWatchedFilms, (id_user, id_film))
        con.commit()
    elif id_film in userWatchedFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHED
        print("Already in WatchedFilm, deleting")
        sqlRemoveFromWatchedFilms = """
        DELETE FROM watched_films WHERE id_user = %s AND id_films = %s"""
        cur.execute(sqlRemoveFromWatchedFilms, (id_user, id_film))
        con.commit()
    elif id_film in userWatchLaterFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHE_LATER/ЗАКРАСИТЬ КНОПКУ WATCHED
        print("Already in Watch LaterFilm, deleting")
        sqlRemoveFromWatchLaterFilms = """
        DELETE FROM watchlater_films WHERE id_user = %s AND id_films = %s"""
        cur.execute(sqlRemoveFromWatchLaterFilms, (id_user, id_film))
        cur.execute(sqlAddToWatchedFilms, (id_user, id_film))
        con.commit()
    else:
        # ЗАКРАСИТЬ КНОПКУ WATCHED
        print("No such film in users list, adding")
        cur.execute(sqlAddToWatchedFilms, (id_user, id_film))
        con.commit()

def addUserWatchLaterFilm(id_user, id_film, userFavoriteFilmList, userWatchedFilmList, userWatchLaterFilmList):
    con = createConnection()
    cur = con.cursor()
    sqlAddToWatchLaterFilms = """
    INSERT INTO watchlater_films (id_user, id_films) VALUES (%s, %s)"""
    if id_film in userFavoriteFilmList:
        #ОБЕСЦВЕТИТЬ КНОПКУ FAVORITE/ЗАКРАСИТЬ КНОПКУ WATCHlater
        print("Already in FavoriteFilm, deleting")
        sqlRemoveFromFavoriteFilms = """
        DELETE FROM favorite_films WHERE id_user = %s AND id_films = %s"""
        cur.execute(sqlRemoveFromFavoriteFilms, (id_user, id_film))
        cur.execute(sqlAddToWatchLaterFilms, (id_user, id_film))
        con.commit()
    elif id_film in userWatchedFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHED/ЗАКРАСИТЬ КНОПКУ WATCHlater
        print("Already in WatchedFilm, deleting")
        sqlRemoveFromWatchedFilms = """
        DELETE FROM watched_films WHERE id_user = %s AND id_films = %s"""
        cur.execute(sqlRemoveFromWatchedFilms, (id_user, id_film))
        cur.execute(sqlAddToWatchLaterFilms, (id_user, id_film))
        con.commit()
    elif id_film in userWatchLaterFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHE_LATER
        print("Already in Watch LaterFilm, deleting")
        sqlRemoveFromWatchLaterFilms = """
        DELETE FROM watchlater_films WHERE id_user = %s AND id_films = %s"""
        cur.execute(sqlRemoveFromWatchLaterFilms, (id_user, id_film))
        con.commit()
    else:
        # ЗАКРАСИТЬ КНОПКУ WatchLater
        print("No such film in users list, adding")
        cur.execute(sqlAddToWatchLaterFilms, (id_user, id_film))
        con.commit()