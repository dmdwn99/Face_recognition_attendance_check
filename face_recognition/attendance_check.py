import pymysql, datetime
import database

def check(id):
    db = database.database('root', 'rkddmdwn99', 'soloDB')
    now = datetime.datetime.now()
    date = str(now.date())
    user_id = str(id)
    sql = "UPDATE user_check SET check_check = 'O' WHERE user_id = '%s' AND date_check = '%s'" %(user_id, date)
    db.cur.execute(sql)
    db.conn.commit()
    sql = "SELECT * FROM user_check WHERE check_check = 'O'"
    db.cur.execute(sql)
    res = db.cur.fetchall()
    print(res)

