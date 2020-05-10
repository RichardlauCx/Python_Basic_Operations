# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import math


def print_(x):
    if type(x) == float:
        print("%.4f" % x)
    else:
        print(x)

    return x


# ********** Begin ********** #
# 请在每一题的print语句内完成题目所需的表达式

# 第一题
val_1 = print_(pow(math.pi, 4) + pow(math.pi, 5))
val_2 = print_(pow(math.e, 6))
print_(val_1-val_2)

# 第二题
val_3 = print_(math.pi/4)
val_4 = print_(4 * math.atan(1 / 5) - math.atan(1 / 239))
# print_(val_3-val_4)

# 第三题
val_5 = print_(math.cos(2 * math.pi / 17))
val_6 = print_((1 / 16) * (-1 + math.sqrt(17) + math.sqrt(2 * (17 - math.sqrt(17))) + 2 * math.sqrt(17 + 3 * math.sqrt(17) - math.sqrt(2 * (17 - math.sqrt(17))) - 2 * math.sqrt(2 * (17 + math.sqrt(17))))))
print_(val_5 - val_6)

# 第四题
print_(math.sqrt((1 + math.sqrt(5)) / 2 + 2) - (1 + math.sqrt(5)) / 2)

# 第五题
val_7 = print_(math.sinh(0.25))
val_8 = print_((pow(math.e, 0.25) - pow(math.e, -0.25)) / 2)
# print_(val_7 - val_8)
