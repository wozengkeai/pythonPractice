# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/8 20:01
@Auth ： zengxiaoyan
@File ：whichday.py
"""

from datetime import datetime
def which_day(year,month,day):
    """
    输入年月日判断这个日期是这一年的第几天
    :param year:
    :param month:
    :param day:
    :return:
    """
    end = datetime(year,month,day).date()     #datetime()用指定日期创建时间，date()获取年月日
    start = datetime(year,1,1).date()
    dif = (end-start).days + 1            #.days返回两个日期相差的天数
    print(dif)


if __name__ == '__main__':
    which_day(2022,2,8)