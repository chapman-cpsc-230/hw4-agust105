"""
File: histogram.py

Copyright (c) 2016 Francis Agustin

License: MIT

Defines `histogram()`, a procedure that takes a list of
positive integers and prints a histogram.
"""

ls = [4,9,13,5]
def hist(n):
    st = ""
    for i in range(n):
        st += "*"
    return st

for i in range (len(ls)):
    print hist(ls[i])

print ls
