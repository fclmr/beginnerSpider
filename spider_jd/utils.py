#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# @File: utils.py
# @Author: lio
# @Date: 2018-02-05

class Utils():
    def none2String(value):
        if value is None:
            return ''
        else:
            return value