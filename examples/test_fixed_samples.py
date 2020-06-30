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
    integral.set_values(1, 4, i, 1, sigma=2)
    res1 = integral(fcn1, eps=1e-5)
    print("Mikor: ", res1)


def main():
    prime_val(n_prime(101))
    prime_val(n_prime(523))
    prime_val(n_prime(1259))
    prime_val(n_prime(10007))


if __name__ == "__main__":
    main()
