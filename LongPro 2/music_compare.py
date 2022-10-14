"""
File: music_compare.py
Author: Rustambek Sobithanov
Purpose: The following program uses functions from utils.py to find the similarity
         level of musics
"""

from utils import *


def main():
    file_name = input('file: ')
    sequence_num = int(input('n: '))
    the_file = open(file_name, 'r')
    content = read_file(the_file)
    name2, ids2, melody2, slices1, slices2 = song_list(sequence_num, content)
    result_melodies(content, name2, ids2, melody2)
    sets(slices1, slices2)


def song_list(sequence_num, content):
    """
    compares musics and prints information about them
    also, finds the most similar musics
    :param sequence_num: integer determining the length of the slices
    :param content: the given file
    :return: name, id, melody notes, a list of slices of the most similar song
             and a list of slices of the first song
    """
    print("--- SONG LIST ---")
    for i in range(len(content)):
        print(f'id={content[i][0]} info="{content[i][1]}" notes={content[i][2]}')
    print()
    print("--- COMPARISONS ---")
    most_similar = 0
    for i in range(1, len(content)):
        result = compare_melodies(content[0][2], content[i][2], sequence_num)
        print(f'id_a={content[0][0]} id_b={content[i][0]} similarity={result}')
        if result > most_similar:
            most_similar = result

            ids2 = content[i][0]

            name2 = content[i][1]

            melody2 = content[i][2]

            slices1 = get_slices(content[0][2], sequence_num)
            slices2 = get_slices(content[i][2], sequence_num)
    return name2, ids2, melody2, slices1, slices2


def result_melodies(content, name2, ids2, melody2):
    """
    prints result of the comparison, ids of most similar songs and their notes
    :param content: the given file
    :param name2: name of the most similar song
    :param ids2: id of the most similar song
    :param melody2: a list of notes of the most similar song
    """
    print()
    print('--- RESULT ---')
    print('Most similar songs:')
    print(f'  {content[0][1]}')
    print(f'  {name2}')

    print()
    print(f'  ids: {content[0][0]}')
    print(f'  ids: {ids2}')

    print()
    print('Melodies:')
    print(f'  {" ".join(content[0][2])}')
    print(f'  {" ".join(melody2)}')


def sets(slices1, slices2):
    """
    prints resulting sets from sliced notes
    :param slices1: a list of sliced notes from the first song
    :param slices2: a list of sliced notes from the most similar song
    """
    print()
    set1 = set()
    for elem in slices1:
        set1.add(tuple(elem))
    set2 = set()
    for elem in slices2:
        set2.add(tuple(elem))

    print('Set 1')
    for elem in sorted(set1):
        print(f'  {" ".join(list(elem))}')
    print()
    print('Set 2')
    for elem in sorted(set2):
        print(f'  {" ".join(list(elem))}')


main()
