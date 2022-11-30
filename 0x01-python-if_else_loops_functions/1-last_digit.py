#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of " + str(number) + " is "
if number < 0:
    lastdigit = (-number % 10) * -1
else:
    lastdigit = number % 10
if lastdigit > 5:
    print(f"{str} {lastdigit} and is greater than 5")
elif lastdigit == 0:
    print(f"{str} {lastdigit} and is zero")
else:
    print(f"{str} {lastdigit} and is less than 6 and not 0")
