# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import sys


def method_1():
    """
    循环读取至无数据可获得，用于算法获取数据时
    :return:
    """

    while True:
        line = sys.stdin.readline()

        if not line:
            # 当无值返回时
            break

        lists = list(map(int, str(line).split()))
        print(lists)


if __name__ == '__main__':
    method_1()