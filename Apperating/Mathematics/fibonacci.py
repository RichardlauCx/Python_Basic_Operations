# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


index = 0


def fibonacci_1(n):
    """
    递归虽然代码简便，但是数据量大时会特别消耗资源
    :param n:
    :return: value
    """
    if n < 0:
        return "请重新输入正整数测试！"

    if n == 0:
        return 0

    if 0 < n <= 2:
        return 1

    else:
        return fibonacci_1(n-1) + fibonacci_1(n-2)


def fibonacci_2(n):
    lists = [1, 1]
    global index

    if n < 0:
        return "请重新输入正整数测试！"

    if n == 0:
        return 0

    if 0 < n <= 2:
        return 1

    else:
        for index in range(2, n):  # 索引比真实数值上面少 1
            lists.append(lists[index-1] + lists[index-2])
            # print(lists[index-1] + lists[index-2])

        return lists[index]  # index == n-1


if __name__ == '__main__':
    num = int(input())
    # print(fibonacci_1(num))
    print(fibonacci_2(num))
