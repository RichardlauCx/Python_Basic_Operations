# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import math


def formula():
    x = int(input())

    result = math.sin(math.radians(15)) + (math.pow(math.e, x) - 5 * x) / math.sqrt(math.pow(x, 2) + 1) - math.log(
        3 * x, math.e)
    # 注：log 默认若不写底数则功能相当于 ln

    print(round(result, 10))


if __name__ == '__main__':
    formula()
