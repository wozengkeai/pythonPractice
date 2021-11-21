# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/1 15:19
@Auth ： zengxiaoyan
@File ：panic.py
"""
"""
将字符串Don't panic!转换为字符串on tap
"""
#1、列表的几个用法append,insert,remove,extend,pop
# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)
# plist.pop(0)
# for i in range(4):
#     plist.pop()
# for i in plist:
#     if i.isalpha() == False:
#         plist.remove(i)
# plist.insert(3,plist.pop())
# plist.insert(2,' ')
# new_phrase = ''.join(plist)  #列表转为字符串
# print(plist)
# print(new_phrase)



#切片,切片不改变原有列表的数据
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3])  #列表转为字符串
new_phrase = new_phrase + ''.join(plist[5],plist[4],plist[7],plist[6])
print(plist)
print(new_phrase)