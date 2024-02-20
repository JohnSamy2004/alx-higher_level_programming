#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    newlist = list(set(my_list))
    for i in newlist:
            sum += i
    return sum
