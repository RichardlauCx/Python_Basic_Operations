# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


import math
import time
from multiprocessing import cpu_count
from multiprocessing import Pool


# 判断数字是否为质数
# ********** Begin *********#
def isPrime_1(n):
    j = 0
    num = 2
    if n < 2:
        return False

    for j in range(num, n):
        if n % j == 0:
            # 不是质数
            return False

    # print(j, n)

    if n == 2 or j == n-1:
        return True
    else:
        return False


def isPrime(n):
    if n <= 1:
        return False

    for num in range(2, int(math.sqrt(n)) + 1):
        # 只需要参考至开方后的那个数即可，过了开方的若有，除了它本身之外必定会再有一个小于开方后值的数
        if n % num == 0:
            return False

    return True  # 如果一直没有被整除，则判定是质数

# ********** End *********#


# 计算给定区间含有多少个质数
# ********** Begin *********#
def howMany(T):
    sums = 0

    for elem in T:
        if isPrime(elem):
            sums += 1

    # print(sums)

    return sums
# ********** End *********#

# 对整个数字空间N进行分段CPU_COUNT
# ********** Begin *********#
# def separateNum_1(N, CPU_COUNT):
#     # num_section = math.ceil(N / CPU_COUNT)  # 向上取整，多一个也要分一组
#     # num_frac = N / num_section
#     num_frac = N - CPU_COUNT
#     sep = []
#     temp = []
#     accum = 0
#
#     while num_frac > 0:
#
#         for i in range(CPU_COUNT*accum, (CPU_COUNT+1) * (accum+1)):
#             temp.append(i)
#
#             print(temp)
#
#         accum += 1
#         num_frac = N - CPU_COUNT*accum


        # num_frac

    # for i in range(N):
    #     temp.append(i)
    #
    #     if i % num_section == 0:
    #         for _ in temp:
    #             # sep.append(temp.pop(index=temp.index(_)))
    #             # print(_)
    #             pass

        # print("temp: ", temp)
        # print("sep: ", sep)


# ********** End *********#

# 对整个数字空间N进行分段CPU_COUNT
# ********** Begin *********#
def separateNum(N, CPU_COUNT):
    num_section = math.ceil(N / CPU_COUNT)  # 向上取整，多一个也要分一组
    lists_num = []
    accum = 0
    lists_sect = []

    for i in range(1, N+1):
        lists_num.append(i)

    for i in range(num_section):
        lists = lists_num[CPU_COUNT*accum: CPU_COUNT*(accum+1)]
        lists_sect.append(lists)

        accum += 1

    return lists_sect, num_section
        # print(lists_sect)


def separateNum_1(N, CPU_COUNT):
    lists = [[i*(N//CPU_COUNT)+1, (i+1) * (N//CPU_COUNT)] for i in range(0, CPU_COUNT)]
    print(lists)
    lists[0][0] = 1


    if lists[CPU_COUNT-1][1] < N:
        lists[CPU_COUNT-1][1] = N

    return lists


if __name__ == '__main__':
    N = int(input())
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    # 多进程
    CPU_COUNT = cpu_count()  # CPU内核数 本机为8
    pool = Pool(CPU_COUNT)
    sepList, sec = separateNum(N, CPU_COUNT)
    result = []
    for i in range(sec):
        result.append(pool.apply_async(howMany, (sepList[i], )))
    pool.close()
    pool.join()
    # print(result)
    ans = 0
    list = [res.get() for res in result]
    # print(list)
    print(sum(list))
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 2, 3, 5, 7,