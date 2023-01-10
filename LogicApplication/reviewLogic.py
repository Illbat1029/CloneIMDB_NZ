from LogicApplication.DB_connector import *
import mysql.connector
from datetime import datetime, timedelta
def getLikesListForThisFilmReviews(idFilm):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlGetLikesListForThisFilmID = """
    SELECT rs.id_user, rs.id_review, rs.score FROM films_review
    JOIN review_score rs
    ON films_review.id = rs.id_review
    WHERE id_films = %s;"""
    cur.execute(sqlGetLikesListForThisFilmID, (idFilm,))
    exe = cur.fetchall()
    print("Get all likes review for film = ", datetime.now() - stime)
    return exe

def deleteReviewVoteForThisUser(idUser, idReview, con = createConnection()):
    stime = datetime.now()
    cur = con.cursor()
    sql = """
    DELETE FROM review_score WHERE id_user = %s AND id_review = %s"""
    cur.execute(sql, (idUser, idReview))
    print("Delete vote review = ", datetime.now() - stime)

def updateReviewVoteForThisUser(idUser, idReview, score, con = createConnection()):
    stime = datetime.now()
    cur = con.cursor()
    sql = """
    UPDATE review_score SET score = %s WHERE id_user = %s AND id_review = %s"""
    cur.execute(sql, (score, idUser, idReview))
    print("Update vote review = ", datetime.now() - stime)

def insertReviewVoteForThisUser(idUser, idReview, score, con = createConnection()):
    stime = datetime.now()
    cur = con.cursor()
    sql = """
    INSERT INTO review_score (score, id_user, id_review) VALUES (%s, %s, %s)"""
    cur.execute(sql, (score, idUser, idReview))
    print("Add vote review = ", datetime.now() - stime)

def reviewScoreButton(idUser, idReview, score, likesReviewsListForThisFilm):
    con = createConnection()
    cur = con.cursor()
    check = 0
    for i in likesReviewsListForThisFilm:
        if (i[0] == idUser and i[1] == idReview):
            if (i[2] == score):
                deleteReviewVoteForThisUser(idUser, idReview, con)
                check = 1
                print("Already exists, deleting...")
            elif(i[2] == -score):
                updateReviewVoteForThisUser(idUser, idReview, score, con)
                check = 1
                print("Already exists separate one, updating...")
    if check == 0:
        insertReviewVoteForThisUser(idUser, idReview, score, con)
        print("Not exists, creating...")
    con.commit()

def isExistsReport(idReview, idUser, type_id):
    con = createConnection()
    cur = con.cursor()
    sqlIsReportExists = """    SELECT EXISTS(SELECT * FROM reviews_report WHERE id_review = '%s' AND id_user = '%s' AND type_id = '%s')"""
    cur.execute(sqlIsReportExists, (idReview, idUser, type_id))
    exe = cur.fetchone()
    con.close()
    return exe

def createReportReview(idReview, idUser, type_id):
    con = createConnection()
    cur = con.cursor()
    sqlSentRewiewReport = """    INSERT INTO reviews_report (id_review, id_user, type_id) VALUES (%s, %s, %s)"""
    if (isExistsReport(idReview, idUser, type_id) == (1,)):
        print("Report already exists")
    else:
        cur.execute(sqlSentRewiewReport, (idReview, idUser, type_id))
        con.commit()



def getAllReportTypes():
    con = createConnection()
    cur = con.cursor()
    sqlGetAllReportTypes = """    SELECT * FROM report_types"""
    cur.execute(sqlGetAllReportTypes)
    exe = cur.fetchall()
    return exe