# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def fun(num):
    num *= 2


def test_0():
    alist = ['a', 'b', 'c']
    blist = alist[:1:-1]  # 倒序取值
    print(blist)


def test_1():
    L1 = ['abc', ['123', '456']]
    L2 = ['1', '2', '3']
    print(L1 > L2)  # 字母要比数字的ASCII码大
    """
    比较规则：
    从第一个元素顺序开始比较，如果相等，则继续，返回第一个不想等元素比较的结果。如果所有元素比较均相等，则长的列表大，一样长则两列表相等
    """


def test_2():
    dicts = {}  # 创建的是一个空字典
    print(type(dicts))

# x = 20
# fun(x)
# print(x)


def test_3():
    data = [1, 0, 2, 0, 0]
    data.remove(0)  # 删除的是给定对象
    print(data)


def test_4():
    print([i ** i for i in range(5) if i % 2 != 0])


def test_5():
    print(int(2.9))  # 直接去掉小数点后面的值
    print(type(2.0))
    print(0.1+0.2 == 0.3)  # -> False
    print(0.1+0.2)  # -> 0.30000000000000004, 因为二进制和十进制转换之间造成的


def test_6():
    for i in range(3, 0, -1):  # 反的来本来就是从大到小：3,2,1
        print(3 - i)


def test_7():
    print(abs(-3 + 4j))  # 勾股定理可得出


def test_8():
    i = 1
    while i < 3:
        print(i)
        i += 1


if __name__ == '__main__':
    # test_0()
    # test_1()
    # test_2()
    # test_3()
    # test_4()
    # test_5()
    # test_6()
    # test_7()
    test_8()

