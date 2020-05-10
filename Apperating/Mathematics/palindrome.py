# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import operator


def judge_palindrome():
    num = input()
    lists = list(num)
    lists_turn = lists[::-1]

    # if operator.eq(lists, lists_turn):
    #     print("yes")
    #
    # else:
    #     print("no")

    result = "yes" if operator.eq(lists, lists_turn) else "no"  # 一行实现条件推导
    print(result)


if __name__ == '__main__':
    judge_palindrome()