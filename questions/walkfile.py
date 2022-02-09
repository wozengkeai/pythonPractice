# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/8 11:22
@Auth ： zengxiaoyan
@File ：walkfile.py
"""
import os

"""
遍历一个文件夹
os模块的walk函数提供了遍历一个文件夹的功能
"""

def walkFile():
    filepath = 'F:\\testerZ\pythonDemo'

    for root,dirs,files in os.walk(filepath,topdown=True):
        """
        root:当前正在访问的文件夹路径
        dirs:该文件夹下的子目录列表
        files:该文件夹下的文件列表
        """
        for d in dirs:
            print(os.path.join(root,d))
        for f in files:
            print(os.path.join(root,f))

if __name__ == '__main__':
    walkFile()