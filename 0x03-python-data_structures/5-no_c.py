#!/usr/bin/python3
def no_c(my_string):
    noCstr = ""
    for i in my_string:
        if (i != 'c') and (i != 'C'):
            noCstr += i
    return (noCstr)
