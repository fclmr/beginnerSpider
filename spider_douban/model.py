#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: model.py
# @Author: lio
# @Date: 2018-01-26

class Top250():
    # 电影链接
    @property
    def movie_links(self):
        return self._movie_links

    @movie_links.setter
    def movie_links(self, value):
        self._movie_links = value

    # 电影名
    @property
    def movie_names(self):
        return self._movie_names

    @movie_names.setter
    def movie_names(self, value):
        self._movie_names = value

    # 电影制作（类型，与制作人员）
    @property
    def movie_create(self):
        return self._movie_create

    @movie_create.setter
    def movie_create(self, value):
        self._movie_create = value

    # 评分
    @property
    def movie_score(self):
        return self._movie_score

    @movie_score.setter
    def movie_score(self, value):
        self._movie_score = value

    # 评价人数
    @property
    def movie_comment_num(self):
        return self._movie_comment_num

    @movie_comment_num.setter
    def movie_comment_num(self, value):
        self._movie_comment_num = value

    # 点评
    @property
    def movie_quote(self):
        return self._movie_quote

    @movie_quote.setter
    def movie_quote(self, value):
        self._movie_quote = value