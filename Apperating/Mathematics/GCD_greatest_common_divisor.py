# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def gcg():
    num_1 = int(input(""))
    num_2 = int(input(""))

    if num_1 < num_2:
        num_min = num_1

    else:
        num_min = num_2

    for val in range(num_min, 0, -1):  # 从高耦合，向低耦合靠拢，尽最大概率减少资源浪费（从最小的一个数 -> 一）
        if num_1 % val == 0 and num_2 % val == 0:
            return val


if __name__ == '__main__':
    print(gcg())