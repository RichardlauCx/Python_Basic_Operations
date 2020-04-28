# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm
import calendar


"""
首先明确  什么是闰年？
    1、能被4整除，但不能被100整除；
    2、能被400整除；
"""


if __name__ == '__main__':
    print(calendar.isleap(2000))
