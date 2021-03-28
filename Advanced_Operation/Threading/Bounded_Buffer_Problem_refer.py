# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import threading
import time

con = threading.Condition()


class Producer(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        global x
        # *********begin*********#

        con.acquire()  # 先执行，先获得到锁

        if x == self.num:
            con.wait()

        else:
            while x < self.num:
                print(x, end=' ')
                time.sleep(0.1)
                x += 1

            print(x)  # 正好最后一个值没来得及输出
            con.notify()

        con.release()
    # ********* end*********#


class Consumer(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        global x
        # *********begin*********#

        con.acquire()

        if x == 0:
            con.wait()

        else:
            while x > 0:
                print(x, end=' ')
                time.sleep(0.1)  # 防止输出顺序混乱
                x -= 1

            print(x)
            con.notify()

        con.release()
    # ********* end*********#


num = input()
x = 0
num = int(num)  # 输入x值的上限
p = Producer(num)
c = Consumer(num)
p.start()
c.start()
p.join()
c.join()
