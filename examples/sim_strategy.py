#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple integration examples

Very simple function for the integration with PyMikor
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def fcn(x):
    return 3.*x[0]*x[0] + 4.*x[1]*x[2] + 2.*x[3]


def main():
    integral = Mikor()
    integral.set_values(2, 4, 10000, 1, sigma=2)
    integral.show_parameters()

    result = integral(fcn, eps=1e-5)
    print(f'\nResult of integration   : {result}')

    integral.set_values(1, 4, 10000, 1, sigma=2)
    print(f'\nResult of integration   : {result}')

    integral.set_values(3, 4, 10000, 1, sigma=2)
    print(f'\nResult of integration   : {result}')

    integral.set_values(4, 4, 10000, 1, sigma=2)
    print(f'\nResult of integration   : {result}')

    del integral


if __name__ == "__main__":
    main()
