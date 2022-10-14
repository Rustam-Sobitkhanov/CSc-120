"""
File: bob.py
Author: Rustambek Sobithanov
Purpose: The following functions take a text file as an input, search
         for palindromes from its context and print out the results.
"""


def main():
    file_name = input()
    try:
        a_file = open(file_name, 'r')
        words = extract_words(a_file)
        command = input()
        if command == 'dump':
            print('WORD LIST:')
            for word in sorted(set(words)):
                print(f'  {word}')
        else:
            command = int(command)
            one_word(words)
            two_or_three_words(words)
            print('PALINDROMES OF LENGTH 1    - length of candidate list: 0\n')
            the_rest(words, command)

    except:
        print("ERROR: Could not open the input file: " + file_name)


def extract_words(a_file):
    words = []
    for line in a_file:
        line = line.strip().split()
        for element in line:
            if len(element) > 1:
                for char in [',', "'", '.', '?', '/', '!', '-', '"']:
                    element = element.replace(char, "")
                if len(element) > 1:
                    words.append(element.lower())
    return words


def one_word(words):
    pal_words = []
    for word in words:
        if word == word[::-1]:
            pal_words.append(word)
    print('1-WORD PALINDROMES:')
    for word in sorted(pal_words):
        print(f'  {word}')
    print()


def two_or_three_words(words):
    long_pal_list = []
    for word1 in words:
        for word2 in words:
            pal = word1 + word2
            if pal == pal[::-1]:
                long_pal_list.append(pal)

    for word1 in words:
        for word2 in words:
            for word3 in words:
                pal = word1 + word2 + word3
                if pal == pal[::-1]:
                    long_pal_list.append(pal)
    print('2-WORD AND 3-WORD PALINDROMES:')
    for word in sorted(set(long_pal_list)):
        print(f'  {word}')
    print()


def the_rest(words, command):
    a_dict = {}
    for word in words:
        if len(word) <= command:
            if len(word) in sorted(a_dict):
                a_dict[len(word)].add(word)
            else:
                a_dict[len(word)] = set(word)
    print(a_dict)


main()
