# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def start():
    lists = list(map(int, input().split(' ')))
    length = len(lists)
    num = int(input())
    result = []

    for i in range(length-1):
        for j in range(i+1, length):
            if lists[i] + lists[j] == num:
                result.append(i)
                result.append(j)
                return result  # 索引编号 -> 以列表形式打印


if __name__ == '__main__':
    print(start())
