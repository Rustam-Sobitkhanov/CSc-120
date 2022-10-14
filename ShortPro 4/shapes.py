"""
File: shapes.py
Author: Rustambek Sobithanov
Purpose: The following functions are written in a way to meet all the spec requirements of the Short PA 4.
         Basically, what they do is give the code version of the drawings given in the project specs
"""


def shape_alpha():
    given_data = [[10, 20], 30, 40, [50, 60]]
    return given_data


def shape_bravo():
    num1 = [123, 456]
    num2 = [789, 1024]
    return [[num1, num2], [num2, num1]]


def shape_charlie(arg1):
    charlie1 = [arg1, arg1]
    charlie2 = [arg1, arg1]
    charlie3 = [arg1, arg1]
    return [[charlie1, charlie2], charlie3]


def shape_delta(arg1, arg2):
    small_arg1 = [arg1]
    small_arg2 = [arg2]
    med_1 = [arg1, small_arg2]
    med_2 = [med_1, small_arg1]
    num = [17]
    result = [arg1, arg2, med_2, num]
    return result


def shape_echo(arg1, arg2, arg3):
    el1 = [arg1, None]
    data = el1
    el3 = [arg3, data]
    el2 = [arg2, el3]
    el1[1] = el2

    return data
