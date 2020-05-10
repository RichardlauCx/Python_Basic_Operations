
# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import fractions
from fractions import Fraction


def fractions_mod():
    val = Fraction.from_float(1.75)  # 过程中会结合2进制的转换，所以类似1.3这样的转换就会出问题。
    print(val)


if __name__ == '__main__':
    fractions_mod()