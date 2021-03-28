# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def derivation_1():
    dicts_1 = {'K%d' % (x, ): x**3 for x in range(10)}  # 逗号只是起着分隔元组中参数的作用，并不是输出所见的逗号
    return dicts_1


if __name__ == '__main__':
    print(derivation_1())
