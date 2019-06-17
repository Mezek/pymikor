#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides tables for N=p

Testing functions of K. Zakrzewska, J. Dudek, N. Nazarewicz
https://doi.org/10.1016/0010-4655(78)90023-1
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from math import *


def fcn1(x):
    f = 1
    for i in range(4):
        f *= x[i]*sqrt(1. - x[i]*x[i])
    return 81*f


def fcn2(x):
    f = 1
    for i in range(4):
        f *= exp(x[i])/(math.e - 1.)
    return f


def fcn3(x):
    f = 1
    for i in range(4):
        f *= math.pi/2.*sin(math.pi*x[i])
    return f


def fcn4(x):
    f = 1
    for i in range(4):
        f *= 2*(1./pow(math.e, 2) - 1)*exp(-2*x[i])
    return f


def fcn5(x):
    f = 1
    for i in range(4):
        f *= 15*(1./pow(math.e, 15) - 1)*exp(-15*x[i])
    return f


def fcn6(x):
    f = 1
    for i in range(4):
        f *= math.pi/4./(1 + x[i]*x[i])
    return f


def main():
    integral = Mikor()
    integral.set_values(4, 50000, 3, 1, sigma=3)
    # integral.set_dpq(3, 907, 31)
    integral.show_parameters()

    k_fcn = [fcn1, fcn2, fcn3, fcn4, fcn5, fcn6]
    # k_fcn = [fcn4]

    print('Results of integration:')
    for i, item in enumerate(k_fcn):
        result = integral(item)
        print(f'{i+1}. = {result}')

    del integral


if __name__ == "__main__":
    main()
