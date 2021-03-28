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

    # print(time.strftime("%Y-%m-%d %X", time.localtime()))
    # print("{1:^2}{2:{0}^10}{3:{0}^6}{4:{0}^4}".format("　", "排名", "学校", "省市", "总分"))
    print("{3:^10}".format("　", "排名", "学校", "省市", "总分"))