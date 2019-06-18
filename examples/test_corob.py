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
        f *= 2/(1/pow(math.e, 2) - 1)*exp(-2*x[i])
    return f


def fcn5(x):
    f = 1
    for i in range(4):
        f *= 15./(1./pow(math.e, 15) - 1)*exp(-15*x[i])
    return f


def fcn6(x):
    f = 1
    for i in range(4):
        f *= 4/math.pi/(1 + x[i]*x[i])
    return f


def fcn7(x):
    f = 1/pow(0.34*0.26, 2)*abs((x[0] - 0.2)*(x[1] - 0.4)*(x[2] - 0.6)*(x[3] - 0.8))
    return f


def fcn8(x):
    n8 = 1.266065877752
    f = 1
    for i in range(4):
        f *= exp(sin(2*math.pi*x[i]))/n8
    return f


def fcn9(x):
    c = log(101)
    f = 1
    for i in range(4):
        f *= 1/(1.01 - x[i])/c
    return f


def fcn10(x):
    c = 6/pow(math.pi, 2)
    f = 1
    for i in range(4):
        if x[i] == 0.:
            continue
        f *= log(x[i])/(x[i] - 1)*c
    return f


def main():
    node = np.array([251, 631, 1259, 2503, 4001, 6521, 10007])

    integral = Mikor()
    integral.set_values(4, 10007, 2, 1, sigma=2)
    # integral.set_dpq(3, 907, 31)
    integral.show_parameters()

    # k_fcn = [fcn1, fcn2, fcn3, fcn4, fcn5, fcn6]
    k_fcn = [fcn9]

    print('Results of integration:')
    for i, item in enumerate(k_fcn):
        result = integral(item)
        print(f'{i+1}. = {result}')

    del integral


if __name__ == "__main__":
    main()
