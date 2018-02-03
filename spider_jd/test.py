#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: test.py
# @Author: lio
# @Date: 2018-01-30

import urllib

# print(urllib.parse.quote("https://search.jd.com/Search?keyword=ikbc c87&enc=utf-8&wtype=1"))

import re

key = r"<html><body><h1>hello world<h1></body></html>"
p1 = r"(?<=<h1>).+?(?=<h1>)"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1, key)
print(matcher1.group(0))

key = r"javapythonhtmlvhdl"
p1 = r"python"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1, key)
print(matcher1.group(0))

key = r"<h1>hello world</h1>"
p1 = r"<h1>.+</h1>"
pattern1 = re.compile(p1)
print(pattern1.findall(key))

key = r"lasidf410330978@qq.comsafa"
p1 = r"lasidf410330978@qq\.comsafa"
pattern1 = re.compile(p1)
print(pattern1.findall(key))

key = r"https://item.jd.com/3491230.html?dist=jd' and https://baidu.com"
p1 = r"https*://"
pattern1 = re.compile(p1)
print(pattern1.findall(key))

key = r"lalala<hTml>hello</Html>heihei"
p = r"<[Hh][Tt][Mm][Ll]>.+?</[Hh][Tt][Mm][Ll]"
pattern = re.compile(p)
print(pattern.findall(key))

key = r"mat cat hat pat"
p = r"[^p]at"
pattern = re.compile(p)
print(pattern.findall(key))

key = r"https://item.jd.com/3491230.html?dist=jd"
p = r"(?<=/)\d.+?(?=\.)"
pattern = re.compile(p)

print(pattern.findall(key))

