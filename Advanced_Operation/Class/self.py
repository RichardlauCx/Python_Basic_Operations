# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


class Account:
    def __init__(self, id):
        self.id = id
        id = 888


class A:
    def __init__(self, a, b, c):
        self.x = a + b + c


if __name__ == '__main__':
    acc = Account(100)
    print(acc.id)

    a = A(6, 2, 3)
    print(a.x)
