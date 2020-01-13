#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 菲波那切数列.py
@Author: lee
@Date  : 2020/1/13 10:43
@Desc  : 生成器实现
'''


# 生成器斐波那契数列

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


for i in fib(10):
    print(i)

f = fib(6)
while True:
    try:
        value = next(f)
        print(value)
    except StopIteration as e:
        print(e.value)
        break
