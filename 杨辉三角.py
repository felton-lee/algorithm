#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 杨辉三角.py
@Author: lee
@Date  : 2020/1/13 10:42
@Desc  : map()函数实现
'''


# 最基本
class Solution1:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        numRows -= 2
        rList = [[1], [1, 1]]
        while numRows > 0:
            newList = [1]
            for i in range(len(rList[-1]) - 1):
                newList.append(rList[-1][i] + rList[-1][i + 1])
            newList.append(1)
            rList.append(newList)
            numRows -= 1
        return rList


s1 = Solution1()
for i in s.generate(3):
    print(i)


# 利用map
class Solution2:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        l1 = [[1]]
        n = 1
        while n < numRows:
            res = list(map(lambda x, y: x + y, [0] + l1[-1], l1[-1] + [0]))
            l1.append(res)
            n += 1
        return l1


s2 = Solution2()
for i in s2.generate(4):
    print(i)


# 利用sum和zip
class Solution3:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l1 = [1]
        l2 = []
        n = 0
        while n < numRows:
            l2.append(l1)
            l1 = [sum(t) for t in zip([0] + l1, l1 + [0])]
            n += 1
        return l2


s3 = Solution3()
for i in s3.generate(5):
    print(i)
