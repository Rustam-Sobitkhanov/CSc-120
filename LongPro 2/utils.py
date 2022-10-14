"""
File: utils.py
Author: Rustambek Sobithanov
Purpose: The following program consists of functions which help to compare music notes and find
         the most similar music to the first one given.
"""


def read_file(the_file):
    """
    reads the file and separates its info into a list of tuples
    :param the_file: the given file
    :return: a list of tuples
    """
    content = []
    music_info = the_file.readlines()
    i = 0
    while i < len(music_info):
        for element in music_info[i].split():
            if element.isnumeric():
                song_id = element
                break
        song_name = music_info[i].split(str(song_id))[1].strip()
        i += 1
        notes = music_info[i].strip()
        notes_list = []
        for note in notes.split():
            notes_list.append(note)
        i += 2
        all_in_one = (int(song_id), song_name, notes_list)
        content.append(all_in_one)
    return content


def get_slices(data, n):
    """
    takes data of notes and separates them into slices with the given integer length
    :param data: a list of all the notes as separate strings
    :param n: integer specifying the length of the slices
    :return: a list of sliced notes
    """
    slices = []
    for i in range(len(data) - n + 1):
        chunks = []
        for j in range(n):
            chunks.append(data[i + j])
        slices.append(chunks)
    return slices


def compare_sets(a, b):
    """
    takes two sets and determines how similar they are
    :param a: set of sliced notes of the first song
    :param b: set of sliced notes of another song
    :return: a float 0.0-1.0, determining the similarity level
    """
    intersection = len(a.intersection(b))
    union = (len(a) + len(b)) - intersection
    return float(intersection) / union


def compare_melodies(m1, m2, n):
    """
    uses two other functions to get the similarity level of songs
    :param m1: a list of notes of the first song
    :param m2: a list of notes of another song
    :param n: integer determining the length of the slices
    :return: a float 0.0-1.0, determining the similarity level
    """
    output1 = get_slices(m1, n)
    output2 = get_slices(m2, n)
    changed1 = set()
    changed2 = set()
    for elem in output1:
        changed1.add(tuple(elem))
    for elem in output2:
        changed2.add(tuple(elem))
    similarity = compare_sets(changed1, changed2)
    return similarity
