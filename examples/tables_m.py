#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides tables for Mikor subroutine
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

import sys
sys.path.append('../src')
from pymikor import *


def candidates(arr, eps, start, stop):
    integral = PyMikor()
    # integral.show_parameters()
    for i in range(start, stop + 1):
        print(str(i), sep=' ', end=' ', flush=True)
        with open('coefficients.txt', 'a') as f:
            f.write('\n ' + '-' * 9 + f'\n   s = {i}\n ' + '-' * 53 + '\n')
            f.write('  N=p' + ' ' * 7 + 'a' + ' ' * 7 + '  values' + ' ' * 12 + f'eps < {eps}\n')
            f.write(' ' + '-' * 53 + '\n')
            for j in range(len(arr)):
                integral.set_values(3, i, arr[j], 1, sigma=1)
                mo, mo_val, cand = integral.first_optimal_a_candidates(eps)
                f.write(f'{arr[j]:6}   ')
                f.write(f'{mo:5}' + ' ' * 2 + f' |  {mo_val:.18}\n')
                for k in range(len(cand)):
                    f.write(f' ' * 9)
                    f.write(f'{cand[k][0]:5}' + ' ' * 6 + f'{cand[k][1]:.18}')
                    f.write(f'\t  {(cand[k][1] - mo_val):.4}\n')
                f.write('\n')


def main():
    ms1 = np.array([1259])
    ms3 = np.array([23, 53, 101, 151, 307, 523])
    ms4 = np.array([101, 151, 307, 523])

    mk = np.array([23, 53, 101, 151, 307, 523, 829, 1259, 2129, 3001, 4001, 5003,
                   6007, 8191, 10007, 13001, 20011, 30011, 40009, 50021, 75011,
                   100003, 200003, 500009, 1000003, 2000003, 5000011])
    mn = np.array([5003, 6007, 8191, 10007, 13001, 20011, 30011, 40009, 50021, 75011,
                   100003, 200003, 500009, 1000003, 2000003, 5000011])

    print('Spawning numbers...')

    with open('coefficients.txt', 'w') as f:
        f.write('Table of optimal candidates\n')
    eps = 1e-12
    # candidates(ms3, eps, 3, 6)
    # candidates(ms4, eps, 5, 6)
    candidates(ms1, eps, 3, 3)


if __name__ == "__main__":
    main()
