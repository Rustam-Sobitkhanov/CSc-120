"""
File: indentation_print.py
Author: Rustambek Sobithanov
Purpose: The following lines of code accepts a particular input from
         the user until the user types 'quit', and each time the user
         gives an input, it calculates the number of spaces at the
         beginning of the input and prints it out.
"""


while True:
    space_count = 0
    stuff = input()
    if stuff.strip() == 'quit':
        break
    else:
        for i in range(len(stuff)):
            if stuff[i] == ' ':
                space_count += 1
            else:
                break
    print(space_count)
