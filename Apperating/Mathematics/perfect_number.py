# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def judge_perfect():
    """
    打印完数：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如 6 = 1＋2＋3。

    题目内容：
    输入一个正整数n（n<1000），输出1到n之间的所有完数（包括n）。
    :return:
    """
    n = int(input())
    sums = 0

    for num in range(1, n + 1):
        divisors = 0  # 因子之和

        for count in range(1, int(num / 2) + 2):
            # 取中间值能够提高算法效率，减少不必要的运算，比较到中值大一点儿的整数（偶数大1，奇数大1以内）
            # print("num: " + str(num) + "    count: " + str(count))

            if num % count == 0:
                # print(count)
                # 因子之和
                divisors += count

        if num == divisors and num != 1:
            # 完数
            # print(num)
            # print("divisors" + str(divisors))
            print(divisors)


if __name__ == '__main__':
    # n = int(input())
    # print(n/2)
    # print(int(29/2) + 1)
    judge_perfect()
