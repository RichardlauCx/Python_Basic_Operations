# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def transform():
    alist = [1, 1, 2, 3]
    b = set(alist)
    print(b)


def union():
    str_set_1 = set(input())
    str_set_2 = set(input())

    string = str_set_1 | str_set_2  # | 为位运算 ---》 |	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1
    print(sorted(string))


if __name__ == '__main__':
    # transform()
    union()
