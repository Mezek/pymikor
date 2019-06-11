#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides tables for N=p

Testing functions
https://doi.org/10.1016/0010-4655(78)90023-1
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def fcn1(x):
    df = 0
    for i in range(4):
        df *= x[i]*math.sqrt(1. - x[i]*x[i])
    return 81*df


def fcn2(x):
    df = 0
    for i in range(4):
        df *= math.exp(x[i])/(math.e - 1.)
    return df


def main():
    integral = Mikor()
    integral.set_values(3, 50000, 3)
    # integral.set_dpq(3, 907, 31)
    integral.show_parameters()

    result = integral(fcn2, name='Fcn progress')
    print(f'Result of integration   : {result}')

    del integral


if __name__ == "__main__":
    main()
