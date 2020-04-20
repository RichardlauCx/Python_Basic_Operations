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


# ********** Begin ********** #
# 请在每一题的print语句内完成题目所需的表达式

# 第一题
print_(pow(math.pi, 4) + pow(math.pi, 5) - pow(math.e, 6))

# 第二题
print_(math.pi - (4 * math.atan(1 / 5) - math.atan(1 / 239)))

# 第三题
print_(math.cos(2 * math.pi / 17) - (1 / 16) * (
            -1 + math.sqrt(17) + math.sqrt(2 * (17 - math.sqrt(17))) + 2 * math.sqrt(2 * (17 + math.sqrt(17)))))

# 第四题
print_()

# 第五题
print_()

# 第六题：要求编写两式比较的表达式，输出为True或False
print_()

# 第七题
print_()
print_()

# 第八题：要求编写两式比较的表达式，输出为True或False
print_()
# ********** End ********** #
