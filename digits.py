"""
File: digits.py

Copyright (c) 2016 Francis Agustin

License: MIT

A function `digits(n)` that calculates the number of digits
(plus the sign for negative numbers) in an integer.
"""

inp = raw_input("Please enter an integer, positive or negative: ")
x = int (inp)

def digits(n):
    return len(str(x))

print digits(n)

stopper = raw_input("Hit <enter> to quit.")
