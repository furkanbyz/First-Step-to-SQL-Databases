import mysql.connector

studentdb = mysql.connector.connect(
    user="root",
    host="localhost",
    password="mysql1234",
    database="schooldb"
)
mycursor=studentdb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)