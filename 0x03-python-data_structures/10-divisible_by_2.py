#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    prod = []
    if my_list:
        for elem in my_list:
            prod.append(False if elem % 2 else True)
        return prod
