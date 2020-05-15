# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def test():
    lists_num = list(map(int, input().split()))
    lists_copy = lists_num[:]  # 乘的时候要乘以之前的数据，不能乘以变化后的数据
    sums = 1

    for i in range(len(lists_num)):
        for val_1 in lists_copy[:i]:
            sums *= val_1

        for val_2 in lists_copy[i+1:]:
            sums *= val_2

        lists_num[i] = sums
        sums = 1

    return lists_num


if __name__ == '__main__':
    print(test())
