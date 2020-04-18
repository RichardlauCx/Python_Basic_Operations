# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def solve_iteration():
    """
    题目内容：
    猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
    以后每天早上都吃了前一天剩下的一半零一个。到第n天（<1<n<11）早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
    :return:
    """

    n = int(input())
    peaches = 1  # 最后一天所剩

    if 1 < n < 11:
        for day in range(n, 1, -1):
            peaches = (peaches + 1) * 2  # 算出前一天未吃之前的桃数

        print(peaches)

    else:
        print("请注意输入格式: 共一行，为一个大于1小于11的正整数")


def solve_recurrence(n):
    """
    递归实现：有未知到已知，后面的情况，是根据前面发展出来的
    :return:
    """
    if n == days:
        # 最后一天，递归结束
        return 1

    else:
        return (solve_recurrence(n+1) + 1) * 2
        # 前一天总比后一天，先多一、再乘以二


if __name__ == '__main__':
    day_1 = 1  # 从第一天开始
    days = int(input())

    if 1 < days < 11:
        # for day in range(1, days):
        print(solve_recurrence(day_1))
