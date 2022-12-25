from DB_connector import *

sql = """INSERT INTO user (uname, pass, email) VALUES (%s, %s, %s)"""
data = [
    ("helpme", "654321", "mhm@gmail.com"),
    ("Sus", "123456", "sus@gmail.com")
]
sqlGet = """SELECT * FROM user"""
#executemanyQuery(createConnection(),sql,data)
dataDB = getDataFromDataBaseExecute(createConnection(),sqlGet)

for i in dataDB:
    print(i)
