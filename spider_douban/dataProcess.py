#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: dataProcess.py
# @Author: lio
# @Date: 2018-01-29
import MySQLdb


class Sql(object):
    def __init__(self):
        self.connect = MySQLdb.connect(
            host='127.0.0.1',  # MYSQL_HOSTS,
            db='spider',  # MYSQL_DB,
            user='root',  # MYSQL_USER,
            passwd='root',  # MYSQL_PASSWORD,
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def insert_top250(self, top250):
        try:
            self.cursor.execute("""insert into douban_top250(movie_link, movie_names, movie_create, movie_score, movie_comment_num, movie_quote) values (%s, %s, %s, %s, %s, %s)""",
                                (top250.movie_link,
                                 top250.movie_names,
                                 top250.movie_create,
                                 top250.movie_score,
                                 top250.movie_comment_num,
                                 top250.movie_quote
                                ))
            self.connect.commit()
        except Exception as error:
            print(error)
        finally:
            self.cursor.close()
            self.connect.close()
