# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def derivation_1():
    lists = [x*x for x in range(10)]


def derivation_2():
    lists = [x + y for x in range(10) for y in range(x)]  # 此时右侧部分相当于循环嵌套，而不是分别循环，详见function: test_1()
    return lists


def derivation_3():
    lists = [x*x for x in range(10) if x % 2 == 0]  # 相当于只要偶数的平方
    return lists


def derivation_4():
    lists = [x.upper() for x in [1, 'abc', 'xyz', True] if isinstance(x, str)]  # 如果是字符串实例对象的话，那么就将此字符串转换为全部大写
    return lists


def test_1():
    for x in range(10):
        for y in range(x):
            print('x:' + str(x) + '   y: ' + str(y))


if __name__ == '__main__':
    # derivation_1()
    # print(derivation_2())
    # test_1()
    print(derivation_4())