"""
File: pipes_static_A.py
Author: Rustambek Sobithanov
Purpose: The following lines depict random pipes/squares in a tiles of Grid Pipe each time its run.
"""
from graphics import *
import random


def main():
    gui = graphics(500, 500, 'Pipe Grid')
    gui.rectangle(0, 0, 600, 600, "grey30")
    parameterized1(gui)
    parameterized2(gui)
    draw_lines(gui)
    gui.primary.mainloop()


def draw_lines(gui):
    """
    separates tiles using white lines
    :param gui: reference to the Pipe Grid
    """
    coord_x = 0
    while coord_x < 600:
        gui.line(coord_x, -10, coord_x, 520, 'white', 3)
        coord_x += 100
    coord_y = 0
    while coord_y < 600:
        gui.line(-10, coord_y, 520, coord_y, 'white', 3)
        coord_y += 100


def draw_tile(gui, x_coord, y_coord, north, south, west, east, add_blue, square):
    """
    draws pipes/squares at a given coordinate
    """
    draw_exits(gui, x_coord, y_coord, north, south, west, east, add_blue)
    if square:
        draw_square(gui, x_coord, y_coord, add_blue)


def draw_square(gui, x_coord, y_coord, add_blue):
    """
    draws a square at the given coordinate
    :param gui:reference to the canvas Pipe Grid
    :param x_coord: x-coordinate
    :param y_coord: y-coordinate
    :param add_blue: boolean value of True or False
    """
    start_x = x_coord + 35
    start_y = y_coord + 35
    color = 'black'
    if add_blue:
        color = 'blue'
    gui.rectangle(start_x, start_y, 30, 30, color)


def draw_exits(gui, x_coord, y_coord, north, south, west, east, add_blue):
    """
    draws pipes in a tile depending on the boolean value passed to the function
    :param gui: reference to the canvas Grid Pipe
    :param x_coord: x-coordinate
    :param y_coord: y-coordinate
    :param north: boolean value of True or False
    :param south: boolean value of True or False
    :param west: boolean value of True or False
    :param east: boolean value of True or False
    :param add_blue: boolean value of True or False
    """
    vert_start_x = x_coord + 50
    hor_start_y = y_coord + 50
    color = 'black'
    if add_blue:
        color = 'blue'
    if north:
        gui.line(vert_start_x, y_coord, vert_start_x, hor_start_y, color, 10)
    if south:
        gui.line(vert_start_x, y_coord + 100, vert_start_x, hor_start_y, color, 10)
    if west:
        gui.line(x_coord, hor_start_y, vert_start_x + 5, hor_start_y, color, 10)
    if east:
        gui.line(x_coord + 100, hor_start_y, vert_start_x - 5, hor_start_y, color, 10)


def parameterized1(gui):
    """
    randomly depicts pipes/squares depending on the value of the function 'bool(random.getrandbits(1))'
    :param gui: Reference the canvas
    """
    draw_tile(gui, x_coord=0, y_coord=0, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=bool(random.getrandbits(1)), east=bool(random.getrandbits(1)), add_blue=True, square=False)
    draw_tile(gui, x_coord=100, y_coord=0, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=bool(random.getrandbits(1)), east=bool(random.getrandbits(1)),
              add_blue=bool(random.getrandbits(1)), square=bool(random.getrandbits(1)))
    draw_tile(gui, x_coord=200, y_coord=0, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=bool(random.getrandbits(1)), east=bool(random.getrandbits(1)),
              add_blue=bool(random.getrandbits(1)), square=bool(random.getrandbits(1)))
    draw_tile(gui, x_coord=300, y_coord=0, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=True, east=bool(random.getrandbits(1)), add_blue=False, square=False)
    draw_tile(gui, x_coord=400, y_coord=0, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=False, east=bool(random.getrandbits(1)), add_blue=False, square=True)

    draw_tile(gui, x_coord=0, y_coord=100, north=True, south=bool(random.getrandbits(1)),
              west=bool(random.getrandbits(1)), east=False, add_blue=bool(random.getrandbits(1)), square=False)
    draw_tile(gui, x_coord=100, y_coord=100, north=bool(random.getrandbits(1)), south=True,
              west=bool(random.getrandbits(1)), east=bool(random.getrandbits(1)), add_blue=True, square=True)
    draw_tile(gui, x_coord=200, y_coord=100, north=bool(random.getrandbits(1)), south=False,
              west=True, east=bool(random.getrandbits(1)), add_blue=bool(random.getrandbits(1)), square=True)
    draw_tile(gui, x_coord=300, y_coord=100, north=bool(random.getrandbits(1)), south=False,
              west=bool(random.getrandbits(1)), east=True, add_blue=bool(random.getrandbits(1)), square=False)
    draw_tile(gui, x_coord=400, y_coord=100, north=bool(random.getrandbits(1)), south=False,
              west=False, east=bool(random.getrandbits(1)), add_blue=False, square=bool(random.getrandbits(1)))

    draw_tile(gui, x_coord=0, y_coord=200, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=True, east=bool(random.getrandbits(1)), add_blue=bool(random.getrandbits(1)), square=False)
    draw_tile(gui, x_coord=100, y_coord=200, north=bool(random.getrandbits(1)), south=True,
              west=False, east=bool(random.getrandbits(1)), add_blue=True, square=bool(random.getrandbits(1)))
    draw_tile(gui, x_coord=200, y_coord=200, north=bool(random.getrandbits(1)), south=True,
              west=bool(random.getrandbits(1)), east=False, add_blue=bool(random.getrandbits(1)), square=True)


def parameterized2(gui):
    """
    randomly depicts pipes/squares depending on the value of the function 'bool(random.getrandbits(1))'
    :param gui: Reference the canvas
    """
    draw_tile(gui, x_coord=300, y_coord=200, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=bool(random.getrandbits(1)), east=True, add_blue=bool(random.getrandbits(1)), square=False)
    draw_tile(gui, x_coord=400, y_coord=200, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=True, east=bool(random.getrandbits(1)), add_blue=False, square=bool(random.getrandbits(1)))

    draw_tile(gui, x_coord=0, y_coord=300, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=bool(random.getrandbits(1)), east=bool(random.getrandbits(1)), add_blue=True, square=False)
    draw_tile(gui, x_coord=100, y_coord=300, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=True, east=True, add_blue=bool(random.getrandbits(1)), square=bool(random.getrandbits(1)))
    draw_tile(gui, x_coord=200, y_coord=300, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=bool(random.getrandbits(1)), east=True, add_blue=True, square=bool(random.getrandbits(1)))
    draw_tile(gui, x_coord=300, y_coord=300, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=False, east=bool(random.getrandbits(1)), add_blue=bool(random.getrandbits(1)), square=False)
    draw_tile(gui, x_coord=400, y_coord=300, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=True, east=bool(random.getrandbits(1)), add_blue=False, square=bool(random.getrandbits(1)))

    draw_tile(gui, x_coord=0, y_coord=400, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=False, east=bool(random.getrandbits(1)), add_blue=bool(random.getrandbits(1)), square=True)
    draw_tile(gui, x_coord=100, y_coord=400, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=True, east=bool(random.getrandbits(1)), add_blue=bool(random.getrandbits(1)), square=False)
    draw_tile(gui, x_coord=200, y_coord=400, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=False, east=bool(random.getrandbits(1)), add_blue=False, square=bool(random.getrandbits(1)))
    draw_tile(gui, x_coord=300, y_coord=400, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=bool(random.getrandbits(1)), east=False, add_blue=False, square=bool(random.getrandbits(1)))
    draw_tile(gui, x_coord=400, y_coord=400, north=bool(random.getrandbits(1)), south=bool(random.getrandbits(1)),
              west=bool(random.getrandbits(1)), east=False, add_blue=bool(random.getrandbits(1)), square=True)


main()
