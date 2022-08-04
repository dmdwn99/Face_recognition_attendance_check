from db_model.mysql import conn_mysqldb

mysql_db = conn_mysqldb()
db_cursor = mysql_db.cursor()
SQL = "SELECT * FROM user_check WHERE USER_ID = '" + str(number) + "'"
db_cursor.execute(sql)
        
def get(number):
    mysql_db = conn_mysqldb()
    db_cursor = mysql_db.cursor()
    sql = "SELECT * FROM user_check WHERE USER_ID = '" + str(number) + "'"
    db_cursor.execute(sql)
    user = db_cursor.fetchone()
    if not user:
        return None

    user = User(number=user[0], user_id=user[1], user_pw=user[2])
    return user

    @staticmethod
    def find(user_id, user_pw):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_ID = '" + \
            str(user_id) + "' AND USER_PW = '" + \
            str(user_pw) + "'"
        # print (sql)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None

        user = User(number=user[0], user_id=user[1], user_pw=user[2])
        return user