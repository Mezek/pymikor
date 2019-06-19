#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find first optimal coefficient a

Modify to change sigma and dimension.
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def main():
    integral = Mikor()
    integral.set_values(1, 1, 1, 1, sigma=2)

    c = 'y'
    while c == 'y':
        p = input('\n Set p number: ')
        p = int(p)
        if not is_prime(p):
            print(f'{p} in NOT prime number')
            continue
        integral.set_dpq(4, p, 1)
        integral.show_parameters()
        opt_a, opt_val = integral.first_optimal_a()
        print(f'First optimal = {opt_a}')

        c = input('\n Continue? [y/n]')


if __name__ == "__main__":
    main()
