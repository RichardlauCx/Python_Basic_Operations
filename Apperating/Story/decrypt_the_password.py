# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def test():
    lists_str = input()
    n = ord(lists_str[-1]) - ord('E')  if ord(lists_str[-1]) > ord('E') else ord(lists_str[-1]) - ord('E') + (90-65) + 1  # 加密方式，整体移动n个字符位
    s = ''

    for val in lists_str:
        if ord(val) - n < 65:
            s += chr(ord(val)-n + 26)

        else:
            s += chr(ord(val)-n)

    return s


def test_1():
    a = input()
    s = ''
    n = ord(a[-1]) - 69 if ord(a[-1]) > 69 else ord(a[-1]) - 65 + 90 - 69 + 1
    # 相当于用下一圈的值来减它，再加过程中的一，具体加一的原理画图便可知
    for i in a:
        if ord(i) - n < 65:
            s += chr(ord(i) - n + 26)  # 加上它们的间隔值，可以形成一次逻辑环路
        else:
            s += chr(ord(i) - n)
    print(s)


if __name__ == '__main__':
    print(test())
