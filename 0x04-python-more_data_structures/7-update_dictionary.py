#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key or value not in a_dictionary:
        a_dictionary[key] = value
    return a_dictionary
