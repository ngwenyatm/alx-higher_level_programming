#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastNambah = (number % 10)
elif number < 0:
    lastNambah = (number % -10)
if lastNambah > 5:
    print(f"Last digit of {number} is {lastNambah} and is greater than 5")
elif lastNambah == 0:
    print(f"Last digit of {number} is {lastNambah} and is 0")
else:
    print(f"Last digit of {number} is {lastNambah} and is less than 6 and not 0")
