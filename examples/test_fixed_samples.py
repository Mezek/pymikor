#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Integrating functions

Methods for integrating by given fixed samples
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from math import *
from scipy.integrate import *


def fcn1(x):
    f = 1
    for i in range(4):
        dblx = x[i]*x[i]
        if dblx > 1.0:
            dblx = 1.0
        f *= x[i]*sqrt(1. - dblx)
    return 81*f


def fcn7(x):
    return 3.*x[0]*x[0] + 4.*x[1]*x[2] + 8.*x[3]*x[4]*x[5] + 7.*pow(x[6], 6)


def fcn1s(x):
    return x*sqrt(1. - x*x)


def prime_val(i):
    x = np.linspace(0, 1, i)
    fcn1sv = np.vectorize(fcn1s)
    res1a = simps(fcn1sv(x), x)
    res1b = trapz(fcn1sv(x), x)

    print("Number: ", i)
    print("Simps: ", np.power(res1a, 4)*81)
    print("Trapz: ", np.power(res1b, 4)*81)

    integral = Mikor()
    integral.set_values(1, 4, i, 1, sigma=3)
    res1 = integral(fcn1)
    print("Mikor: ", res1)


def main():
    fs = np.array([# 53, 101, 151, 307, 523, 829,
                    1259, 2129, 3001, 4001, 5003,
                   6007, 8191, 10007, 13001, 20011, 30011, 40009, 50021])
    for i in fs:
        prime_val(n_prime(i))


if __name__ == "__main__":
    main()
