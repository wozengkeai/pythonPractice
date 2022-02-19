# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/19 11:19
@Auth ： zengxiaoyan
@File ：more_than_half.py
"""

"""
写一个函数，若传入一个有若干个整数的列表，该列表中某个元素出现的次数超过了50%，返回这个元素
"""

def more_than_half(items):
    temp = {}
    items_len = len(items)
    for item in items:
        if item not in temp.keys():
            temp.setdefault(item,1)
        else:
            temp[item] += 1
            if temp[item] / items_len > 0.5:
                return item


#LeeCode上这种方法可以，但是结果我感觉不太对
# def more_than_half(items):
#     temp,times = None,0
#     for item in items:
#         if times == 0:
#             temp = item
#             times += 1
#
#         else:
#             if temp == item:
#                 times += 1
#             else:
#                 times -= 1
#     return temp

if __name__ == '__main__':
    items = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(more_than_half(items))

    print(Solution().majorityElement(items))