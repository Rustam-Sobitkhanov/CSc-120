"""
File: swap.py
Author: Rustambek Sobithanov
Purpose: The following function takes a string input from the user, determines if its length is an odd or even
         number, and depending on that, it either just swaps the positions of 2 halves of the string or
         swaps the positions leaving the middle character in its own place.
"""


def main():
    str_input = input('Please give a string to swap: ').strip()
    half_num = int(len(str_input) / 2)
    if len(str_input) % 2 == 0:
        half1 = str_input[:half_num]
        half2 = str_input[half_num:]
        print(half2 + half1)
    else:
        half1 = str_input[:half_num]
        half2 = str_input[half_num + 1:]
        print(half2 + str_input[half_num] + half1)


main()
