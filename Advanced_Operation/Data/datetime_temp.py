# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import calendar
from datetime import *
import datetime


def temp():
    td1 = timedelta(minutes=10)
    td2 = timedelta(minutes=15)

    print(td1 * 10)


def January():
    global days
    days += 31

    return days


days = 0  # 声明


def judge_days_1():
    global days
    # dates_str = input().split('/')  # 保存数据
    dates = list(map(int, input().split('/')))

    for month in range(0, dates[1]):
        # 只有到了下个月时，上个月才叠加满天
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            # 一三五七八十腊，三十一天永不差
            days += 31

        elif month == 4 or month == 6 or month == 9 or month == 11:
            # 四六九冬，三十天
            days += 30

        elif month == 2:
            # 只有二月二十八，闰年二月二十九
            if calendar.isleap(dates[0]):
                days += 29

            else:
                days += 28

    days += dates[2]

    print(days)


def judge_days_2():
    """
    # 也可以通过列表进行遍历
    if ly == True: # 若是闰年，则二月为29天
    ms = [31, 29, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]

    else:
    ms = [31, 28, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]

    :return:None
    """


def judge_days_3():
    """
    input: format-2019/7/8
    :return: None
    """
    dates = list(map(int, input().split('/')))
    # print(dates)

    s_day = datetime.date(dates[0], dates[1], dates[2])  # 固定的一种日期输出格式函数：2019-07-08
    days = s_day - datetime.date(dates[0]-1, 12, 31)  # 减去上一年的最后一天，相当于本年已经过了多少天

    # print(days)  # -> 189 days, 0:00:00
    # print(days.days)
    print(s_day.strftime('%j'))  # %j十进制表示的每年的第几天


def judge_days_4():
    dates = list(map(int, input().split('/')))
    s_day = datetime.date(dates[0], dates[1], dates[2])  # 固定的一种日期输出格式函数：2019-07-08

    print(s_day.strftime('%j'))  # %j十进制表示的每年的第几天
    # 使用内置函数(strftime是一种计算机函数，根据区域设置格式化本地时间/日期，函数的功能将时间格式化，或者说格式化一个时间字符串


if __name__ == '__main__':
    # temp()
    # judge_days()
    # judge_days_2()
    judge_days_3()
