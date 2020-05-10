# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


class Vector3d:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def length(self):
        return (self.__x**2 + self.__y**2 + self.__z**2) ** 0.5

    # 请在这里增加3个特殊方法，分别用来支持加法运算符、减法运算符以实现两个三维向量间的加法和减法运算，以及打印函数print()
    	#********** Begin *********#
    def __str__(self):


    def __add__(self, v):
        return self

    def __sub__(self, v):


    	#********** End *********#
x1, y1, z1 = map(int, input().split(','))
x2, y2, z2 = map(int, input().split(','))

v1 = Vector3d(x1, y1, z1)
v2 = Vector3d(x2, y2, z2)

print(v1 + v2)
print(v1 - v2)