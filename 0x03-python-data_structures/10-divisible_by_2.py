#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multi = []
    if my_list:
        for digint in my_list:
            multi.append(False if digint % 2 else True)
        return multi
