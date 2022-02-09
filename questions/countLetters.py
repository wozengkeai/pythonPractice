# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/8 10:46
@Auth ： zengxiaoyan
@File ：countLetters.py
"""

#写一个函数统计传入的列表中每个数字出现的次数并返回对应的字典

def count_letters(items):
    result = {}

    for item in items:
        if isinstance(item,(int,float)):
            result[item] = result.get(item,0) + 1
    print(result)
    return result


if __name__ == '__main__':
    letters = [1,2,1,2,'abc']
    count_letters(letters)