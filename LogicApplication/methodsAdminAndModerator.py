from LogicApplication.DB_connector import *
import mysql.connector
from LogicApplication.getDataFromIMDB import *
class ReportReview:
    def __init__(self, review, type):
        self.review = review
        self.type = type
def addFilmsAdmin (idFilmStart, idFilmEnd=0):
    if (idFilmEnd == 0):
        idFilmEnd = idFilmStart+1
    addFilmsAdmin(idFilmStart, idFilmEnd)
def splitDataFilmDelete(dataSplit):
    ret = dataSplit.split(",")
    for i in range(len(ret)):
        ret[i]=ret[i].strip()
    return ret
def deleteFilmFromDB (dataWindow):
    con = createConnection()
    cur = con.cursor()
    sqlDeleteFilm = """
    DELETE FROM films WHERE filmname = %s AND releasedata=%s"""
    splitValue = splitDataFilmDelete(dataWindow)
    dataDelete = (splitValue[0], splitValue[1])
    cur.execute(sqlDeleteFilm,dataDelete)
    con.commit()
def getAllReportReviews():
    con = createConnection()
    cur = con.cursor()
    sqlGetAllReportReviews = """
    SELECT review, report_types.type_name FROM admin_review_validation
    JOIN films_review
    ON admin_review_validation.id_review = films_review.id
    JOIN report_types
    ON admin_review_validation.id_report_type = report_types.id
    """
    cur.execute(sqlGetAllReportReviews)
    allReportReviews = cur.fetchall()
    retData = []
    for row in allReportReviews:
        buff = list(row)
        rep = ReportReview(buff[0], buff[1])
        retData.append(rep)
    return retData
def deleteReviewAfterValidation(reviewId):
    con = createConnection()
    cur = con.cursor()
    sqlDeleteReview = """
    DELETE FROM films_review WHERE id = %s
    """
    dataDelete = (reviewId, )
    cur.execute(sqlDeleteReview, dataDelete)
    con.commit()


