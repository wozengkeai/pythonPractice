# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/19 14:41
@Auth ： zengxiaoyan
@File ：list_depth.py
"""
from typing import List

"""
写一个函数，传入的参数是一个列表（列表的元素可能也是一个列表），返回该列表最大的嵌套深度
"""

def list_depth(items: List):
    if isinstance(items, list):
        max_depth = 1
        for item in items:
            max_depth = max(list_depth(item) + 1,max_depth)
        return max_depth
    return 0

if __name__ == '__main__':
    items = [2,[1,2,[1]]]
    print(list_depth(items))

