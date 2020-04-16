# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def while_1():
    k = 1000
    sums = 0
    while k > 1:
        # print(k)
        sums += 1
        k = k / 2

        print(sums)


def while_2():
    n = 1
    while n >= 0:
        print(n)
        n = n - 1
    else:
        print(n)


def while_3():
    n = 1
    while n >= 0:
        n = n - 1
        print(n)
    else:
        print(n)


def while_4():
    i = 1
    while i < 3:
        print(i)
        i += 1


def while_5():
    for i in range(3, 0, -1):
        print(i + 1)


def for_1():
    for i in range(3):
        print(i, end=',')


def for_2():
    for i in range(2):
        print(i, end='')
    else:
        print(0)


def for_3():
    lst = [1, 3, 5, 7]
    for i in lst:
        print(i)
        if i >= 5:
            break
    else:
        print('END')  # 提前跳出啦，所以不执行


if __name__ == '__main__':
    # while_1()
    # while_2()
    # while_3()
    # while_4()
    while_5()

    # for_1()
    # for_2()
    # for_3()
