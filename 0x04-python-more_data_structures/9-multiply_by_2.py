#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = a_dictionary.copy()
    keyList = list(newDict.keys())
    for i in keyList:
        newDict[i] *= 2
    return (newDict)
