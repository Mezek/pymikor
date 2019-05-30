#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *


def main():
    integral = Mikor()
    integral.set_values(3, 1, 5147)
    integral.show_parameters()

    z, w = integral.first_optimal_a()
    print(z, w)
    print(integral.calc_optimal_coeffs_a(z))

    print(integral.more_optimal(1.e-10))

    #print('S:', integral.h_for_coeffs([1, 30, 104]))
    #print('S:', integral.h_for_coeffs([1, 73, 155]))

    #integral.compute_coeffs(3, 1001)

    del integral


if __name__ == "__main__":
    main()