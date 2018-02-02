#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: model.py
# @Author: lio
# @Date: 2018-01-29

class JdPrice():

    # 商品地址
    @property
    def p_link(self):
        return self._p_link

    @p_link.setter
    def p_link(self, value):
        self._p_link = value

    # 商品名
    @property
    def p_name(self):
        return self._p_name

    @p_name.setter
    def p_name(self, value):
        self._p_name = value

    # 商品标题
    @property
    def p_title(self):
        return self._p_title

    @p_title.setter
    def p_title(self, value):
        self._p_title = value

    # 商品介绍
    @property
    def p_detail(self):
        return self._p_detail

    @p_detail.setter
    def p_detail(self, value):
        self._p_detail = value

    # 商店名
    @property
    def p_store_name(self):
        return self._p_store_name

    @p_store_name.setter
    def p_store_name(self, value):
        self._p_store_name = value

    # 评论数
    @property
    def p_comment_num(self):
        return self._p_comment_num

    @p_comment_num.setter
    def p_comment_num(self, value):
        self._p_comment_num = value

    # 价格
    @property
    def p_price(self):
        return self._p_price

    @p_price.setter
    def p_price(self, value):
        self._p_price = value


