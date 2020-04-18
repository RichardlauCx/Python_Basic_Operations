# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import math
from multiprocessing import cpu_count
from multiprocessing import Pool

N = int(input())
a = list(map(int, input().split()))


def howMany(T):
    # 获取到每段列表之中的最大值
    ans = 0;
    for i in range(T[0] - 1, T[1]):
        ans = max(ans, a[i])
    return ans


# 对整个数字空间N进行分段CPU_COUNT，得出每个进程需要处理的范围
def seprateNum(N, CPU_COUNT):
    list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]
    list[0][0] = 1
    if list[CPU_COUNT - 1][1] < N:
        list[CPU_COUNT - 1][1] = N
    return list


if __name__ == '__main__':
# 多进程
# ********** Begin *********#
    CPU_COUNT = cpu_count()
    pool = Pool(CPU_COUNT)
    sepList = seprateNum(N, CPU_COUNT)
    result = []  # 进程列表

    for i in range(CPU_COUNT):  # CUP数 个进程

        result.append(pool.apply_async(howMany, (sepList[i], )))  # 获取每小段的最大值



    pool.close()
    # pool.terminate()
    pool.join()
    print("在这儿呢~~~")

    # lists = [res.get() for res in result]

    # print(max(lists))  # 输出整个列表的最大值（每段最大值中的最大值）
    exit(0)
# ********** End *********#
