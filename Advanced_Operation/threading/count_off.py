# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


# -*- coding: utf-8 -*-

import threading
import time

lock = threading.Lock()


class mythread(threading.Thread):  # 通过继承的方式
    x = 0

    def __init__(self):
        threading.Thread.__init__(self)
        # 调用多线程类的构造方法

    def run(self):
        global x  # 定义全局变量
    # *********begin*********#
        lock.acquire()
        x += 1
        print(x, end='')
        lock.release()
    # ********* end*********#


num = input()
t1 = []  # 线程列表
for i in range(int(num)):
    t = mythread()
    t1.append(t)
x = 0
for i in t1:
    i.start()  # 启动全部线程
    # print(i.ident)
