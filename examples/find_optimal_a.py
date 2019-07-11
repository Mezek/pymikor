#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find first optimal coefficient a

Modify to change sigma and dimension.
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

import sys
sys.path.append('../src')
from pymikor import *


def main():
    integral = Mikor()
    integral.set_values(1, 1, 1, 1, sigma=2)

    c = 'y'
    while c == 'y':
        # p = int(input('\n Set p number: '))
        p = int(30011)
        if not is_prime(p):
            print(f'{p} in NOT prime number')
            continue
        integral.set_dpq(5, p, 1)
        integral.show_parameters()
        opt_a, opt_val = integral.first_optimal_a(1)
        print(f'First optimal = {opt_a}')

        aoc = ([opt_a, 2311])
        for i in range(len(aoc)):
            h_valueA = integral.h_poly(aoc[i])
            h_valueB = integral.h_poly_chet(aoc[i])
            print(f'      {aoc[i]}')
            print(f'H   = {h_valueA}')
            print(f'H_c = {h_valueB}')

        # c = input('\n Continue? [y/n]')
        c = 'n'


if __name__ == "__main__":
    main()
