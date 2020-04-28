# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import turtle


"""
    分型学之父 --- 数学家曼德勃罗
    分型：主体与部分，以某种方式相似
    自然界：河流、树枝
    分形图：曼德勃罗集
    数学中：龙形曲线、Hilbert（希尔伯特曲线）- 不定维度的（分数维）、谢尔宾斯基三角形（每次面积趋于3/4）- 体积趋于无穷，表面积趋于零
"""


def tree(branch_len, t):

    if branch_len > 5:
        if branch_len > 20:
            # 树枝
            t.color("brown")

        elif branch_len < 20:
            # 树叶
            t.color("green")

        t.down()

        t.forward(branch_len)  # 枝干
        t.right(25)
        tree(branch_len - 15, t)  # 递归实现 分支

        t.left(50)
        tree(branch_len - 15, t)
        t.right(25)

        t.up()
        t.backward(branch_len)  # 回到原位置


def main():
    t = turtle.Turtle()  # 实例化海龟
    my_win = turtle.Screen()  # 初始化窗口

    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")

    tree(75, t)

    my_win.exitonclick()  # 点击事件触发后退出


if __name__ == '__main__':
    main()
