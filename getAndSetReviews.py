from DB_connector import *
import mysql.connector
class userReview:
    def __init__(self, idUser, uname, filmname, review, score):
        self.idUser = idUser
        self.username = uname
        self.filmname = filmname
        self.review = review
        self.scoreReview = score
def isExistRivew(idUser, idFilm):
    con = createConnection()
    cur = con.cursor()
    sqlExistReview="""
    SELECT EXISTS (SELECT id FROM films_review WHERE id_user = %s AND id_films = %s)  
    """
    data = (idUser, idFilm)
    cur.execute(sqlExistReview, data)
    isExist = cur.fetchone()
    isExist = isExist[0]
    return (isExist)
def addReview(idUser, idFilm, review):
    con = createConnection()
    cur = con.cursor()
    sqlAddReview = """
    INSERT INTO films_review (id_user, id_films, review, score) 
    VALUES (%s, %s, %s, %s)"""
    data = (idUser, idFilm, review, 0)
    if(isExistRivew(idUser, idFilm)!=1):
        cur.execute(sqlAddReview, data)
        con.commit()
    else:
        print("Review is allredy exist!")

def changeRivewText (idUser, idFilm, review):
    con = createConnection()
    cur = con.cursor()
    sqlChangeReview = """
    UPDATE films_review SET review = %s WHERE id_user = %s AND id_films = %s"""
    data = (review, idUser, idFilm)
    if(isExistRivew(idUser, idFilm)==1):
        cur.execute(sqlChangeReview, data)
        con.commit()
    else:
        print("Review is not exist!")
def deleteReview (idUser, idFilm):
    con = createConnection()
    cur = con.cursor()
    sqlDeleteReview = """
    DELETE FROM films_review WHERE id_user = %s AND id_films = %s"""
    data = (idUser, idFilm)
    if(isExistRivew(idUser, idFilm)==1):
        cur.execute(sqlDeleteReview, data)
        con.commit()
    else:
        print("Review is not exist!")

def getAllReviewsUser(idUser):
    con = createConnection()
    cur = con.cursor()
    sqlGetAllReviewUser = """
    SELECT id_user, filmname, review, films_review.score FROM films_review
    JOIN films
    ON films_review.id_films = films.id
    WHERE id_user = %s
    """
    data = (idUser, )
    cur.execute(sqlGetAllReviewUser, data)
    allReview = cur.fetchall()
    dataRet = []
    for row in allReview:
        buff = list(row)
        uReview = userReview(buff[0], "BRAK" ,buff[1], buff[2], buff[3])
        dataRet.append(uReview)
    return dataRet
def getAllReviewsForFilm(idFilm):
    con = createConnection()
    cur = con.cursor()
    sqlGetAllReviewFilm = """
     SELECT id_user, username, filmname, review, films_review.score FROM films_review
     JOIN films
     ON films_review.id_films = films.id
     JOIN user
     ON films_review.id_user = user.id
     WHERE id_films=%s"""
    data = (idFilm, )
    cur.execute(sqlGetAllReviewFilm, data)
    allReview = cur.fetchall()
    dataRet = []
    for row in allReview:
        buff = list(row)
        uReview = userReview(buff[0], buff[1], buff[2], buff[3], buff[4])
        dataRet.append(uReview)
    return dataRet