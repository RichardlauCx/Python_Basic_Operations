# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def merge_sort(lst):
    """
    归并排序实现
    :param lst: 待排序列表
    :return: 排序后的列表
    """

    # print("lst:", lst)
    if len(lst) <= 1:
        return lst

    middle = int(len(lst) / 2)
    # print("middle：", middle)
    merget = []

    # print("---------------回调用一次------------")
    # data_list = [6, 202, 100, 301, 38, 8, 1]

    # 递归的思想
    left = merge_sort(lst[:middle])  # 先从这里一层一层往出退
    right = merge_sort(lst[middle:])  # 再重这里一层一层往出退

    # print("left: ", left)
    # print("right: ", right)

    while left and right:
        merget.append(left.pop(0) if left[0] <= right[0] else right.pop(0))  # 输出两个列表首值中，相对较小的元素
        # print("merget: ", merget)

    # print("---------------结束调用一次------------")

    # print(fla)
    # print(merget)
    merget.extend(right if right else left)
    return merget


"""
Debug:
lst: [6, 202, 100, 301, 38, 8, 1]
middle： 3
---------------回调用一次------------
lst: [6, 202, 100]
middle： 1
---------------回调用一次------------
lst: [6]
lst: [202, 100]
middle： 1
---------------回调用一次------------
lst: [202]
lst: [100]
left:  [202]
right:  [100]
merget:  [100]
---------------结束调用一次------------
left:  [6]
right:  [100, 202]
merget:  [6]
---------------结束调用一次------------
lst: [301, 38, 8, 1]
middle： 2
---------------回调用一次------------
lst: [301, 38]
middle： 1
---------------回调用一次------------
lst: [301]
lst: [38]
left:  [301]
right:  [38]
merget:  [38]
---------------结束调用一次------------
lst: [8, 1]
middle： 1
---------------回调用一次------------
lst: [8]
lst: [1]
left:  [8]
right:  [1]
merget:  [1]
---------------结束调用一次------------
left:  [38, 301]
right:  [1, 8]
merget:  [1]
merget:  [1, 8]
---------------结束调用一次------------
left:  [6, 100, 202]
right:  [1, 8, 38, 301]
merget:  [1]
merget:  [1, 6]
merget:  [1, 6, 8]
merget:  [1, 6, 8, 38]
merget:  [1, 6, 8, 38, 100]
merget:  [1, 6, 8, 38, 100, 202]
---------------结束调用一次------------
"""

if __name__ == '__main__':
    data_list = [6, 202, 100, 301, 38, 8, 1]
    # flag = 0
    # flag += 1
    print(merge_sort(data_list))

    # merge_sort(data_list)
