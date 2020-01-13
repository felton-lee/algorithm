#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 生消模型.py
@Author: lee
@Date  : 2020/1/13 11:09
@Desc  : 生成器实现生消模型
'''


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
