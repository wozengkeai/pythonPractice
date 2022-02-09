# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/7 11:23
@Auth ： zengxiaoyan
@File ：singleton.py
"""
from functools import wraps

"""
如何实现单例模式?
1、类有且仅有一个特殊类型的对象
2、为唯一对象提供访问点，令其可以被全局访问
3、控制共享资源的并行访问（通常用于日志记录、数据库连接、打印机后台程序）
"""

#1、经典单例模式

class singleton(object):
    def __new__(cls, name):
        if not hasattr(cls,'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self,name):
        self.name = name


#2、使用装饰器
def singleton2(cls):
    instances = {}

    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]

    return wrapper

@singleton2
class President:
    pass




if __name__ == '__main__':
    s1 = singleton('abid')
    print(s1.name)