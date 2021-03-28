# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


from Class.func__dict__ import Person

print(Person)

class Parent:
    def __init__(self, param):
        self.v1 = param


class Child(Parent):
    def __init__(self, param):
        super().__init__(param)
        self.v2 = param


# if __name__ == '__main__':
    # obj = Child(100)
    # # print(obj.v1 == obj.v2)
    # print(obj.v1)

