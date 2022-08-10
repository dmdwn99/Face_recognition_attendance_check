import pymysql

class database:
    def __init__(self, user, password, DB):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user=user,
            password=password,
            db=DB,
            charset='utf8')
        self.cur = self.conn.cursor()
        print('connect')
    def create_table(self, name, var):
        sql = 'CREATE TABLE ' + name + '(' + var + ');'
        print(sql)
        self.cur.execute(sql)
    def insert_user_info(self):
        #sql = "INSERT INTO user_check (WEEK, USER_ID, DATE_CHECK, CHECK_CHECK) VALUES ('%s', '%s', '%s', '%s')" % (str(week), str(user_id), str(date_check), str(check_check))

        pass

    def init_user_check(self):
        pass
