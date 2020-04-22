# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def uc_filter():
    lists = list(map(int, input().split(' ')))
    res_list = []

    # for index in range(1, len(lists), 2):  # 奇数位的<索引值>！
    #     # 注意：由于列表索引是从0开始的，所以对于索引值来说，相当于偶数数列（0,2,4...）
    #     res_list.append(lists[index])

    res_list = lists[1::2]  # 等价于上面，但是优化了很多

    return res_list


if __name__ == '__main__':
    print(uc_filter())
