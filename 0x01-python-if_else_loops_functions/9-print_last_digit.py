#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        numbaMsila = (number % 10)
    elif number < 0:
        numbaMsila = (number % -10)
    print("{:d}".format(numbaMsila), end="")
    return numbaMsila
