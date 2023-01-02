from DB_connector import *
import mysql.connector

def addVotesAndScoreUser(idUser, idFilm, score):
    con = createConnection()
    cur = con.cursor()
    sqlAddVotesAndScore = """
    INSERT INTO films_score(id_user, id_films, score) VALUES (%s, %s, %s)"""
    data = (idUser, idFilm, score)
    cur.execute(sqlAddVotesAndScore, data)
    con.commit()
def deleteScoreUser (idUser, idFilm):
    con = createConnection()
    cur = con.cursor()
    sqlDeleteScoreUser = """
    DELETE FROM films_score WHERE id_user = %s AND id_films = %s"""
    data = (idUser, idFilm)
    cur.execute(sqlDeleteScoreUser, data)
    con.commit()
def changeScoreFilmUser(idUser, idFilm, newScore):
    con = createConnection()
    cur = con.cursor()
    sqlChangeScoreFilm = """
    UPDATE films_score SET score= %s WHERE (id_user = %s AND id_films = %s) """
    data = (newScore, idUser, idFilm)
    cur.execute(sqlChangeScoreFilm, data)
    con.commit()