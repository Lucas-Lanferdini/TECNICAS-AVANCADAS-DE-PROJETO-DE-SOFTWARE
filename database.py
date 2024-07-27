import mysql.connector

def connect_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="sys"
    )
    print(db)
    return db

def get_cursor(db):
    return db.cursor()
