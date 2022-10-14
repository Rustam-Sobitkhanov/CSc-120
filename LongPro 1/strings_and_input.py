"""
File: strings_and_input.py
Author: Rustambek Sobithanov
Purpose: Taking series of inputs and making operations based on them.
"""


def main():
    # taking an input from the user
    input_string = input('input string: ')

    # printing the length of the input string
    print(len(input_string))

    # printing the second character
    print(input_string[1])

    # printing the first 10 characters
    print(input_string[:10])

    # printing the last 5 characters
    print(input_string[-5:])

    # printing the string in all caps
    print(input_string.upper())

    # determining the characteristics of the input and printing a statement based on that
    if input_string[0].lower() in ['q', 'w', 'e', 'r', 't', 'y'] or \
            input_string[0].upper() in ['Q', 'W', 'E', 'R', 'T', 'Y']:
        print('QWERTY')
    elif input_string[0] in ['u', 'i', 'o', 'p']:
        print('UIOP')
    elif input_string[0].isalpha():
        print('LETTER')
    elif input_string[0].isdigit():
        print('DIGIT')
    else:
        print('OTHER')

    # taking 2 numeric inputs
    num1 = int(input())
    num2 = int(input())

    # printing the product of the above inputs
    print(num1 * num2)


main()
