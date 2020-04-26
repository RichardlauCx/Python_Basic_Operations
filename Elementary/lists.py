# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm
import sys


def in_():
    a = [3]  # 是一个列表
    alist = [1, 2, 3, 4, 5]
    print(a in alist)


def sort_():
    alist = sorted([1, 2, 3], reverse=True)
    blist = reversed([1, 2, 3])  # 是一个对象
    # print(alist)
    print(alist == blist)


def multiply():
    alist = [1, 2, 3]
    blist = alist * 3  # 和字符串一样，实现复制功能
    print(blist)


def section():
    alist = [3, 4, 5, 7, 9, 12, 13, 15, 17]
    blist = alist[3:7:2]  # 前两个先限制范围，最后的参数则是步长  返回值为：输出加步长
    print(blist)


def nest():
    x = [[]]
    x[0].append(1)
    print(x)


def merge():
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_list.extend(b_list)

    for a_elem in a_list:
        if a_elem > 10:
            a_list.remove(a_elem)

    sets = set(a_list)
    lists = sorted(list(sets))

    print(lists)


def list_reverse():
    lists = list(map(int, input().split()))
    # method one
    lists.sort(reverse=True)
    print(lists)

    # method two
    # print(list(reversed(lists)))

    # method three
    # print(lists[::-1])

    # method four
    lists.reverse()  # 给原列表逆序，不产生新的副本
    print(lists)


def absolute_sort():
    lists = list(map(int, input().split()))
    for elem in lists:
        if type(elem) is not int:
            lists.remove(elem)

    # method one
    # lists.sort(key=abs)
    # print(lists)

    # method two
    print(sorted(lists, key=abs))  # build-in


def judge_num(char):
    """
    此方对判断数字是否为正整数，且不超过10
    :return: 符合要求的数字
    """
    num = int(char)

    if 0 < num < 10:
        return num

    return


def element_overwrite():
    lists = list(map(judge_num, input().split()))
    # raise SyntaxError("只能输入一位的数字！")  # 举起语法错误

    while None in lists:
        lists.remove(None)

    for index in range(len(lists)):
        if lists[index] % 2 != 0:
            lists[index] **= 2

        else:
            lists[index] = int(lists[index]/2)

    print(sorted(lists))

    # n = input()
    # print(type(n))  # 默认字符串


if __name__ == '__main__':
    # in_()
    # sort_()
    # multiply()
    # section()
    # nest()
    # merge()
    # list_reverse()
    # absolute_sort()
    element_overwrite()
