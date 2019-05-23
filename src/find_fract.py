from math import *
import numpy as np


def fraction(num):
    f, i = modf(num)
    return f


def lfraction(num):
    return str(num-int(num)).split('.')[1]


num = 12316767678678.6
lnum = 1231676767867812316767678678.6

#a = [15, 16, 17]
#a = [503, 504, 505]
a = np.arange(1, 15)

d = 503
m = 1
n = 1.
for i in range(len(a)):
    m = (m*a[i]) % d
    n = n*a[i]
    print(m, n)

m = m / d
n = n / d
print(fraction(m))
print(fraction(n))
print(217/d, 720/d)