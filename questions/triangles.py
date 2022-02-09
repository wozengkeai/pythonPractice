# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/7 23:05
@Auth ： zengxiaoyan
@File ：triangles.py
"""
"""
杨辉三角
第n+1行的第i个数等于第n行的第i-1个数和第i个数之和，这也是组合数的性质之一。即 C(n+1,i)=C(n,i)+C(n,i-1)。
"""
def triangles(n):
    line = []
    for i in range(n):
        pass