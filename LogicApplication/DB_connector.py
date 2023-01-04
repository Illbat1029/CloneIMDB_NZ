import mysql.connector
from mysql.connector import Error

def createConnection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="34.88.49.141",
            user="root",
            password="Hu@n584217",
            database="dataIMDB"
        )
        #print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def executeQuery(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def executemanyQuery(connection, query, data):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def getDataFromDataBaseExecute (connection, query):
    connection.autocommit = True
    result = None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return result

def getDataFromDataBaseExecutemany (connection, query, data):
    connection.autocommit = True
    result = None
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        result=cursor.fetchall()
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return result
