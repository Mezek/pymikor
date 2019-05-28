#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *


def f(x):
    df = 0
    for d in range(len(x)):
        df += x[d]
    return df


def main():
    integral = Mikor()
    integral.set_values(3, 2, 199)
    integral.show_parameters()

    print(integral.optimal_coeffs(integral.first_optimal()[0]))

    z, w = integral.first_optimal()

    print(integral.h_poly(z))
    print(integral.h_poly_chet(z))

    print(integral.more_optimal(1.e-15))

    print('S:', integral.h_for_coeffs([1, 30, 104]))
    print('S:', integral.h_for_coeffs([1, 73, 155]))


if __name__ == "__main__":
    main()