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


def fy(x):
    return x*sqrt(1. - x*x)


def main():
    x = np.linspace(0, 1, 1007)
    fyv = np.vectorize(fy)
    res1a = simps(fyv(x), x)
    print(np.power(res1a, 4)*81)

    integral = Mikor()
    integral.set_values(3, 4, 1007, 1, sigma=2)
    res1 = integral(fcn1, eps=1e-4)
    print(res1)


if __name__ == "__main__":
    main()
