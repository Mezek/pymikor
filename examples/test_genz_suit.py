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
        f.write('Genz suit')

    nd = (3, 5, 8, 10, 13, 15)
    for i in nd:
        with open('coefficients.txt', 'a') as f:
            f.write('\nDimension: ' + str(i))

    dmn = 15
    integral = Mikor()
    integral.set_values(1, dmn, 1000, 1, sigma=2)
    integral.show_parameters()

    fof = Integrand('FCN', dmn)
    fof.normalize_a(2, 600)
    fof.show_parameters()

    result = integral(fof.oscillatory_fcn)
    exact_res = fof.exact_oscillatory()
    print(f'\nResults oscillatory:')
    print(f'{result:.10e}')
    print(f'{exact_res:.10e}')
    print(f'{(result - exact_res):.3e}')

    # result = integral(fof.product_peak_fcn)
    # exact_res = fof.exact_product_peak()
    # print(f'\nResults: {result} {exact_res} {result - exact_res}')

    # result = integral(fof.gaussian_fcn)
    # exact_res = fof.exact_gaussian()
    # print(f'\nResults: {result} {exact_res} {result - exact_res}')

    # result = integral(fof.c0_fcn)
    # exact_res = fof.exact_c0()
    # print(f'\nResults: {result} {exact_res} {result - exact_res}')

    # result = integral(fof.corner_peak_fcn)
    # exact_res = fof.exact_corner_peak()
    # print(f'\nResults: {result} {exact_res} {result - exact_res}')

    # result = integral(fof.discontinuous_fcn)
    # exact_res = fof.exact_discontinuous()
    # print(f'\nResults: {result} {exact_res} {result - exact_res}')

    del integral


if __name__ == "__main__":
    main()
