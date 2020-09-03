#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test integrand suit by Genz

"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from integrand_suit import *


def main():
    with open('coefficients.txt', 'w') as f:
        f.write('\n')

    dmn = 7
    fof = Integrand('FCN', dmn)
    integral = Mikor()
    integral.set_values(2, dmn, 1000, 1, sigma=2)
    integral.show_parameters()
    # result = integral(fof.oscillatory_fcn)
    # print(f'\nResult of integration   : {result}, {fof.exact_oscillatory()}')

    # result = integral(fof.product_peak_fcn)
    # print(f'\nResult of integration   : {result}, {fof.exact_product_peak()}')

    fof.show_parameters()
    # result = integral(fof.gaussian_fcn)
    # ex_tr = fof.exact_gaussian()
    # print(f'\nResults: {result} {ex_tr} {result-ex_tr}')

    # result = integral(fof.c0_fcn)
    # ex_tr = fof.exact_c0()
    # print(f'\nResults: {result} {ex_tr} {result - ex_tr}')

    # result = integral(fof.corner_peak_fcn)
    # ex_tr = fof.exact_corner_peak()
    # print(f'\nResults: {result} {ex_tr} {result - ex_tr}')

    result = integral(fof.discontinuous_fcn)
    ex_tr = fof.exact_discontinuous()
    print(f'\nResults: {result} {ex_tr} {result - ex_tr}')

    del integral


if __name__ == "__main__":
    main()
