#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Integration of function

Evaluation of known integrals
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def fcn1(x):
    return np.exp(x[1] - x[0])


def main():

    ex_fcn1 = np.exp(-0.5) + np.exp(0.5) - 2.
    integral = Mikor()

    # fcn1
    x_lim = [[0., 0.5] for _ in range(2)]
    integral.set_values(3, 2, 100003, 1, sigma=2, limits=x_lim)

    # fcn2
    # x_lim = [[0.00001, 0.99999] for _ in range(10)]
    # integral.set_values(1, 10, 1000003, 1, sigma=2, limits=x_lim)

    integral.show_parameters()

    result = integral(fcn1)
    # result = integral(fcn2)
    print(f'\nResult: {result}')
    print(f'Exact:  {ex_fcn1}')
    print(f'Diff:  ', (result - ex_fcn1))

    del integral


if __name__ == "__main__":
    main()
