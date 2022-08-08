import pymysql

class database:
    def __init__(self,user,password,DB):
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
        pass

    def init_user_check(self):
        pass
