# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import threading
import math

ans = 0
lock = threading.Lock()


# 判断数字是否为质数
# ********** Begin *********#
def isPrime(n):
    if n <= 1:
        return False

    for num in range(2, int(math.sqrt(n)) + 1):
        if n % num == 0:
            return False

    return True


# ********** End *********#


# ********** Begin *********#
# 计算给定区间含有多少个质数
def howMany(T):
    sum = 0

    for num in range(T[0], T[1] + 1):
        if isPrime(num):
            sum += 1

    lock.acquire()  # 获得线程锁，保护共享的数据
    try:
        global ans
        ans += sum

    finally:
        lock.release()  # 数据操作完毕释放锁

    return sum


# ********** End *********#

# ********** Begin *********#
# 对整个数字空间N进行分段CPU_COUNT
def seprateNum(N, CPU_COUNT):
    lists = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(CPU_COUNT)]  # 相当于整除的下界与整除的上界（每一段的上下）
    lists[0][0] = 1  # 首项
    lists[-1][-1] = N  # 尾项

    # print(lists)
    return lists


# ********** End *********#


if __name__ == '__main__':
    N = int(input())
    threadNum = 32
    t = []
    sepList = seprateNum(N, threadNum)

    for i in range(0, threadNum):
        t.append(threading.Thread(target=howMany, args=(sepList[i],)))
        t[i].start()

    for i in range(0, threadNum):
        t[i].join()

    # list = [res.get() for res in result]
    # print(sum(list), end='')

    # for res in t:
    #
    #     print(res)

    # ans = [x for res in t]
    print(N - 1 - ans, end='')  # 使用全局变量法解决，还有一种是自定义获得值方法
    # print(ans)