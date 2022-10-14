"""
File: twine.py
Author: Rustambek Sobithanov
Purpose: The following program tracks a person's path using a twine as they
         wander through a forest. The program is controlled by giving series
         of commands like 'n', 's', 'e', 'w', etc.
"""


def main():
    print('Please give the name of the obstacles filename, or - for none:')
    obstacle = input()
    obst_coord = handling_obstacles(obstacle)
    crossings = {}
    location_history = [(0, 0)]
    cur_pos = location_history[-1]
    calculating_operations(cur_pos, location_history, crossings, obst_coord)


def calculating_operations(cur_pos, location_history, crossings, obst_coord):
    """
    chooses what operation to perform based on the input
    :param cur_pos: x and y coordinate of a current position of a person
    :param location_history: list containing tuples of x and y coordinates
                             of all the places where the person has been
    :param crossings: a dictionary which keeps track of how many times the
                      twine has crossed a particular coordinate
    :param obst_coord: a list of tuples containing all the coordinates
                       of the obstacles on the way
    """
    while True:
        print(f'Current position: {cur_pos}')
        print(f'Your history:     {location_history}')
        print('What is your next command?')
        try:
            command = input()
        except:
            break
        if command in ['n', 's', 'e', 'w']:
            location_history = direction_commands(location_history,
                                        command, cur_pos, obst_coord)
        elif command == 'crossings':
            crossings = crossing(location_history)
            print(f'There have been {crossings[location_history[-1]]} times'
                  f' in the history when you were at this point.')
        elif command == 'back':
            crossings, location_history = \
                back(location_history, crossings)
        elif command == 'map':
            mapping(location_history, obst_coord)
        elif command == 'ranges':
            ranges(location_history)
        else:
            input_check(command)
        cur_pos = location_history[-1]
        print()


def input_check(command):
    """
    prints statements based on the type of the incorrect input
    :param command: input command given by the user
    """
    if len(command.split()) > 1:
        print('Your command should not contain more than 1 word!')
    elif len(command) == 0:
        print('You do nothing.')
    else:
        print(f'ERROR: Invalid command: {command}')


def direction_commands(location_history, command, cur_pos, obst_coord):
    """
    takes the coordinate of where the person has moved and appends it to
    the list
    :param location_history: list containing tuples of x and y coordinates
                             of all the places where the person has been
    :param command: input command given by the user
    :param cur_pos: x and y coordinate of a current position of a person
    :param obst_coord: a list of tuples containing all the coordinates
                       of the obstacles on the way
    :return: list containing tuples of x and y coordinates
             of all the places where the person has been
    """
    if command == 'n':
        x = cur_pos[0]
        y = cur_pos[1] + 1
    elif command == 's':
        x = cur_pos[0]
        y = cur_pos[1] - 1
    elif command == 'e':
        x = cur_pos[0] + 1
        y = cur_pos[1]
    elif command == 'w':
        x = cur_pos[0] - 1
        y = cur_pos[1]
    if (x, y) not in obst_coord:
        location_history.append((x, y))
    else:
        print('You could not move in that direction, '
              'because there is an obstacle in the way.')
        print('You stay where you are.')

    return location_history


def crossing(location_history):
    """
    keeps track of how many times the twine has crossed a particular
    coordinate
    :param location_history: list containing tuples of x and y coordinates
                             of all the places where the person has been
    :return: a dictionary which keeps track of how many times the
             twine has crossed a particular coordinate
    """
    crossings = {}
    for coord in location_history:
        if coord in crossings:
            crossings[coord] += 1
        else:
            crossings[coord] = 1
    return crossings


def back(location_history, crossings):
    """
    clears the coordinates of the earlier move if the person decides
    to move back to the previous position
    :param location_history: list containing tuples of x and y coordinates
                             of all the places where the person has been
    :param crossings: a dictionary which keeps track of how many times the
                      twine has crossed a particular coordinate
    :return: the same two parameters with their updated versions
    """
    if len(location_history) >= 2:
        crossings = crossing(location_history)
        crossings[location_history[-1]] -= 1
        location_history.pop()
        print("You retrace your steps by one space")
    else:
        print("Cannot move back, as you're at the start!")
    return crossings, location_history


def ranges(location_history):
    """
    gives information about how far the twine went
    :param location_history: list containing tuples of x and y coordinates
                             of all the places where the person has been
    """
    x_coords = []
    y_coords = []
    for coord in location_history:
        x_coords.append(coord[0])
        y_coords.append(coord[1])
    fur_north = sorted(y_coords)[-1]
    fur_south = sorted(y_coords)[0]
    fur_west = sorted(x_coords)[0]
    fur_east = sorted(x_coords)[-1]
    print(f'The furthest West your twine goes is {fur_west}')
    print(f'The furthest East your twine goes is {fur_east}')
    print(f'The furthest South your twine goes is {fur_south}')
    print(f'The furthest North your twine goes is {fur_north}')


def mapping(location_history, obst_coord):
    """
    draws the map of each step the person took while the program is running
    and each obstacle present
    :param location_history: list containing tuples of x and y coordinates
                             of all the places where the person has been
    :param obst_coord: a list of tuples containing all the coordinates
                       of the obstacles on the way
    """
    for y in range(6, -7, -1):
        string = '|'
        if y in [6, -6]:
            print('+-----------+')
        else:
            for x in range(-5, 7):
                if x == 6:
                    string += '|'
                    print(string)
                elif len(location_history) < 2:
                    if x == 0 and y == 0:
                        string += '+'
                    else:
                        string += ' '
                else:
                    if (x, y) in obst_coord:
                        string += 'X'
                    elif location_history[-1][0] == x and\
                            location_history[-1][1] == y:
                        string += '+'
                    elif x == 0 and y == 0:
                        string += '*'
                    else:
                        if (x, y) in location_history:
                            string += '.'
                        else:
                            string += ' '


def handling_obstacles(obstacle):
    """
    reads the file, if the file name is valid, where obstacle coordinates are
    located and appends each x-y coordinate as a tuple to the list
    :param obstacle: name of the file containing obstacle coordinates
    :return: a list of tuples containing all the coordinates
                       of the obstacles on the way
    """
    if obstacle != '-':
        try:
            file = open(obstacle, 'r')
            file_list = file.readlines()
            obst_coord = []
            for coord in file_list:
                coord = coord.strip().split()
                obst_coord.append((int(coord[0]), int(coord[1])))
            return obst_coord
        except:
            obst_coord = []
            return obst_coord
    else:
        obst_coord = []
        return obst_coord


main()