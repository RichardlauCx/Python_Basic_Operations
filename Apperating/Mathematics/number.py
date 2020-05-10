# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm
import math


def number_seven(n):
    """
    与7相关的数：如果一个正整数，它能被7整除或者它的十进制表示法中某个位数上的数字为7，则称之为与7相关的数。

    题目内容：
    现在我们给定一个正整数n（n<1000），求所有小于等于n的与7无关的正整数的平方和。
    :param n:
    :return:
    """
    total = 0

    for val in range(n+1):
        # 要记是对每一个数操作，而不是对总数操作，理清对象
        string = str(val)
        # if val % 7 == 0 or '7' in string:
        # 与7相关的数

        if val % 7 != 0 and '7' not in string:
            # 与7无关的数
            total += val ** 2
            # print(val)

    print(total)


def square_root_1():
    num = 0

    while True:
        flag = 0
        for val in range(int(num + 150 / 2)):
            if pow(val, 2) == num + 150:
                # 判断为是完全平方数
                flag += 1
                break

        for val in range(int(num + 150 + 136 / 2)):
            if pow(val, 2) == num + 150 + 136:
                flag += 1
                break

        if flag == 2:
            return num

        num += 1


def square_root_2():
    ranges = 1000  # 寻找范围

    for val in range(ranges):
        num_1 = math.sqrt(val + 150)
        num_2 = math.sqrt(val + 150 + 136)

        if num_1 == int(num_1) and num_2 == int(num_2):
            # 如果开根号还是整数，则证明是算术平方根
            return val

        # if pow(num_1, 2) == val + 150 and pow(num_2, 2) == val + 150 + 135:
        #     # 若能平方回去，则证明是算术平方根
        #     return val


if __name__ == '__main__':
    # num = int(input())
    # number_seven(num)
    # print(special())
    print(square_root_2())