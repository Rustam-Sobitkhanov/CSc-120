"""
File: two_lines_of_words.py
Author: Rustambek Sobithanov
Purpose: The following code takes 2 inputs from the user and performs some
         operations based on them.
"""


input1 = input().split()
input2 = input().split()
print(f'The first line was: {input1}')
print(f'The second line was: {input2}')
print()
combo = input1 + input2
print(f'The combination of both lines had {len(combo)} words.')
print(f'The combined set of words was: {combo}')
print()
print(f'After sorting, the words were: {sorted(combo)}')
print()
print('Pairs:')
num = 0
while num < len(input1) and num < len(input2):
    print(f'{num}: {input1[num]}, {input2[num]}')
    num += 1
