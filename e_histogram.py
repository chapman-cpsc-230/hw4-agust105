"""
File: e_histogram.py

Copyright (c) 2016 Francis Agustin

License: MIT

Using the `digits(n)` function you have written to improve
the histogram procedure to print a title and the number of
asterisks in each row.
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

print '''
n    |   DATA
-----+---------'''
print ls[0:1], " |", hist(ls[1])
print ls[1:2], " |", hist(ls[2])
print ls[2:3], "|", hist(ls[3])
print ls[3:4], " |", hist(len(ls))
