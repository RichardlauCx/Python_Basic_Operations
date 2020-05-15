# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def test_1():
    """
    此方案将得八分
    :return:
    """
    lists_str = input().upper()
    lists = []

    for val in range(len(lists_str)):
        # if type(lists_str[val]) == int or type(lists_str[val]) == str:
        if type(lists_str[val]) == int or 'A' <= lists_str[val] <= 'Z' or 'a' <= lists_str[val] <= 'z':
            lists.append(lists_str[val])

    # lists = str(lists).upper()
    # print(int)
    # print(lists)
    # print(lists[::-1])

    return lists == lists[::-1]


def test_2():
    """
    :return:
    """
    lists_str = input().upper()
    lists = []
    s = ''

    for val in lists_str:
        if val.isdigit() or val.isalpha():
            # lists.append(val)
            s += val

    return s == s[::-1]  # Python判断回文数的精髓


if __name__ == '__main__':
    print(test_2())
