#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list
    if idx >= len(my_list) or idx < 0:
        return new
    else:
        new[idx] = element
        return new
