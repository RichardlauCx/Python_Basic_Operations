# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import copy


def dict_():
    dict = {'1': 1, '2': 2}
    theCopy = dict  # 这只是相当于给了一个别名
    shallow_copy = copy.copy(dict)  # 浅拷贝
    deep_copy = copy.deepcopy(dict)  # 深拷贝
    # print(theCopy['1'])
    dict['1'] = 5
    # print(theCopy['1'])

    sum1 = dict['1'] + theCopy['1']
    sum2 = dict['1'] + shallow_copy['1']
    sum3 = dict['1'] + deep_copy['1']

    print(sum1)
    print(sum2)
    print(sum3)


def add_value():
    x = {1: 2}
    x[2] = 3

    # x = {1: 2, 2: 3}  # 简化后，等作用
    print(x)


def in_the_dictionary():
    dicts = {}
    lists = list(map(int, input().split()))
    n = len(lists) // 2  # 取出中值（Floor除法）
    print(n)

    if type(n) is int:
        # 如果是整型，则必定为偶数
        for elem in lists:
            if elem < 0:
                lists.remove(elem)

        dicts['1'] = lists[:n]
        dicts['2'] = lists[n:]

        print(dicts)


if __name__ == '__main__':
    # dict_()
    # add_value()
    in_the_dictionary()