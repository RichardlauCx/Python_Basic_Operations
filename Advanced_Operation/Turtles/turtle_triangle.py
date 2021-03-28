# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import turtle

# ********* Begin *********#
def external():
    tur.pendown()
    tur.speed(1)
    tur.left(60)
    tur.forward(200)

    tur.right(120)
    tur.forward(200)

    tur.right(120)
    tur.forward(200)
    tur.right(180)

    tur.penup()


def within():
    tur.pencolor("blue")
    tur.fillcolor("yellow")

    tur.forward(100)

    tur.pendown()
    tur.begin_fill()
    tur.left(60)
    tur.forward(100)

    tur.left(120)
    tur.forward(100)

    tur.left(120)
    tur.forward(100)
    tur.end_fill()

    tur.penup()


def innermost():
    tur.left(120)
    tur.forward(50)

    tur.fillcolor("white")
    tur.pencolor("red")
    tur.left(60)

    tur.pendown()
    tur.begin_fill()
    tur.forward(50)

    tur.left(120)
    tur.forward(50)

    tur.left(120)
    tur.forward(50)
    tur.end_fill()



# ********* End *********#
# 保存屏幕图片
# if __name__ == '__main__':  # 一般用作模块测试时，被其他程序调用后，不会执行的区域
tur = turtle.Turtle()  # 创建turtle对象
tur.pencolor("red")
external()
within()
innermost()

path_1 = "Python/src1/py1-1/yourimg/sj.ps"
path_2 = 'Python/src1/py1-2/yourimg/sj.ps'
path_3 = "Python/src1/py1-3/yourimg/sj.ps"
path = "sj_2.ps"
ts = turtle.getscreen()

ts.getcanvas().postscript(file=path_3)  # 返回默认大小(400, 300), 指定生成路径对象,生成矢量图对象（.ps扩展名为矢量图形文件）

# turtle.done()