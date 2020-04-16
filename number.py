# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def number_seven(n):
    """
    与7相关的数：如果一个正整数，它能被7整除或者它的十进制表示法中某个位数上的数字为7，则称之为与7相关的数。

    题目内容：
    现在我们给定一个正整数n（n<1000），求所有小于等于n的与7无关的正整数的平方和。
    :param n:
    :return:
    """
    total = 0

    for val in range(n+1):
        # 要记是对每一个数操作，而不是对总数操作，理清对象
        string = str(val)
        # if val % 7 == 0 or '7' in string:
        # 与7相关的数

        if val % 7 != 0 and '7' not in string:
            # 与7无关的数
            total += val ** 2
            # print(val)

    print(total)


if __name__ == '__main__':
    num = int(input())
    number_seven(num)