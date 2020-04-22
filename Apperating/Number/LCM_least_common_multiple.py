# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def lcm():
    num_1 = int(input())
    num_2 = int(input())

    if num_1 > num_2:
        num_max = num_1

    else:
        num_max = num_2

    for val in range(num_max, num_1 * num_2 | +1):  # 从高耦合，至低耦合靠拢（从最大的一个数 -> 两个数的积）
        if val % num_1 == 0 and val % num_2 == 0:
            return val


if __name__ == '__main__':
    print(lcm())
