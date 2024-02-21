#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    owner = None
    if not a_dictionary:
        return None
    else:
        for key, value in a_dictionary.items():
            value = int(value)
            if value > max:
                max = value
                owner = key
    return owner
