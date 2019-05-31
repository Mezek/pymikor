#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *


def main():
    integral = Mikor()
    integral.set_values(3, 1, 20039)
    integral.set_p_q(691, 29)

    #integral.set_values(5, 1, 15019)
    #integral.set_p_q(653, 23)

    integral.show_parameters()

    fa, wa = integral.first_optimal_a()
    print('a =', integral.calc_optimal_coeffs_a(fa))
    # print(integral.more_optimal(1.e-10))

    fb, wb = integral.first_optimal_b()
    print(f'b = {fb}', f'wb = {wb}')
    print('b =', integral.calc_optimal_coeffs_b(fb))

    integral.calc_optimal_coeffs_c()
    print('c =', integral.get_opt_coeffs_c())

    # print('S:', integral.h_for_coeffs([1, 30, 104]))
    # print('S:', integral.h_for_coeffs([1, 73, 155]))

    del integral


if __name__ == "__main__":
    main()