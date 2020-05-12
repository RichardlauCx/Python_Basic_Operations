# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def derivation_1():
    sets = {x*x for x in range(10)}


def derivation_2():
    sets = {x + y for x in range(10) for y in range(x)}  # 此时右侧部分相当于循环嵌套，而不是分别循环


if __name__ == '__main__':
    pass
