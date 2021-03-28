# -*- coding: utf-8 -*-
#  @ Date   : 2021/3/27
#  @ Author : RichardLau_Cx
#  @ File   : test.py
#  @ Project: Python_Basic_Operations
#  @ IDE    : PyCharm


import time

a = f"{'西安欢迎你!':<50s}"
i = 0
while 1:
    a1 = a[i:]  # 用切片组合进行输出
    a2 = a[:i]
    print(f"\r{a1}{a2}", end='')
    time.sleep(0.5)  # 推迟执行的秒数可以限制滚动速度 数值越大 滚动越慢
    i -= 1
    i %= 50