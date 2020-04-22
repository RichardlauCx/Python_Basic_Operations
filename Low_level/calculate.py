# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def calculate1():
    x = float(input())
    a = 2
    b = -45
    c = 13
    y = a * x**2 + b*x + c
    return x, y


if __name__ == '__main__':
    result = calculate1()
    print(result[0], result[1])
