#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides tables for Mikor subroutine
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def main():
    ms = np.array([23, 53, 101, 151])
    mk = np.array([23, 53, 101, 151, 307, 523, 829, 1259, 2129, 3001, 4001, 5003,
                   6007, 8191, 10007, 13001, 20011, 30011, 40009, 50021, 75011,
                   100003, 200003, 500009, 1000003, 2000003, 5000011])
    mn = np.array([5003, 6007, 8191, 10007, 13001, 20011, 30011, 40009, 50021, 75011,
                   100003, 200003, 500009, 1000003, 2000003, 5000011])

    integral = Mikor()
    # integral.show_parameters()
    print('Spawning numbers...')

    with open('coefficients.txt', 'w') as f:
        f.write('Table of optimal coefficients\n')

    arr = ms
    eps = 1e-12
    for i in range(3, 7):
        print(str(i), sep=' ', end=' ', flush=True)
        with open('coefficients.txt', 'a') as f:
            f.write(f'\n s = {i},        eps < {eps}\n')
            f.write('  N=p' + ' ' * 7 + 'a' + ' ' * 7 + f'  values\n')
            f.write(' ' + '-' * 47 + '\n')
            for j in range(len(arr)):
                integral.set_values(3, i, arr[j], 1, sigma=1)
                mo, mo_val, cand = integral.first_optimal_a_candidates(eps)
                f.write(f'{arr[j]:6}   ')
                f.write(f'{mo:5}' + ' ' * 2 + f' |  {mo_val}\n')
                for k in range(len(cand)):
                    f.write(f' ' * 9)
                    f.write(f'{cand[k][0]:5}' + ' ' * 6 + f'{cand[k][1]}\n')
                f.write('\n')
    print('\n')


if __name__ == "__main__":
    main()
