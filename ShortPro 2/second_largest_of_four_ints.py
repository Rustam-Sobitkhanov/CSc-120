"""
File: second_largest_of_four.py
Author: Rustambek Sobithanov
Purpose: The following code takes a numeric input containing 4 numbers,
         finds the second largest of them all and prints it out.

"""


int_list = []
for i in range(4):
    integer = int(input())
    int_list.append(integer)
print(sorted(int_list)[2])