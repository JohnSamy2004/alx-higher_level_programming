#!/usr/bin/python3
'''write file'''


def write_file(filename="", text=""):
    '''this write file writes text and
    if exist overwrite the content of the file'''
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
