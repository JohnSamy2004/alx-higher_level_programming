#!/usr/bin/python3
''' lookup function'''


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj: The object to inspect.

    Returns:
    A list object containing the names of available attributes and methods.
    """
    return dir(obj)
