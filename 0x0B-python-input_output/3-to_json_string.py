#!/usr/bin/python3
'''convert a Python data structure to a JSON string'''


import json


def to_json_string(my_obj):
    '''string to json'''
    return (json.dumps(my_obj))
