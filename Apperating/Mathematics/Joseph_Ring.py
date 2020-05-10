# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def problem_method1():
    """
    3<=n<=100, 1<=m<=n
    :return:
    """
    lists = []
    result_ls = []
    global n, m

    try:
        n = int(input())
        m = int(input())

        if not 3 <= n <= 100 and not 1 <= m <= n:
            raise ValueError  # #this will send it to the print message and back to the input option

    except ValueError:
        print("Invalid integer. Please Enter the data in a given range!")

    for guy in range(n):
        lists.append(guy)

    guys = 0

    while True:
        guy = guys % len(lists)  # 保证能够形成环
        print(guy)

        if (guys+1) % m == 0:
            result_ls.append(lists.pop(guy))
            guys = guy + 1

        guys += 1

        if len(lists) == 0:
            break

    return result_ls


def problem_false2():
    """
    3<=n<=100, 1<=m<=n
    :return:
    """
    lists = []
    result_ls = []
    global n, m

    try:
        n = int(input())
        m = int(input())

        if not 3 <= n <= 100 and not 1 <= m <= n:
            raise ValueError  # #this will send it to the print message and back to the input option

    except ValueError:
        print("Invalid integer. Please Enter the data in a given range!")

    for guy in range(n):
        lists.append(guy)

    guys = 0
    count = 1  # 报数

    while True:
        if len(lists) == 0:
            break

        guy = guys % len(lists)  # 保证能够形成环
        print(guy)

        if count == m:
            result_ls.append(lists.pop(guy))
            count = 1
            guys = 0
            continue

        guys += 1
        count += 1

    return result_ls


def problem_false3():
    """
    3<=n<=100, 1<=m<=n
    :return:
    """
    lists = []
    result_ls = []
    global n, m

    try:
        n = int(input())
        m = int(input())

        if not 3 <= n <= 100 or not 1 <= m <= n:
            raise ValueError  # #this will send it to the print message and back to the input option

    except ValueError:
        print("Invalid integer. Please Enter the data in a given range!")

    # for guy in range(n):
    #     lists.append(guy)

    lists = list(range(n))

    while True:
        if len(lists) == 0:
            break

        for index in range(len(lists)):
            if (index+1) % m == 0:
                result_ls.append(lists.pop(index))

    return result_ls


def problem_method4():
    """
    3<=n<=100, 1<=m<=n
    :return:
    """
    result_ls = []
    global n, m

    try:
        n = int(input())
        m = int(input())

        if not 3 <= n <= 100 or not 1 <= m <= n:
            raise ValueError  # #this will send it to the print message and back to the input option

    except ValueError:
        print("Invalid integer. Please Enter the data in a given range!")

    # for guy in range(n):
    #     lists.append(guy)

    lists = list(range(n))  # 数据存放
    count = 0

    while True:
        if len(lists) == 0:
            break

        count = (count + (m-1)) % len(lists)
        # -1 相当于刨去报数开头的那个计数，只加 delta量
        # 位置(count) 加 增量(m-1) 取余 总长度，超出范围后即又从头开始，则可形成约瑟夫环
        # 注意：总长度与被取余数，也形成了一个互相动态的过程，如：长度慢慢减少，自然就进入下一圈更多；长度较长时，即在本圈中标记
        # 取余时，找下一个标记点（以当前位置为参考点），不止是判断向后的圈，本圈也会判断
        result_ls.append(lists.pop(count))  # 弹出之后，后面的会自动补过来，所以相当于接起来了，就不必过多考虑

    return result_ls


if __name__ == '__main__':
    n, m = None, None

    print(problem_method4())
