import pymysql

class Sql():

    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',  # MYSQL_HOSTS,
            db='spider',  # MYSQL_DB,
            user='root',  # MYSQL_USER,
            passwd='root',  # MYSQL_PASSWORD,
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def insert_jdPrice(self, item):
        pass