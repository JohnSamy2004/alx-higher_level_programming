#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for index, Value in enumerate(my_list):
        if search == Value:
            new[index] = replace
    return new

