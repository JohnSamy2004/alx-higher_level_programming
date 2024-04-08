#!/usr/bin/python3
"""
This module has one function that adds up 2 integers
"""

def add_integer(a, b=98):
    '''Returns an integer: the addition of a and b as integer
    Args:
        a: first argument
        b: second argument
    Returns:
        Sum of a and b as an integer
    if a not int or b not int:
        Raise:
          TypeError: a must be an integer or b must be an integer
    '''
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
