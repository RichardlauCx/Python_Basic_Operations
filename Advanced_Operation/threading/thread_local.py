# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import threading
import time

global_data = threading.local()
x = 10


def action():
    global x
    global_data.x = x  # 建立线程局部变量（过程使用）

    for i in range(1000000):
        global_data.x += 1
        # print(global_data.x)
        global_data.x -= 1
        # print(global_data.x)

    x = global_data.x


x = int(input())


thread = []

for i in range(10):
    thread.append(threading.Thread(target=action))
    thread[i].start()

for i in range(10):
    thread[i].join()

# time.sleep(100)
print(x)

