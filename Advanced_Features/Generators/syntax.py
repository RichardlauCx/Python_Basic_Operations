# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def even_number(max):
    n = 0

    while n < max:
        yield n
        n += 2


if __name__ == '__main__':
    for val in even_number(10):  # 生成器对象
        print(val)
