from DB_connector import *

sql = """INSERT INTO user (uname, pass, email) VALUES (%s, %s, %s)"""
data = [
    ("Maks", "654321", "maks@gmail.com"),
    ("Nikita", "123456", "nikita@gmail.com")
]
sqlGet = """SELECT * FROM user"""
executemanyQuery(createConnection(),sql,data)
dataDB = getDataFromDataBaseExecute(createConnection(),sqlGet)

for i in dataDB:
    print(i)
