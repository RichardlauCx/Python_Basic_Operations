# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


if __name__ == '__main__':
    a = 10
    b = 0
    try:
        c = a / b
        print(c)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("always excute")
    print("done")
