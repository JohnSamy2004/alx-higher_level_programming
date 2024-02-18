#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la = list(tuple_a)
    lb = list(tuple_b)
    while len(la) < 2:
        la[.append(0)]
    while len(lb) < 2:
        lb.append(0)
    list_c = [la[0] + lb[0], la[1] + lb[1]]
    return tuple(list_c)
