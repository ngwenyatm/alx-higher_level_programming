#!/usr/bin/python3
def number_keys(a_dictionary):
    numb = 0
    keyList = list(a_dictionary.keys())
    for i in keyList:
        numb = numb + 1
    return (numb)
