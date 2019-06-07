#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *


def fcn1(x):
    df = 0
    for d in range(len(x)):
        df += x[d]
    return df


def fcn2(x):
    df = 1
    for d in range(len(x)):
        df *= x[d]
    return df


def main():
    integral = Mikor()
    integral.set_values(3, 1000, 2, 10)
    # integral.set_dpq(3, 1907, 1)
    integral.show_parameters()

    result1 = integral(fcn1, name='F1')
    result2 = integral(fcn2, name='F2')

    print(f'Result of integration is: {result1}')
    print(f'Result of integration is: {result2}')

    """
    fa, wa = integral.first_optimal_a()
    print('a =', integral.calc_optimal_coefficients_a(fa))
    # print(integral.more_optimal(1.e-10))

    fb, wb = integral.first_optimal_b()
    print(f'b = {fb}', f'wb = {wb}')
    print('b =', integral.calc_optimal_coefficients_b(fb))

    integral.calc_optimal_coefficients_c()
    print('c =', integral.get_opt_coefficients_c())
    """
    # print('S:', integral.h_for_coeffs([1, 30, 104]))
    # print('S:', integral.h_for_coeffs([1, 73, 155]))

    del integral


if __name__ == "__main__":
    main()