"""
File: annoying_recursion_part2.py
Author: Rustambek Sobithanov
Purpose: The following functions meet the requirements of LongPro 8
"""


def annoying_triangleNumbers(n):
    """
    calculates the sum of all the numbers till and including the given number
    :param n: an integer
    :return: an integer which is described above
    """
    if n in [0, 1, 2, 3]:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 3
        else:
            return 6
    elif n in [4, 5, 6]:
        if n == 4:
            return 4 + annoying_triangleNumbers(3)
        elif n == 5:
            return 5 + annoying_triangleNumbers(4)
        else:
            return 6 + annoying_triangleNumbers(5)
    elif n >= 7:
        return n + annoying_triangleNumbers(n - 1)


def annoying_fibonacci_sequence(n):
    """
    calculates and returns the list of fibonacci numbers
    :param n: an integer
    :return: a list which is described above
    """
    if n in [0, 1, 2, 3]:
        if n == 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            return [0, 1, 1]
    elif n in [4, 5, 6]:
        if n == 4:
            last_int = annoying_fibonacci_sequence(3)
            return annoying_fibonacci_sequence(3) + [last_int[-1] + last_int[-2]]       # second part of the calculation
        elif n == 5:                                                                    # gives the n-th fib number
            last_int = annoying_fibonacci_sequence(4)
            return annoying_fibonacci_sequence(4) + [last_int[-1] + last_int[-2]]
        else:
            last_int = annoying_fibonacci_sequence(5)
            return annoying_fibonacci_sequence(5) + [last_int[-1] + last_int[-2]]
    elif n >= 7:
        last_int = annoying_fibonacci_sequence(n - 1)
        return annoying_fibonacci_sequence(n - 1) + [last_int[-1] + last_int[-2]]


def annoying_valley(n):
    """
    prints out the shape of a "valley" in the shape of a V pointing right
    :param n: an integer determining the size of the shape
    """
    if n in [0, 1, 2, 3]:
        if n == 1:
            print('*')
        elif n == 2:
            print('./')
            print('*')
            print('.\\')
        elif n == 3:
            print('../')
            print('./')
            print('*')
            print('.\\')
            print('..\\')
    elif n in [4, 5, 6]:
        if n == 4:
            print('.../')
            annoying_valley(3)
            print('...\\')
        elif n == 5:
            print('..../')
            annoying_valley(4)
            print('....\\')
        else:
            print('...../')
            annoying_valley(5)
            print('.....\\')
    elif n >= 7:
        print('.' * (n - 1) + '/')
        annoying_valley(n - 1)
        print('.' * (n - 1) + '\\')

