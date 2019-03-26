#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: jdPrice.py
# @Author: lio
# @Date: 2018-01-29

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import re
import json

from spider_jd.dataProcess import Sql
from spider_jd.model import JdPrice


class jdPrice():
    def __init__(self):
        self.keyword = 'gtx1060'
        self.base_url = "https://search.jd.com/Search?keyword=%s&enc=utf-8&wtype=1" % quote(self.keyword)

    def download_html(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }

        data = requests.get(url, headers=headers).content

        return data

    def download_sub_page(self, sub_url):
        return self.download_html(sub_url)

    # 翻页
    def next_page(self, url):
        self.download_html(url)


    def getSoup(self, soup, attr):
        if soup is None:
            return
        elif attr == 'text':
            return soup.get_text()
        else:
            return soup.get(attr)


    def parse_html(self, html):
        soup = BeautifulSoup(html.decode('utf-8'), 'lxml')
        p_list = soup.find_all('li', attrs={'class': 'gl-item'})
        sql = Sql()
        for i in p_list:
            jdPriceItem = JdPrice()
            p_link = self.getSoup(i.find('div', attrs={'class': 'p-img'}).find('a'), 'href')
            p_title = self.getSoup(i.find('div', attrs={'class': 'p-img'}).find('a'), 'title')
            #p_store_name = i.find('div', attrs={'class': 'p-shop'}).find('a', attrs={'class': 'curr-shop'}).get_text()
            p_store_name = self.getSoup(i.find('div', attrs={'class': 'p-shop'}).find('a', attrs={'class': 'curr-shop'}), 'text')
            sub_url = 'https:%s' % p_link
            #print(sub_url)
            jdPriceItem.p_link = sub_url
            sub_html = self.download_sub_page(sub_url)
            sub_soup = BeautifulSoup(sub_html.decode('gbk', 'ignore'), 'lxml')
            item_info = sub_soup.find('div', attrs={'class': 'product-intro clearfix'}).find('div', attrs={'class': 'itemInfo-wrap'})
            p_name = self.getSoup(item_info.find('div', attrs={'class': 'sku-name'}), 'text').strip()
            #print(p_name)
            jdPriceItem.p_name = p_name
            #print(p_title)
            jdPriceItem.p_title = p_title
            p_detail_li = sub_soup.find('div', attrs={'class': 'p-parameter'}).find('ul', attrs={'class', 'parameter2 p-parameter-list'}).find_all('li')
            p_detail = ''
            for j in p_detail_li:
                p_detail += self.getSoup(j, 'text') + '; '

            #print(p_detail)
            jdPriceItem.p_detail = p_detail
            #print(p_store_name)
            jdPriceItem.p_store_name = p_store_name

            p_comment_num = self.getSoup(i.find('div', attrs={'class': 'p-commit'}).find('strong').find('a'), 'text')
            #print(p_comment_num)
            jdPriceItem.p_comment_num = p_comment_num

            # 价格，ajax回传
            pattern = re.compile(r"(?<=/)\d.+?(?=\.)")
            skuid = re.search(pattern, sub_url)
            # print(skuid.group(0))
            price_url = 'https://p.3.cn/prices/mgets?skuIds=' + skuid.group(0)
            price_data = self.download_html(price_url)
            price_json = json.loads(price_data)
            p_price = price_json[0].get('p')
            #print(p_price)
            jdPriceItem.p_price = p_price
            try:
                jdPriceItem.p_price_plus = price_json[0].get('tpp')
            except:
                jdPriceItem.p_price_plus = ''

            # 图片
            img_url = ''
            try:
                p_img = 'https:' + self.getSoup(i.find('div', attrs={'class': 'p-img'}).find('a').find('img'), 'src')
                print(p_img)
                pattern_img = re.compile(r"(?<=com).+?jpg")
                img_path = re.search(pattern_img, p_img)
                img_url = 'imgs/' + img_path.group(0).replace('/', '')
                img_file = open(img_url, 'wb')
                img_file.write(requests.get(p_img).content)
                img_file.close()
            except:
                pass
            jdPriceItem.p_img = img_url
            # sql.insert_jdPrice(jdPriceItem)

        sql.close()


    def main(self):
        i = 1
        while i < 2:
            print("第%d页" % i)
            next_url = self.base_url + '&page=' + str(i)
            data = self.download_html(next_url)
            self.parse_html(data)
            i += 2


jdPrice = jdPrice()
jdPrice.main()