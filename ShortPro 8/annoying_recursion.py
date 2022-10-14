"""
File: annoying_recursion.py
Author: Rustambek Sobithanov
Purpose: The following functions showcase the algorithms which are required in
         the specs of ShortPro 8
"""


def annoying_factorial(n):
    if n in [0, 1, 2, 3]:
        if n in [0, 1]:
            return 1
        elif n == 2:
            return 2
        else:
            return 6
    elif n in [4, 5, 6]:
        if n == 6:
            return 6 * annoying_factorial(5)
        elif n == 5:
            return 5 * annoying_factorial(4)
        elif n == 4:
            return 4 * annoying_factorial(3)
    elif n >= 7:
        return n * annoying_factorial(n - 1)


def annoying_fibonacci(n):
    if n in [0, 1, 2, 3]:
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1
        if n == 3:
            return 2
    elif n in [4, 5, 6]:
        if n == 6:
            return annoying_fibonacci(5) + annoying_fibonacci(4)
        if n == 5:
            return annoying_fibonacci(4) + annoying_fibonacci(3)
        if n == 4:
            return annoying_fibonacci(3) + annoying_fibonacci(2)
    elif n >= 7:
        return annoying_fibonacci(n - 1) + annoying_fibonacci(n - 2)


def annoying_climbUp(n):
    if n in [0, 1, 2, 3]:
        if n == 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 2]
        return [1, 2, 3]
    elif n in [4, 5, 6]:
        if n == 4:
            return [1, 2, 3, 4]
        elif n == 5:
            return [1, 2, 3, 4, 5]
        return [1, 2, 3, 4, 5, 6]
    elif n >= 7:
        return annoying_climbUp(n - 1) + [n]


def annoying_climbDownUp(n):
    if n in [0, 1, 2, 3]:
        if n == 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [2, 1, 2]
        return [3, 2, 1, 2, 3]
    elif n in [4, 5, 6]:
        if n == 4:
            return [4, 3, 2, 1, 2, 3, 4]
        elif n == 5:
            return [5, 4, 3, 2, 1, 2, 3, 4, 5]
        return [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]
    elif n >= 7:
        return [n] + annoying_climbDownUp(n - 1) + [n]

