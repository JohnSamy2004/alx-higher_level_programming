#!/usr/bin/python3
import json
'''convert a JSON string to a Python data structure'''


def to_json_string(my_obj):
    '''json to string'''
    return json.loads(my_obj)
