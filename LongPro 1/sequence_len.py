"""
File: sequence_len.py
Author: Rustambek Sobithanov
Purpose: The following function takes a series of numeric inputs from the user, finds where the order broke
         and prints how many numbers came in order.
"""


def main():
    int_nums = []
    input_repeat = True
    descending = True
    ascending = True
    ascending, int_nums = break_finder(input_repeat, int_nums, descending, ascending)
    overall = calculation(ascending, int_nums)
    print(overall)


def break_finder(input_repeat, int_nums, descending, ascending):
    """
    the function takes a numeric input from the user, checks for the type of order (ascending/descending) and finds
    the breaking point of the sequence
    :param input_repeat: a boolean value which controls if the very first while loop should continue or not
    :param int_nums: an empty list
    :param descending: a boolean value determining if the sequence is descending or not
    :param ascending: a boolean value determining if the sequence is ascending or not
    :return: a boolean value and a list of all the numeric inputs from the user
    """
    while input_repeat:
        nums = input().split()
        for element in nums:
            int_nums.append(int(element))

        if len(int_nums) > 1:
            count = 0
            descending = True
            ascending = True

            while (ascending and descending) and count < len(int_nums) - 1:
                current_num = int_nums[count]
                next_num = int_nums[count + 1]
                if current_num == next_num:
                    count += 1
                elif next_num > current_num:
                    descending = False
                    for i in range(len(int_nums) - 1):
                        if int_nums[i] > int_nums[i + 1]:
                            input_repeat = False
                else:
                    ascending = False
                    for i in range(len(int_nums) - 1):
                        if int_nums[i] < int_nums[i + 1]:
                            input_repeat = False
    return ascending, int_nums


def calculation(ascending, int_nums):
    """
    the function calculates how many numeric inputs were given in the order
    :param ascending: a boolean value
    :param int_nums: a list of all the numeric input values
    :return:
    """
    overall = 1
    if ascending:
        for i in range(len(int_nums) - 1):
            if int_nums[i] <= int_nums[i + 1]:
                overall += 1
            else:
                break
    else:
        for i in range(len(int_nums) - 1):
            if int_nums[i] >= int_nums[i + 1]:
                overall += 1
            else:
                break
    return overall


main()
