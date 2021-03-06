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
    return 3.*x[0]*x[0] + 4.*x[1]*x[2] + 2.*x[1]


def fcn2(x):
    return 3.*x[0]*x[0] + 4.*x[1]*x[0] + 2.*x[1]


def main():
    integral = PyMikor()

    """ strategy 1 """

    integral.set_values(1, 3, 99, 1, sigma=1)
    integral.show_parameters()
    result = integral(fcn, eps=1e-5)
    print(f'\nIntegration result: {result}')

    integral.set_values(1, 3, 259, 1, sigma=2)
    integral.show_parameters()
    result = integral(fcn)
    print(f'\nIntegration result: {result}')

    integral.set_values(1, 3, 10000, 1, sigma=2, eps=0.)
    integral.show_parameters()
    result = integral(fcn, eps=7e-5)
    print(f'\nIntegration result: {result}')

    """ strategy 2 """

    integral.set_values(2, 3, 11, 1, sigma=2, eps=1e-6)
    integral.show_parameters()
    result = integral(fcn)
    print(f'\nIntegration result: {result}')

    integral.set_values(2, 3, 1540, 1, sigma=2)
    integral.show_parameters()
    result = integral(fcn)
    print(f'\nIntegration result: {result}')
    """
    integral.set_values(3, 4, 10000, 1, sigma=2)
    integral.show_parameters()
    result = integral(fcn, eps=1e-5)
    print(f'\nIntegration result: {result}')
    
    integral.set_values(4, 4, 10000, 1, sigma=2)
    integral.show_parameters()
    result = integral(fcn, eps=1e-5)
    print(f'\nIntegration result: {result}')
 
    integral.set_values(3, 2, 1000, 1, sigma=2)
    integral.show_parameters()
    result = integral(fcn2, eps=1e-5)
    print(f'\nIntegration result: {result}')
    """

    del integral


if __name__ == "__main__":
    main()
