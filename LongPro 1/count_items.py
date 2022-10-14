"""
File: swap.py
Author: Rustambek Sobithanov
Purpose: The following function reads a file the contents of which are a string and an integer, performs
         some operations on them, prints what happens in each stage of the operation and the ending result.
"""


def main():
    file_name = input('File to scan: ').strip()
    a_file = open(file_name, 'r')

    str_int = separation(a_file)

    tuple_list = []
    print('STEP 1: THE ORIGINAL DICTIONARY')
    for key in sorted(str_int.keys()):
        print(f'Key: {key} Value: {str_int[key]}')
        my_tuple = (str_int[key], key)
        tuple_list.append(my_tuple)
    print()

    print('STEP 2: A LIST OF VALUE->KEY TUPLES')
    print(tuple_list)
    print()

    print('STEP 3: AFTER SORTING')
    print(sorted(tuple_list))
    print()

    print('STEP 4: THE ACTUAL OUTPUT')
    for row in sorted(tuple_list):
        print(f'{row[1]} {row[0]}')


def separation(a_file):
    """
    the function reads the given file and separates its content to a string and its associated integer value
    then it puts them into a dictionary as a key and value
    :param a_file: a file each line of which is a pair of string and integer
    :return: a dictionary with the contents being the strings of the file and their associated integer values
    """
    data = a_file.readlines()
    str_int = {}
    for info in data:
        if len(info) <= 1 or info.strip().split()[0] == '#':
            continue
        else:
            pair = info.strip('\n').split()
            if pair[0] in str_int:
                str_int[pair[0]] += int(pair[1])
            else:
                str_int[pair[0]] = int(pair[1])
    return str_int


main()
