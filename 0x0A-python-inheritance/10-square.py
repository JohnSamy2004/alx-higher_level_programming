ass square from rectangle
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
        square inerits from BaseGeometry
        Attributes:
            size must be private. No getter or setter
            size must be a positive integer, validated by integer_validator

        Methods:
            __init__ - initialises the square.
    """
    def __init__(self, size):
        '''initialises Square'''
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        '''area of square'''
        return (self.__size * self.__size)
