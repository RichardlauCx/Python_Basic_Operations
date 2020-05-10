# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


class Person:
    def __init__(self, id):
        self.id = id


if __name__ == '__main__':
    tom = Person(123)  # 相当于传入键值映射
    # print(tom.id)

    tom.__dict__['age'] = 20
    # tom.__dict__['age2'] = 21
    print(len(tom.__dict__))  # 字典的长度是按对来统计计算的，几对就有多长
    # print(tom.__dict__)  # __dict__ 方法使参数形成映射（变量k与值v）字典
    print(tom.age)  # 根据键取值
