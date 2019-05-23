# program to compute fraction of a big number

from math import *
from decimal import *



def fraction(num):
    f, i = modf(num)
    return f


def lfraction(num):
    return str(num-int(num)).split('.')[1]


# Driver program
num = 12316767678678.6
lnum = 1231676767867812316767678678.6


print(fraction(num))
print(fraction(lnum))

print(lfraction(num))
print(lfraction(lnum))

print(floor(0), floor(1), floor(1.2), floor(Decimal(503)**Decimal(13)/Decimal(1013)))