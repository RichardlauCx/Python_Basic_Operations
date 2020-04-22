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

        con.acquire()
        while x <= self.num:

            if x == self.num:
                con.wait()

                try:
                    con.notify()
                except Exception:
                    pass


            print(x, end=' ')
            x += 1

            time.sleep(0.1)



        print(x)  # 正好最后一个值没来得及输出
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

        while x >= 0:
            if x == 0:
                con.wait()
                try:
                    con.notify()
                except Exception:
                    pass

            print(x, end=' ')
            x -= 1
            time.sleep(0.1)  # 防止输出顺序混乱


        print(x)
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