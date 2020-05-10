# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import decimal


def decimal_mod():
    print(0.1 + 0.1 + 0.1 - 0.3)  # ---> 5.551115123125783e-17

    result = decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3')
    # 传入字符串为十进制的表示，生成对象后，具有定点精度
    print(result)  # ---> 0.0


if __name__ == '__main__':
    decimal_mod()