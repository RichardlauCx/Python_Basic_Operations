# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


class Student:

    def __init__(self, name: str, score_m: int, score_c: int, score_e: int) -> None:  # :和-> 为函数标注，前者标注参数类型，后者标注返回值类型
        # super().__init__()
        self.name = name
        self.score_m = score_m  # 数学成绩
        self.score_c = score_c  # 语文成绩
        self.score_e = score_e  # 英语成绩


def start():
    stu_0 = Student
    stu_1 = Student

    name = input().split(' ')
    print(name[1])
    stu_0.name = name[0]
    stu_1.name = name[1]
    # print(stu_1.name)

    score_m = input().split(' ')
    stu_0.score_m = score_m[0]
    stu_1.score_m = score_m[1]

    score_c = input().split(' ')
    stu_0.score_c = score_c[0]
    stu_1.score_c = score_c[1]

    score_e = input().split(' ')
    stu_0.score_e = score_e[0]
    stu_1.score_e = score_e[1]

    # print(stu_1.name + ' ' + stu_1.score_m + ' ' + stu_1.score_c + ' ' + stu_1.score_e)


if __name__ == '__main__':
    start()
