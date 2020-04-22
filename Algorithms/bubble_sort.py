# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def bubble_sort():
    lists = list(map(int, input().split()))

    for frequency in range(len(lists)-1):
        # 一个大的趟数，比总数据少一趟
        for index in range(len(lists)-1 - frequency):
            # 不停地向后冒泡泡，冒到头之后，下一次就冒至更低一层
            if lists[index] > lists[index+1]:
                lists[index], lists[index+1] = lists[index+1], lists[index]

    return lists


if __name__ == '__main__':
    print(bubble_sort())
