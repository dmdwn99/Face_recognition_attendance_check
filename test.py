import datetime as dt
x = dt.datetime.now()

print(x.date(),type(x.date()))
date = str(x.date())
print(date,type(date))


class attendance_check:
    def __init__(self, user, password):
        self.conn = pymysql.connect(host='127.0.0.1', user=user, password=password, db=DB, charset='utf8')
        self.cur = self.conn.cursor()
        print('connect')
    def check(self):
        con = sqlite3.connect('../DB/student.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student WHERE id = %d", self.id)
        self.id = cursor.fetchone()


