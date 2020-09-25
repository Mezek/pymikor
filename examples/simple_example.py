#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple integration example

Very simple function for the integration with PyMikor
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def fcn(x):
    return 3.*x[0]*x[0] + 4.*x[1]*x[2] + 8.*x[3]*x[4]*x[5] + 7.*pow(x[6], 6)


def main():
    integral = PyMikor()
    integral.set_values(1, 7, 10000, 1, sigma=2, limits=[[0, 10], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]])
    # integral.set_values(1, 7, 1000, 1, sigma=2)
    # integral.set_dpq(7, 907, 31)
    integral.show_parameters()

    # result = integral(fcn, eps=1e-4)
    result = integral(fcn)
    print(f'\nResult of integration   : {result}')

    del integral


if __name__ == "__main__":
    main()
