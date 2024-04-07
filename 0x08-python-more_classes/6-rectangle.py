#!/usr/bin/python3
''' This defines a rectangle by: (based on 0-rectangle.py)'''


class Rectangle:
    '''Class :)'''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return ((self.width + self.height) * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.width == 0 or self.height == 0:
            return ("")

        else:
            rectangle_string = ""
            for i in range(self.height):
                rectangle_string += "#" * self.width + "\n"
            return rectangle_string[:-1]

    def __repr__(self):
        """Return the string representation of the Rectangle.
        Represents the rectangle in a format that can be recreated using eval()
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        self.number_of_instances -= 1
