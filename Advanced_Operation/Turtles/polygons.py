# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import turtle


def temp(n):
    # 实现多边形
    # 多边形的内角和为180° * (n-2)
    # 多边形的外角和为360°
    t = turtle.Turtle()

    for freq in range(n):
        corner = 360 / n
        t.forward(60)
        t.right(corner)

    turtle.done()


if __name__ == '__main__':
    n = int(input())
    temp(n)
