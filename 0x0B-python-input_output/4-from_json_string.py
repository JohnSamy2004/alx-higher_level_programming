#!/usr/bin/python3
'''convert a JSON string to a Python data structure'''


import json


def from_json_string(my_str):
    '''json to string'''
    return (json.dumps(my_str))
