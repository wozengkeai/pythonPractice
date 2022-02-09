# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/7 23:09
@Auth ： zengxiaoyan
@File ：fibonacci.py
"""
"""
斐波拉契数列：除了第一和第二个数，后面的数都是前两个数相加而得
1,1,2,3,5,8,13...
"""

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        i += 1
        print(a)



if __name__ == '__main__':
        fibonacci(10)