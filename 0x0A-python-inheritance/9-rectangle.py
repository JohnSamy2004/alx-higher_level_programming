#!/usr/bin/python3
"""
    8-rectangle: class Rectangle from BaseGeomerty
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle inerits from BaseGeometry
        Attributes:
            width (int): width of rectangle.
            height (int): height of rectangle.
        Methods:
            __init__ - initialises the Rectangle.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''area of rectangle'''
        return (self.__width * self.__height)

    def __str__(self):
        '''returns details of the Rectangle'''
        return (f"[{type(self)}] {self.__width}/{self.__height}")
