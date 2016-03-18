"""
File: heaviside.py

Copyright (c) 2016 Francis Agustin

License: MIT

Implement Heaviside function and test implementation on values.
"""

def H(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

print H(-10)
print H(-10**-15)
print H(0)
print H(10**-15)
print H(10)

def test_H(x):
    if H(-10) != 0:
        print "ERROR"
    if H(-10**-15) != 0:
        print "ERROR"
    if H(0) != 1:
        print "ERROR"
    if H(10**-15) != 1:
        print "ERROR"
    if H(10) != 1:
        print "ERROR"
    else:
        print "Well Done!"
