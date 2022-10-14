"""
File: classes_prob2.py
Author: Rustambek Sobithanov
Purpose: The following class gives the representation of a color in different
         formats.
"""


class Color:
    """
    This class represents and RGB color. It stores the red, green, and blue
    components of the color as integers ([0,255] inclusive on both ends).

    The methods:
        __init__(self, r,g,b):              - Constructor. Accepts values of r,g,n and if their value
                                              exceeds 255 it sets them to 255 and if their value is
                                              negative it sets them to 0. As otherwise, it leaves them
                                              as they are.
        __str__(self):                      - returns a string in the form of, "rgb(125,0,255)"
        html_hex_color(self):               - returns a string in the form of, "#FF0034"
        get_rgb(self):                      - returns the red, green, blue components as a tuple
        set_standard_color(self, name):     - accepts a color name as a string and changes RGB values
                                              accordingly.
        remove_red(self):                   - sets the red component of the current color to 0.
    """
    def __init__(self, r, g, b):
        """
        creates private variables for Red, Green, and Blue. Also, it
        contains a function which, if needed, sets the values of Red,
        Green, or Blue to either 0 or 255.
        :param r: an integer value
        :param g: an integer value
        :param b: an integer value
        """
        def correct_color(color):
            """
            if color is < 0, it sets the value of color to 0, and if
            color is > 255, it sets its value to 255
            :param color: an integer value
            :return: 0 or 255
            """
            if color < 0:
                color = 0
            else:
                color = 255
            return color

        if r < 0 or r > 255:
            self._red = correct_color(r)
        else:
            self._red = r

        if g < 0 or g > 255:
            self._green = correct_color(g)
        else:
            self._green = g

        if b < 0 or b > 255:
            if b < 0:
                self._blue = correct_color(b)
        else:
            self._blue = b

    def __str__(self):
        a_tuple = (self._red, self._green, self._blue)
        return f'rgb{a_tuple}'

    def html_hex_color(self):
        """
        uses the below formula to find hex color code for a given integer
        value of RGB
        :return: a string form of hex color code
        """
        red = f"{self._red:02X}"
        green = f"{self._green:02X}"
        blue = f"{self._blue:02X}"
        return f'#{red}{green}{blue}'

    def get_rgb(self):
        return (self._red, self._green, self._blue)

    def set_standard_color(self, name):
        """
        changes the RGB values depending on the name of the color
        :param name: a string - name of a color
        """
        if name.lower() == 'white':
            self._red = 255
            self._green = 255
            self._blue = 255
        elif name.lower() == 'red':
            self._red = 255
            self._green = 0
            self._blue = 0
        elif name.lower() == 'yellow':
            self._red = 255
            self._green = 255
            self._blue = 0
        elif name.lower() == 'black':
            self._red = 0
            self._green = 0
            self._blue = 0

    def remove_red(self):
        self._red = 0

