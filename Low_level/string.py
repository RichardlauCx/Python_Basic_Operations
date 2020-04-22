# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def string():
    x = "big"
    y = 2
    # print(x + y)

    x = "big"
    y = 2
    # print(x * y)

    x = "big"
    y = "name"
    # print(x + y)

    x = 156
    ch = 'A'
    y = 1
    # print(x >= y and ch < 'b' and y)  # 直到最后一个，若还成立，则输出最后一位表达式的值
    # print(ord(ch), ord('a'))

    name = "Mike"
    w = name.upper()
    # print(w)

    name = "Mike"
    u = name[-2:]
    print(u)


def rotate_left():
    """
    字符串循环左移（10分）
    :return:
    """

    s = str(input())
    n = int(input())

    temp = s[:n]
    result = s[n:] + temp

    print(result)


if __name__ == '__main__':
    # string()
    rotate_left()