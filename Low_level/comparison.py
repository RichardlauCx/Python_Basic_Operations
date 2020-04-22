# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def comparison():
    print(0x56 > 56)  # 0x为16进制，进制越大的数换算与统一进制下的值越大
    print(3 > 2 > 2)
    print((3, 2) > (ord('a'), ord('b')))  # 将字符串转化为对应的数值
    print('a' < 'b' < 'c')


if __name__ == '__main__':
    pass