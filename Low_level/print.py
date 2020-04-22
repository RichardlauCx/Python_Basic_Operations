# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import time


def print_triangle():
    """
    图形可以先画出来，再去寻找规律
    规律：空格一行比一行少；
        符号一奇数排列
    :return: None
    """
    n = int(input())
    for i in range(n):
        line = " " * (n - 1 - i) + "@" * (2 * i + 1)
        print(line)


if __name__ == '__main__':
    # print_triangle()

    print(time.strftime("%Y-%m-%d %X", time.localtime()))
