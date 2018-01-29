#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: Test.py
# @Author: lio
# @Date: 2018-01-29
from spider_douban.model import Top250

top250 = Top250()

top250.movie_link = '链接'

print(top250.movie_link)