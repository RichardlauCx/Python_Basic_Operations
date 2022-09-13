# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def fun_lambda_1():
    lists = list(map(lambda x: len(x), ['a', '12', 'ab123']))  # map 会解析出来值，映射进去
    print(lists)


def fun_lambda_2():
    func_1 = lambda x: x * 2
    func_2 = lambda x: x ** 2

    print(func_1(func_2(2)))


counter = 1


def fun_global():
    number = 0

    def func():
        global counter
        #
        for i in [1, 2, 3]:
            counter += 1

        number = 10

    #
    func()
    print(counter, number)


def Sum(a, b=3, c=5):
    """
    计算一个列表的的总和
    :param a:
    :param b:
    :param c:
    :return: 返回结果
    """
    return sum([a, b, c])


def func_lambda_1():
    func_1 = lambda x: x*2
    func_2 = lambda x: x*3

    a = 2
    a = func_1(a)
    a = func_2(a)
    a = func_1(a)

    print(a)


if __name__ == '__main__':
    # fun_lambda_1()
    # fun_lambda_2()
    # fun_global()
    # print(Sum(8, 2))
    # func_lambda_1()
    pass
