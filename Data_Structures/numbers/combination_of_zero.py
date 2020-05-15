# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def test_1():
    lists_num = sorted(list(map(int, input().split())))
    length = len(lists_num)
    num = 0
    lists = []
    sets = set()
    # print(lists_num)

    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                # for 拿出来的是索引值
                if lists_num[i] + lists_num[j] + lists_num[k] == 0:
                    lists.append(lists_num[i])
                    lists.append(lists_num[j])
                    lists.append(lists_num[k])

                    sets.add((lists_num[i], lists_num[j], lists_num[i]))  # 排序后，添加到集合当中则不会出现重复组

                    # num += 1
                    # print(lists_num[i], lists_num[j], lists_num[k])

    # for i in lists_num:
    #     for j in lists_num:
    #         for k in lists_num:
    #             if i + j + k == 0:
    #                 num += 1
    #                 print(i, j, k)

    return len(sets)


def test_2():
    lists_num = list(map(int, input().split()))
    length = len(lists_num)
    num = 0
    # print(lists_num)

    for i in range(length):
        for j in range(length)[i:]:
            for k in range(length)[j:]:
                # if i + j + k == 0:
                #     num += 1
                print(i, j, k)

    # for i in lists_num:
    #     for j in lists_num:
    #         for k in lists_num:
    #             if i + j + k == 0:
    #                 num += 1
    #                 print(i, j, k)

    return num


if __name__ == '__main__':
    print(test_1())
