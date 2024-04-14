#!/usr/bin/python3
'''append to a file'''


def append_write(filename="", text=""):
    '''this write file and appends
        the new text to the file'''
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
