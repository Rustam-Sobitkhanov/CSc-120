"""
File: road.py
Author: Rustambek Sobithanov
Purpose: The following lines of codes draw a simple animation, which is a movement of cars
         on a highway.
"""
from graphics import graphics
import random


def main():

    gui = graphics(800, 600, 'Road')
    x_coord = 0
    red = random.randint(0, 250)            # getting random rgb values so that I can
    green = random.randint(0, 250)          # use it to get a random color when needed
    blue = random.randint(0, 250)

    while x_coord < 5000:
        gui.clear()
        gui.rectangle(-200, -200, 1000, 1000, '#FEF7DC')
        gui.rectangle(-200, 100, 1000, 400, '#171010')
        lines(gui, x_coord)
        car(gui, x_coord / 5, y_coord=250,
            color=gui.get_color_string(red, green, blue))
        car(gui, x_coord / 4, y_coord=0,
            color=gui.get_color_string(red, blue, green))
        x_coord += 20
        if x_coord > 4000:                  # controls the continuity of the animation
            x_coord = -1500
            red = random.randint(0, 250)
            green = random.randint(0, 250)
            blue = random.randint(0, 250)
        gui.update_frame(60)

def car(gui, x_coord, y_coord, color):
    """
    draws a car
    :param gui: reference to the canvas
    :param x_coord: int representing the x-coordinate
    :param y_coord: int representing the y-coordinate
    :param color: reference to the random rgb color for the car
    """
    gui.ellipse(100 + x_coord, 470 - y_coord, 50, 50, 'white')
    gui.ellipse(250 + x_coord, 470 - y_coord, 50, 50, 'white')
    gui.rectangle(50 + x_coord, 420 - y_coord, 250, 50, color)
    gui.rectangle(100 + x_coord, 370 - y_coord, 150, 50, color)
    gui.rectangle(190 + x_coord, 375 - y_coord, 50, 40, '#B5EAEA')


def lines(gui, x_coord):
    """
    draws the white lines in the middle of the highway
    :param gui: reference to the canvas
    :param x_coord: int representing the x-coordinate
    """
    add_to_x = 0
    while add_to_x < 10000:
        gui.rectangle(-1500 + add_to_x - x_coord, 290, 40, 20, 'white')
        add_to_x += 100


main()
