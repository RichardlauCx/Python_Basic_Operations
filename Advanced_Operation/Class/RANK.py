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
        self.total = self.score_m + self.score_c + self.score_e

    # def __gt__(self, other):
    #     if self.total > other.total:
    #         return str(self.name) + ' ' + str(self.score_m) + ' ' + str(self.score_c) + ' ' + str(self.score_e)
    #
    #     else:
    #         return str(other.name) + ' ' + str(other.score_m) + ' ' + str(other.score_c) + ' ' + str(other.score_e)

    def __lt__(self, other) -> bool:
        """
        重写小于号的方法，对于sort()函数才有效果
        :param other:
        :return:
        """
        if self.total < other.total:
            return False  # 因为要从大到小来排序

        else:
            return True


def start():
    """
    通过修改操作符"<"来对应修改内置函数sort()的实现方法
    :return:
    """
    stu = []
    name = input().split(' ')
    amount = len(name)
    score_m = list(map(int, input().split(' ')))
    score_c = list(map(int, input().split(' ')))
    score_e = list(map(int, input().split(' ')))

    for i in range(amount):
        stu.append(Student(name[i], score_m[i], score_c[i], score_e[i]))

    stu.sort()
    # stu = sorted(stu, key=lambda x: x.total)  # 如果没有重写__lt__方法的话再通过key进行判断
    # print(stu)
    # stu = sorted(stu, key = lambda total: stu[0].total)
    print(str(stu[0].name) + ' ' + str(stu[0].score_m) + ' ' + str(stu[0].score_c) + ' ' + str(stu[0].score_e))

    # print(stu_1.name + ' ' + stu_1.score_m + ' ' + stu_1.score_c + ' ' + stu_1.score_e)
    # print(stu_0)

    # print(stu_0 > stu_1)


def func_2():
    """
    通过改变排序算法的键判断情况来实现
    :return: None
    """
    pass


if __name__ == '__main__':
    start()
