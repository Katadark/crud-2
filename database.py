import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lima9102",
    database="dealership"
)

def get_db():
    return db
