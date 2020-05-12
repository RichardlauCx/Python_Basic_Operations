# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def derivation_1():
    generators = (x*x for x in range(10))  # 先生成迭代器
    print(generators)

    for n in generators:
        # 随时需要，随时迭代生成
        print(n)

    print(next(i for i in generators))  # 此语句通过next()只能生成一个值
    # 若已经生成完毕，则会抛出：StopIteration异常

    print(tuple(generators))  # 或者通过list、set、dict均可实现


if __name__ == '__main__':
    derivation_1()
