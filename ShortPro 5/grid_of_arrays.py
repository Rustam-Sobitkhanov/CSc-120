"""
File: grid_of_arrays.py
Author: Rustambek Sobithanov
Purpose: The following function returns an array with multiple references
         to different arrays and objects
"""


def grid_of_arrays():
    last_list = [None, (2, 2), None]
    list8 = [last_list, (1, 2), None]
    list7 = [list8, (0, 2), None]
    list6 = [None, (2, 1), last_list]
    list5 = [list6, (1, 1), list8]
    list4 = [list5, (0, 1), list7]
    list3 = [None, (2, 0), list6]
    list2 = [list3, (1, 0), list5]
    the_list = [list2, (0, 0), list4]
    return the_list
