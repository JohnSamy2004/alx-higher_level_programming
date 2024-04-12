#!/usr/bin/python3
'''an empty class'''


class BaseGeometry:
    '''represents Base Geometry'''
    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
    
    '''that validates value is integer or not'''
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
