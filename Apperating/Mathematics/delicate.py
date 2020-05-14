# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def start_be():
    x = int(input())
    y = int(input())
    n = int(input())
    lists = []
    num = 1
    flag = False

    while num <= n:
        for i in range(n):
            for j in range(n):
                if num == pow(x, i) + pow(y, j):
                    lists.append(num)
                    flag = True
                    break

            if flag:
                flag = False
                break

        num += 1

    return sorted(lists)


def start():
    x = int(input())
    y = int(input())
    n = int(input())
    sets = set()
    num = 1

    # lists = [num for ]
    for i in range(n):
        for j in range(n):
            num = pow(x, i) + pow(y, j)

            if num <= n:  # 返回值小于或等于n(n<=200)
                sets.add(num)

    return sorted(sets)


if __name__ == '__main__':
    print(start())
