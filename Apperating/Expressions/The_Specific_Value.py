# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def print_(x):
        if type(x) == float:
            print("%.4f" % x)
        else:
            print(x)


def convert():

    # # ********** Begin ********** #
    # #请在每一题的print语句内完成题目所需的表达式

    # #第一题
    print_(1234 % 123)

    # #第二题：某个国家的人均寿命是90岁，请问人均能活多少秒？
    print_(90 * 365 * 24 * 60 * 60)

    # #第三题：123/12的商（整除求得）
    print_(123 // 12)

    # #第四题
    print_(123 / 12)

    # #第五题
    print_(pow(10, 9) / 60 / 60 / 24 / 365)

    # #第六题：要求编写两式比较的表达式，输出为True或False
    print_(pow(3, 3) + pow(4, 3) + pow(5, 3) == pow(6, 3))

    # #第七题：“可知“多百分之一努力，得千分收成”
    print_(pow(1.02, 365))
    print_(pow(1.01, 265))

    # #第八题：要求编写两式比较的表达式，输出为True或False -> 三天打鱼，两天晒网，终将一无所获
    print_(pow(1.01, 3) * pow(0.99, 2) > 1.01)
    # # ********** End ********** #


if __name__ == '__main__':
    convert()