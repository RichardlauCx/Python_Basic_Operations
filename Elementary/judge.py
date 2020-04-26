# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import datetime


def judge_days():
    dtstr = "20181206"
    dt = datetime.datetime.strptime(dtstr, "%Y%m%d")  # 格式转化为datetime
    another_dtstr = dtstr[:4] + "0101"
    another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
    days = int((dt-another_dt).days) + 1  # 相距天数
    return days


if __name__ == '__main__':
    print(judge_days())
