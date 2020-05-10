# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def introduction():
    """
    水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），
    水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

    附：其他位数的自幂数名字
    一位自幂数：独身数
    两位自幂数：没有
    三位自幂数：水仙花数
    四位自幂数：四叶玫瑰数
    五位自幂数：五角星数
    六位自幂数：六合数
    七位自幂数：北斗七星数
    八位自幂数：八仙数
    九位自幂数：九九重阳数
    十位自幂数：十全十美数
    :return: None
    """
    pass


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
