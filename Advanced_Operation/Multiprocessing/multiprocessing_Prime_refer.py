# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©Educoder
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import math
from multiprocessing import cpu_count
from multiprocessing import Pool

# 判断数字是否为质数
#********** Begin *********#
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
#********** End *********#

# 计算给定区间含有多少个质数
#********** Begin *********#
def howMany(T):
    sum = 0;
    for i in range(T[0], T[1] + 1):
        # 观察每一小段内的质数性
        if isPrime(i):
            sum += 1
    return sum
#********** End *********#


# 对整个数字空间N进行分段CPU_COUNT
#********** Begin *********#
def separateNum(N, CPU_COUNT):
    list = [[i * (N // CPU_COUNT) + 1, (i + 1) * (N // CPU_COUNT)] for i in range(0, CPU_COUNT)]  # 相当于整除的下界与整除的上界
    # (N // CPU_COUNT) 相当于每一个CPU要处理的数据量，整体即为寻找之间的上下平衡，下一个的开始为上一个结束加一（不重复）
    # 相当于拿出每个范围的首尾位置，来划定区间范围
    print(list)
    list[0][0] = 1  # 第一个总下限
    if list[CPU_COUNT - 1][1] < N:  # 最后一个总上限
        list[CPU_COUNT - 1][1] = N
    return list
#********** End *********#


if __name__ == '__main__':
    N = int(input())
    # 多进程
    CPU_COUNT = cpu_count()  # #CPU内核数 本机为8
    pool = Pool(CPU_COUNT)
    sepList = separateNum(N, CPU_COUNT)
    result = []
    for i in range(CPU_COUNT):
        result.append(pool.apply_async(howMany, (sepList[i], )))
    pool.close()
    pool.join()
    ans = 0
    list = [res.get() for res in result]
    print(sum(list), end = '')
    # print(result)
