from DB_connector import *
import mysql.connector
import bcrypt


def AuthenticateUser (login, password):
    sqlAuthenticateUser = """
    SELECT * FROM user WHERE username = %s AND password = %s
    """
    s = """SELECT * FROM user"""
    r = getDataFromDataBaseExecute(createConnection(),s)
    for i in r:
        print(i)
    con = createConnection()
    cur = con.cursor()
    cur.execute(sqlAuthenticateUser,[(login), (password)])
    a = cur.fetchall()
    if a:
        return True
    return False
def RegistrationUser():
    return True
