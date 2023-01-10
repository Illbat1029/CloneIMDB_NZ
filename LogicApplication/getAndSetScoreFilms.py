from LogicApplication.DB_connector import *
import mysql.connector
from datetime import datetime, timedelta

def addVotesAndScoreUser(idUser, idFilm, score):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlAddVotesAndScore = """
    INSERT INTO films_score(id_user, id_films, score) VALUES (%s, %s, %s)"""
    data = (idUser, idFilm, score)
    cur.execute(sqlAddVotesAndScore, data)
    con.commit()
    print("Add vote for film = ", datetime.now() - stime)
def deleteScoreUser (idUser, idFilm):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlDeleteScoreUser = """
    DELETE FROM films_score WHERE id_user = %s AND id_films = %s"""
    data = (idUser, idFilm)
    cur.execute(sqlDeleteScoreUser, data)
    con.commit()
    print("Delete score user = ", datetime.now() - stime)
def changeScoreFilmUser(idUser, idFilm, newScore):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlChangeScoreFilm = """
    UPDATE films_score SET score= %s WHERE (id_user = %s AND id_films = %s) """
    data = (newScore, idUser, idFilm)
    cur.execute(sqlChangeScoreFilm, data)
    con.commit()
    print("Change score user = ", datetime.now() - stime)
def selectScoreFromDB(idUser, idFilm):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlChangeScoreFilm = """
    SELECT score FROM films_score WHERE(id_user = %s AND id_films = %s)"""
    data = (idUser, idFilm)
    cur.execute(sqlChangeScoreFilm, data)
    x=cur.fetchall()
    print("Select score dla filma = ", datetime.now() - stime)
    return x