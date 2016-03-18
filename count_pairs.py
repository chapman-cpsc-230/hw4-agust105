"""
File: count_pairs.py

Copyright (c) 2016 Francis Agustin

License: MIT

Wrote a program that returns the number of
occurrences of a pair of bases in a DNA strand.
"""

['A', 'T', 'G', 'C']

def count_v2(dna,pair):
    i = 0
    for AT in dna:
        if AT == pair:
            i += 1
    return dna.count(pair)

dna = 'ACTGGCTATCCATT'
pair = "AT"
n = count_v2(dna,pair)
print '%s appears %d times in %s' % (pair,n, dna)

# dna = 'ATGCGGACCTAT'

print count_v2("ATGCGGACCTAT", "AT")
