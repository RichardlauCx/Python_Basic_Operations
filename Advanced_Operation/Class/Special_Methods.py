# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


class Vector3d:
    def __init__(self, x, y, z):
        """
        每个维度为一个私有变量
        :param x:
        :param y:
        :param z:
        """
        self.__x = x
        self.__y = y
        self.__z = z

    # def __init__(self, dimension):
    #     """
    #     通过列表的方式来实现
    #     :param dimension: 向量的维度
    #     """
    #     self.__coords = [0] * dimension

    def length(self):
        return (self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5

    # 请在这里增加3个特殊方法，分别用来支持加法运算符、减法运算符以实现两个三维向量间的加法和减法运算，以及打印函数print()
    # ********** Begin *********#
    def __str__(self):
        """
        相当于修改内置函数print()
        :return: 输出结果格式
        """
        return '(' + str(self.__x) + ', ' + str(self.__y) + ', ' + str(self.__z) + ')'

    def __add__(self, v):
        """
        修改运算符 "+"
        :param v: 向量坐标（加数）
        :return: 向量的和
        """
        result = Vector3d(self.__x + v.__x, self.__y + v.__y, self.__z + v.__z)
        # self.__x 和 v.__x 分别为算式当中的左右操作数

        return result

    def __sub__(self, v):
        """
        修改运算符 "-"
        :param v:
        :return: 向量的差（减数）
        """
        result = Vector3d(self.__x - v.__x, self.__y - v.__y, self.__z - v.__z)

        return result


# ********** End *********#
x1, y1, z1 = map(int, input().split(','))
x2, y2, z2 = map(int, input().split(','))

v1 = Vector3d(x1, y1, z1)
v2 = Vector3d(x2, y2, z2)

print(v1 + v2)
print(v1 - v2)

# v1._Vector3d__x = 3  # 访问私有属性的方法
