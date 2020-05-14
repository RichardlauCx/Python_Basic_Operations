# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def start():
    lists = list(map(int, input().split()))  # 没有说明；列表内到底有多少个长度

    lists.sort(reverse=True)  # 方便获取有效三角形的最大周长
    # lists = sorted(lists, reverse=True)

    for i in range(len(lists) - 2):
        if lists[i] < lists[i+1] + lists[i+2]:  # 判断依据：两个小边之和大于最大的一边 ---> 构成有效的三角形
            return sum(lists[i:i+3])

    else:
        return 0


if __name__ == '__main__':
    print(start())