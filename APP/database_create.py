import sqlite3
from datetime import datetime

def create_db():
    cursor.execute("""CREATE TABLE student(id integer PRIMARY KEY,
    name VARCHAR(50), date DATE, time TIME, attendance integer)""")

def insert_db():
    cursor.execute()


con = sqlite3.connect('../DB/student.db')
cursor = con.cursor()
now = datetime()



