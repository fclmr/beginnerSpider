import pymysql

class Sql(object):

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

    def insert_jdPrice(self, jd_price):

        try:
            self.cursor.execute("""insert into jd_item(p_link, p_name, p_title, p_detail, p_store_name, p_comment_num, p_price, p_price_plus) values (%s, %s, %s, %s, %s, %s, %s, %s)""" ,
                                (
                                    jd_price.p_link,
                                    jd_price.p_name,
                                    jd_price.p_title,
                                    jd_price.p_detail,
                                    jd_price.p_store_name,
                                    jd_price.p_comment_num,
                                    jd_price.p_price,
                                    jd_price.p_price_plus
                                ))

            self.connect.commit()
        except:
            self.connect.rollback()
            print('插入数据库失败！')
            print("false")


    def close(self):
        self.cursor.close()
        self.connect.close()