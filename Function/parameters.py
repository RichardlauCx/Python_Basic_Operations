# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : ©RichardLau_Cx
#  @ file   : Richard.py
#  @ IDE    : PyCharm

i = 0


def distance(*args):
    """
    Output multidimensional coordinate values for each dimension
    :param args: Multidimensional coordinate，n the form of a tuple
    :return: None
    """
    global i
    print("Dimension coordinate the situation that has been passed in parameter:")
    for arg in args[0]:
        i += 1
        print("Dimension_%d: %d" % (i, arg))


if __name__ == '__main__':
    Dimension_coordinates = 5, 2, 0, 1, 3, 1, 4  # for example：(5, 2, 0, 1, 3, 1, 4)
    # run = 'distance' + str(Dimension_coordinates) + ''
    distance(Dimension_coordinates)
    # print(run)  # passed value call
