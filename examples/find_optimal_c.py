#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find optimal coefficient

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
        qq = np.array([13001, 113, 6426])
        p = qq[0]
        q = qq[1]
        opt_a = qq[2]
        if not is_prime(p):
            print(f'p={p} in NOT prime number')
            break
        if not is_prime(q):
            print(f'q={q} in NOT prime number')
            break
        integral.set_dpq(12, p, q)
        integral.show_parameters()
        opt_b, opt_b_val = integral.first_optimal_b(opt_a)
        print(f'Optimals = {p}, {q}, {integral.a_opt}, {opt_b}')

        # c = input('\n Continue? [y/n]')
        c = 'n'


if __name__ == "__main__":
    main()
