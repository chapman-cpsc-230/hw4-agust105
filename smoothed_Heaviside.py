"""
File: smoothed_Heaviside.py

Copyright (c) 2016 Francis Agustin

License: MIT

Implemented a smoother Heaviside function by extending domain of the function
and tested its implementation.
"""

from math import sin, pi


def test_H_eps(x, eps = 0.01):
    xoe = x/eps
    if x < -eps:
        result = 0
    elif x <= eps:
        result = 0.5 * (1 + (xoe) + (sin(pi*xoe)))/pi
    else:
        result = 1
    return result

eps = 0.01

print test_H_eps(-eps - 1)
print test_H_eps(-eps)
print test_H_eps(0)
print test_H_eps(eps)
print test_H_eps(eps + 1)
