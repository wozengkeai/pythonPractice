# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/8 17:04
@Auth ： zengxiaoyan
@File ：changemoney.py
"""
from functools import lru_cache


@lru_cache
def change_money(total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    return change_money(total-2) + change_money(total-3) + change_money(total-5)


if __name__ == '__main__':
    print(change_money(6))