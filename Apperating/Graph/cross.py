# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def temp_1():
    """
    打印出n阶的“叉”，这个叉图案由字符‘+’和‘X’构成，n越大，这个图案也就越大
    注：找规律问题
    :return:
    """
    # 首先，输入的都需要是奇数
    n = int(input())

    ranges = n * 2 - 1
    for column in range(ranges):
        # 一共有n列

        if column <= ranges / 2:
            print("+" * column, end='')
            print("X", end='')
            print("+" * (n*2 - 3 - column*2), end='')

            if column+1 != n:
                print("X", end='')

            print("+" * column)

        elif column > ranges / 2:
            print("+" * (ranges - (column+1)), end='')
            print("X", end='')
            print("+" * (- (n*2 - column*2 - 1)), end='')
            print("X", end='')
            print("+" * (ranges - (column + 1)))


def temp_2():
    """
    1. 先试着画一个只有“+”的相关矩阵
    2. 在试着画‘+’的循环里面添加‘X’，通过添加if条件语句实现
    3. 在逐步修改，即可得到（X所在位置即矩形对角线）
    :return:
    """
    n = int(input())

    for i in range(0, 2 * n - 1):
        for m in range(0, 2 * n - 1):
            if m == i or m == 2 * n - 1 - 1 - i:
                print('X', end='')
            else:
                print('+', end='')
        print()


def teacher():
    n = int(input()) - 1  # n=2
    lst = ['X'] * (2 * n + 1)  # lst = ['x','x','x','x','x']
    for i in range(n):  # 循环2次，打出前两行
        s = '+' * i + 'X' + '+' * (n - i - 1)  # 打出每一行的前半部分
        s = s + '+' + s[::-1]  # 把 s 倒过来合并字符串
        lst[i] = lst[-1 - i] = s  # 循环替换lst[i]的值
    lst[n] = "+" * n + 'X' + '+' * n  # 把中间一行，即第2行进行修改
    for l in lst:
        print(l)  # 遍历lst里的元素，输出


if __name__ == '__main__':
    temp_1()
    # temp_2()
    # teacher()
