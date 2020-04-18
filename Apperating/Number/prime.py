# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm
#  @ Introduction : 素数（质素）


def judge_prime():
    n = int(input())
    lists = []

    if 2 < n <= 100:
        for num in range(2, n):
            for digit in range(2, int(num/2)+1):
                if num % digit == 0:
                    # 能被整除，则不是质数
                    break

            else:  # 循环结束后
                lists.append(num)
        print(lists)

    else:
        print("请输入：一个大于2的正整数n")


if __name__ == '__main__':
    judge_prime()