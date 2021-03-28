# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import math
import turtle

"""
偶：尖角和-360°
奇：尖角和-180°

偶数又分为：
8、12、16 ---> 规律：可以被四整除
6、10、14 ---> 规律：不可以被四整除

棱角分明的正n角形锐顶角w
w = 180 / n (n为奇数)
w = 360 / n (n为偶数)
统一公式：w = 90/n * (3+(-1)^n)
"""


def temp(n, size):
    """
    # 实现多角形
    :param n: 角的数量
    :param size: 每一边的长度
    :return: None
    """
    t = turtle.Turtle()
    t.speed(1)

    if n % 2 != 0:
        for freq in range(n):
            corner = 180 * (n - 1) / n  # 转角大小
            # print(corner)
            t.forward(200)
            t.right(corner)

    elif n % 2 == 0:
        if n % 4 == 0:
            corner = 180 - 360 / n  # 顶角的补角
            # assert half == int, "not int"

            for freq in range(n):
                # corner = 148
                # print(corner)
                # print(n)
                t.forward(200)
                t.right(corner)

        elif n == 6:
            # 默认会出现重叠现象 （也可向后合并 -> n % 4 != 0）
            half = n / 2  # 分两部分来绘制
            corner = 180 - 360 / n
            interior_corner = 360 / n  # 内顶角

            for freq in range(int(half)):
                # print(corner)
                # print(n)
                t.right(corner)
                t.forward(200)

            t.right(corner)  # 特例实现法
            t.forward(200 / 3)
            t.left(interior_corner)  # 内角除以二
            t.forward(200 / 3)

            for freq in range(int(half)):
                # print(corner)
                # print(n)
                t.right(corner)
                t.forward(200)

        elif n % 4 != 0:
            # 也可以结合多边形来绘制，结合几何算法来实现
            half = n / 2
            corner = 180 - 360 / n
            interior_corner = 360 / n
            # assert half == int, "not int"

            for freq in range(int(half)):
                # print(corner)
                # print(n)
                t.forward(size)
                t.right(corner)

            t.up()
            t.right(interior_corner / 2)
            # 找到新不重叠的顶点（绘图易知）
            distance = size / math.cos(math.radians(interior_corner / 2))  # 根据三角函数来求
            t.forward(distance)
            t.down()

            t.right(180)
            t.left(interior_corner / 2)
            for freq in range(int(half)):
                # print(corner)
                # print(n)

                t.forward(200)
                t.right(corner)

    turtle.done()


if __name__ == '__main__':
    sides = int(input())
    length_side = int(input())
    temp(sides, length_side)
