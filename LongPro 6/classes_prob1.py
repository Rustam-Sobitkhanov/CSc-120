"""
File: classes_prob1.py
Author: Rustambek Sobithanov
Purpose: The following has some classes (Simplest, Rotate, and Band)
         which serve some purpose.
"""


class Simplest:
    """
    The class has three trivial objects: a, b, c. It has a constructor
    which takes those three as parameters (in the order a,b,c), and sets the
    public fields in the object. It has no other methods.
    """
    def __init__(self, first, second, third):
        self.a = first
        self.b = second
        self.c = third


class Rotate:
    """
    The class stores three different values, but rotates them, round-robin
    fashion, when you ask it to.

    The methods:
        __init__(self, first,second,third): - Constructor. It should store the
                                              three values in private fields.
        get_first(self):
        get_second(self):                   - Getters, for the three values,
        get_third(self):                      as they currently

        rotate(self):                       - Rotates the first, second,
                                              and third values The first
                                              should move to the end (the
                                              third position), and the second
                                              and third should move up.

    """
    def __init__(self, first, second, third):
        self._first = first
        self._second = second
        self._third = third

    def get_first(self):
        return self._first

    def get_second(self):
        return self._second

    def get_third(self):
        return self._third

    def rotate(self):
        # resetting the values of the variables
        self._first, self._second, self._third = self._second,\
                                                 self._third, self._first


class Band:
    """
    This class represents a musical group. It can contain one singer, one
    drummer, and any number of guitar players. When the object is created,
    it will only contain a singer; use getters and setters to update the
    various band members.

    The methods:
        __init__(self, singer):                         - Constructor. It should store the singer
                                                          it is passed, set the drummer to None, and
                                                          record that the band does not (yet) have any
                                                          guitar players.
        get_singer(self):
        set_singer(self, new_singer):                   - These are the getters and setters for the singer
        get_drummer(self):                                and the drummer.
        set_drummer(self, new_drummer):

        add_guitar_player(self, new_guitar_player):     - adds a guitar player and stores it in a list
        fire_all_guitar_players(self):                  - sets the len of the list to 0
        get_guitar_players(self):                       - duplicates the list of guitar players and
                                                          returns it
        play_music(self):                               - prints notes based on some conditions
    """
    def __init__(self, singer):
        self.drummer = None
        self.singer = singer
        self.guitar_player = []

    def get_singer(self):
        return self.singer

    def set_singer(self, new_singer):
        self.singer = new_singer

    def get_drummer(self):
        return self.drummer

    def set_drummer(self, new_drummer):
        self.drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        self.guitar_player.append(new_guitar_player)

    def fire_all_guitar_players(self):
        self.guitar_player = []

    def get_guitar_players(self):
        # duplicating a list of guitar players
        a_list = []
        for player in self.guitar_player:
            a_list.append(player)
        return a_list

    def play_music(self):
        # prints notes based on the given conditions
        if self.singer == 'Frank Sinatra':
            print('Do be do be do')
        elif self.singer == 'Kurt Cobain':
            print('bargle nawdle zouss')
        else:
            print('La la la')
        if self.drummer is not None:
            print('Bang bang bang!')
        if len(self.guitar_player) > 0:
            for player in self.guitar_player:
                print('Strum!')
