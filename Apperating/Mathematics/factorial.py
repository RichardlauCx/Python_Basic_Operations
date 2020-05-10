# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def fact():
    n = int(input())
    result = 1

    for val in range(1, n+1):
        result *= val

    return result


if __name__ == '__main__':
    print(fact())