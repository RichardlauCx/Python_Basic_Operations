# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def test():
    lists_1 = list(map(int, input().split()))
    lists_2 = list(map(int, input().split()))

    length = len(lists_1)
    sums = 0

    for i in range(length):
        sums += pow(lists_1[i] - lists_2[i], 2)

    return sums


if __name__ == '__main__':
    print(test())
