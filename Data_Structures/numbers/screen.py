# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def screen():
    for j in (i ** 2 for i in range(10) if i % 3 == 0):
        print(j, end=' ')


if __name__ == '__main__':
    screen()
