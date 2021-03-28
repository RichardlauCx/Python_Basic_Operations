# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def fun():
    print(0)
    i = 0
    while i < 3:
        i += 1
        yield i


if __name__ == '__main__':
    x = fun()
    y = (i for i in x)
    print(list(y))