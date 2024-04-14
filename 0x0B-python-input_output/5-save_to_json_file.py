#!/usr/bin/python3
'''save as json file'''


import json


def save_to_json_file(my_obj, filename):
    '''save as json'''
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)
