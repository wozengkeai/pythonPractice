# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/9 21:32
@Auth ： zengxiaoyan
@File ：recordTime.py
"""
#记录函数执行时间的装饰器

from functools import wraps
from time import time



def record_time(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time()
        result = func(*args,**kwargs)
        print(f'执行时间: {time() - start}')
        return result

    return wrapper

@record_time
def walkFile():
    pass

if __name__ == '__main__':
    walkFile()