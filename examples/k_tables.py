#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides results of Korobov

Use it to check the original tables in book of N.M.Korobov
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def fcn1(x):
    f = 1
    for i in range(4):
        f *= x[i]
    return 16*f


def main():
    integral = Mikor()
    integral.set_values(4, 40000, 3, 1, sigma=3)
    integral.show_parameters()

    result = integral(fcn1, name='Fcn progress')
    print(f'Result of integration   : {result}')


if __name__ == "__main__":
    main()
