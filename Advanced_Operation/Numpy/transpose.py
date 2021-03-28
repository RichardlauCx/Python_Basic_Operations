# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

import numpy as np

a = np.matrix([[1, 0], [0, 1]])
# print(a)
# print(a.T)
b = np.dot(a, a.T)
print(b)
