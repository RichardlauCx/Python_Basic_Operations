# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def print_pyramid():
    """
    规律：
        1. 逐层符号为奇数序列 2*line + 1
        2. 逐层空格为：n - (line+1)
    :return:
    """
    n = int(input())

    for line in range(n):
        # 最后输出换行
        print(" " * (n - (line+1)), end='')  # 先输出空格
        print("+" * (2*line + 1), end='\n')  # 再输出图形

    # for line in range(n):
    #     # 最后不输出换行
    #     print(" " * (n - (line+1)), end='')  # 先输出空格
    #     print("+" * (2*line + 1), end='')  # 再输出图形
    #
    #     if line != n-1:
    #         # 只有最后一行不换行
    #         print('', end='\n')


if __name__ == '__main__':
    print_pyramid()