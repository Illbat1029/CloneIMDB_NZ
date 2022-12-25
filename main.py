from DB_connector import *

sql = """INSERT INTO user (uname, pass, email) VALUES (%s, %s, %s)"""
data = [
    ("soso", "654321", "maks@gmail.com"),
    ("Nsisi", "123456", "nikita@gmail.com")
]
sqlGet = """SELECT * FROM user"""
executemanyQuery(createConnection(),sql,data)
#$sdfsdfsdfsdfsdfsd
#fsdfsdfsdfsdfsdf
#dsfgdfsdfsdfsd
dataDB = getDataFromDataBaseExecute(createConnection(),sqlGet)

for i in dataDB:
    print(i)
