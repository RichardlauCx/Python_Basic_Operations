# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def the_number_of_digits(num):
    sums = 0

    while num >= 1:
        # 只要个位上面还有值，那么就继续判断它的位数
        num /= 10
        # print(num)
        sums += 1

    return sums


def judge_narcissistic(num):
    """
    判断是否为水仙花数
    :param num: 判断上界
    :param digit: 判断位数
    :return:
    """

    for elem in range(100, num+1):
        # 遍历的数字
        sums = 0
        digit = the_number_of_digits(elem)  # 获得当前数字位数
        lists = list(str(elem))  # 数字字符列表

        # for index in range(digit):
        #     sums += int(lists[index]) ** digit

        for ele in lists:  # 此方法比上面的更为简洁
            sums += int(ele) ** digit

        if sums == elem:
            print(elem)


if __name__ == '__main__':
    # n = int(input(" ****** 请输入您想确定水仙花数的范围 ******\n"))

    n = int(input())
    # result = the_number_of_digits(n)
    # print("此数的位数为：" + str(result))

    judge_narcissistic(n)
