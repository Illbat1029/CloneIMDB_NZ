from LogicApplication.DB_connector import *
import mysql.connector
from LogicApplication.getDataFromIMDB import *
from datetime import datetime, timedelta
class ReportReview:
    def __init__(self, id, review, type, username):
        self.reviw_id = id
        self.review = review
        self.type = type
        self.username = username
def addFilmsAdmin (idFilmStart, idFilmEnd=0):
    if (idFilmEnd == 0):
        idFilmEnd = idFilmStart+1
    addFilms(idFilmStart, idFilmEnd)
def splitDataFilmDelete(dataSplit):
    ret = dataSplit.split(",")
    for i in range(len(ret)):
        ret[i]=ret[i].strip()
    return ret
def deleteFilmFromDB (dataWindow):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlDeleteFilm = """
    DELETE FROM films WHERE filmname = %s AND releasedata=%s"""
    splitValue = splitDataFilmDelete(dataWindow)
    dataDelete = (splitValue[0], splitValue[1])
    cur.execute(sqlDeleteFilm,dataDelete)
    con.commit()
    print("Delete film ADMIN = ", datetime.now() - stime)
def getAllReportReviews():
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlGetAllReportReviews = """
    SELECT id_review, review, report_types.type_name, u.username FROM admin_review_validation
    JOIN films_review
    ON admin_review_validation.id_review = films_review.id
    JOIN report_types
    ON admin_review_validation.id_report_type = report_types.id
    JOIN user u 
    ON u.id = films_review.id_user
    """
    cur.execute(sqlGetAllReportReviews)
    allReportReviews = cur.fetchall()
    retData = []
    for row in allReportReviews:
        buff = list(row)
        rep = ReportReview(buff[0], buff[1], buff[2], buff[3])
        retData.append(rep)
    print("Get all review by ADMIN = ", datetime.now() - stime)
    return retData
def deleteReviewAfterValidation(reviewId):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlDeleteReview = """
    DELETE FROM films_review WHERE id = %s
    """
    dataDelete = (reviewId, )
    cur.execute(sqlDeleteReview, dataDelete)
    con.commit()
    print("Delete review after cammit report by ADMIN = ", datetime.now() - stime)
def deleteReviewFromAdminTableWhereReviewGood(reviewId):
    stime = datetime.now()
    con = createConnection()
    cur = con.cursor()
    sqlDeleteReview = """
    DELETE FROM admin_review_validation WHERE id_review = %s
    """
    dataDelete = (reviewId,)
    cur.execute(sqlDeleteReview, dataDelete)
    con.commit()
    print("Delete review after cammit no report by ADMIN = ", datetime.now() - stime)
