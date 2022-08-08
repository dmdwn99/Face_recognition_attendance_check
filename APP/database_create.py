import sqlite3

class database:
    def create_db(count):
        cursor.execute("""CREATE TABLE %s(id integer PRIMARY KEY,
        name VARCHAR(50),attendance integer)""", "student"+str(count))

    def insert_db(id, name):
        cursor.execute()


con = sqlite3.connect('../DB/student.db')
cursor = con.cursor()



