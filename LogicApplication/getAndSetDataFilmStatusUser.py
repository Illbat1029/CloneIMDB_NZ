from LogicApplication.DB_connector import *
import mysql.connector

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

#If lists are global: add lists changes into this methods
def insertIntoFavoriteFilms(id_user, id_film, con = createConnection()):
    cur = con.cursor()
    print("Adding into Favorite Films")
    sqlAddToFavoriteFilms = """
        INSERT INTO favorite_films (id_user, id_films) VALUES (%s, %s)"""
    cur.execute(sqlAddToFavoriteFilms, (id_user, id_film))
def deleteFilmFromFavoriteFilms(id_user, id_film, con = createConnection()):
    cur = con.cursor()
    print("Already in FavoriteFilm, deleting")
    sqlRemoveFromFavoriteFilms = """
            DELETE FROM favorite_films WHERE id_user = %s AND id_films = %s"""
    cur.execute(sqlRemoveFromFavoriteFilms, (id_user, id_film))
def insertIntoWatchedFilms(id_user, id_film, con = createConnection()):
    cur = con.cursor()
    print("Adding into Watchd Films")
    sqlAddToWatchedFilms = """
        INSERT INTO watched_films (id_user, id_films) VALUES (%s, %s)"""
    cur.execute(sqlAddToWatchedFilms, (id_user, id_film))
def deleteFilmFromWatchedFilms(id_user, id_film, con = createConnection()):
    cur = con.cursor()
    print("Already in WatchedFilm, deleting")
    sqlRemoveFromWatchedFilms = """
            DELETE FROM watched_films WHERE id_user = %s AND id_films = %s"""
    cur.execute(sqlRemoveFromWatchedFilms, (id_user, id_film))
def insertIntoWatchLaterFilms(id_user, id_film, con = createConnection()):
    cur = con.cursor()
    print("Adding into WatchLater Films")
    sqlAddToWatchLaterFilms = """
        INSERT INTO watchlater_films (id_user, id_films) VALUES (%s, %s)"""
    cur.execute(sqlAddToWatchLaterFilms, (id_user, id_film))
def deleteFilmFromWatchLaterFilms(id_user, id_film, con = createConnection()):
    cur = con.cursor()
    print("Already in Watch LaterFilm, deleting")
    sqlRemoveFromWatchLaterFilms = """
            DELETE FROM watchlater_films WHERE id_user = %s AND id_films = %s"""
    cur.execute(sqlRemoveFromWatchLaterFilms, (id_user, id_film))
def addUserFavoriteFilm(id_user, id_film, userFavoriteFilmList, userWatchedFilmList, userWatchLaterFilmList):
    con = createConnection()
    if id_film in userFavoriteFilmList:
        #ОБЕСЦВЕТИТЬ КНОПКУ FAVORITE
        deleteFilmFromFavoriteFilms(id_user, id_film, con)
    elif id_film in userWatchedFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHED/ЗАКРАСИТЬ КНОПКУ FAVORITE
        deleteFilmFromWatchedFilms(id_user, id_film, con)
        insertIntoFavoriteFilms(id_user, id_film, con)
    elif id_film in userWatchLaterFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHE_LATER/ЗАКРАСИТЬ КНОПКУ FAVORITE
        deleteFilmFromWatchLaterFilms(id_user, id_film, con)
        insertIntoFavoriteFilms(id_user, id_film, con)
    else:
        # ЗАКРАСИТЬ КНОПКУ FAVORITE
        insertIntoFavoriteFilms(id_user, id_film, con)
    con.commit()
def addUserWatchedFilm(id_user, id_film, userFavoriteFilmList, userWatchedFilmList, userWatchLaterFilmList):
    con = createConnection()
    if id_film in userFavoriteFilmList:
        #ОБЕСЦВЕТИТЬ КНОПКУ FAVORITE/ЗАКРАСИТЬ КНОПКУ WATCHED
        deleteFilmFromFavoriteFilms(id_user, id_film, con)
        insertIntoWatchedFilms(id_user, id_film, con)
    elif id_film in userWatchedFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHED
        deleteFilmFromWatchedFilms(id_user, id_film, con)
    elif id_film in userWatchLaterFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHE_LATER/ЗАКРАСИТЬ КНОПКУ WATCHED
        deleteFilmFromWatchLaterFilms(id_user, id_film, con)
        insertIntoWatchedFilms(id_user, id_film, con)
    else:
        # ЗАКРАСИТЬ КНОПКУ WATCHED
        insertIntoWatchedFilms(id_user, id_film, con)
    con.commit()
def addUserWatchLaterFilm(id_user, id_film, userFavoriteFilmList, userWatchedFilmList, userWatchLaterFilmList):
    con = createConnection()
    if id_film in userFavoriteFilmList:
        deleteFilmFromFavoriteFilms(id_user, id_film, con)
        insertIntoWatchLaterFilms(id_user, id_film, con)
    elif id_film in userWatchedFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHED/ЗАКРАСИТЬ КНОПКУ WATCHlater
        deleteFilmFromWatchedFilms(id_user, id_film, con)
        insertIntoWatchLaterFilms(id_user, id_film, con)
    elif id_film in userWatchLaterFilmList:
        # ОБЕСЦВЕТИТЬ КНОПКУ WATCHE_LATER
        deleteFilmFromWatchLaterFilms(id_user, id_film, con)
    else:
        # ЗАКРАСИТЬ КНОПКУ WatchLater
        insertIntoWatchLaterFilms(id_user, id_film, con)
    con.commit()