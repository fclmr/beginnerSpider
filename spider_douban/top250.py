#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: top250.py
# @Author: lio
# @Date: 2018-01-26

import requests
from bs4 import BeautifulSoup
import re

from spider_douban.dataProcess import Sql
from spider_douban.model import Top250

class Top250Spider():
    url = 'https://movie.douban.com/top250'
    movies = []

    # 下载页面
    def download_page(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        data = requests.get(url, headers=headers).content

        return data

    # 翻页
    def next_page(self, soup):
        try:
            next_url = self.url + soup.find('div', attrs={'class': 'paginator'}).find('span', attrs={'class': 'next'}).find('a').get('href')
            next_html = self.download_page(next_url)
            self.parse_html(next_html)
        except:
            pass

    # 输出
    def parse_html(self, html):
        soup = BeautifulSoup(html, "lxml")
        movie_list = soup.find('ol', attrs={'class': 'grid_view'})
        for li in movie_list.find_all('li'):
            top250 = Top250()
            hd = li.find('div', attrs={'class': 'hd'})
            # 电影链接
            top250.movie_link = hd.find('a').get('href')
            # 电影名
            movie_names = ''
            for movie_name in hd.find_all('span', attrs={'class': 'title'}):
                movie_names += movie_name.get_text()

            for movie_name in hd.find_all('span', attrs={'class': 'other'}):
                movie_names += movie_name.get_text()
            top250.movie_names = movie_names

            bd = li.find('div', attrs={'class': 'bd'})
            # 电影制作(类型，与制作人员)
            movie_create = bd.find('p').get_text().strip()
            top250.movie_create = movie_create
            # 评分
            top250.movie_score = bd.find('div', attrs={'class': 'star'}).find('span', attrs={'class': 'rating_num'}).get_text()
            # 评价人数
            top250.movie_comment_num = bd.find('div', attrs={'class': 'star'}).find('span', text=re.compile("评价")).get_text()

            # 点评
            movie_quote = ''
            try:
                movie_quote = bd.find('p', attrs={'class': 'quote'}).find('span', attrs={'class': 'inq'}).get_text()
            except AttributeError:
                pass
            top250.movie_quote = movie_quote
            self.movies.append(top250)

        self.next_page(soup)

    def main(self):
        html = self.download_page(self.url)
        self.parse_html(html)
        sql = Sql()
        for movie in self.movies:
            sql.insert_top250(movie)

top250Spider = Top250Spider()
top250Spider.main()