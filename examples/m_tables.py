#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides tables for Mikor subroutine
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def main():
    ms = np.array([53])
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
    for i in range(3, 4):
        print(str(i), sep=' ', end=' ', flush=True)
        with open('coefficients.txt', 'a') as f:
            f.write(f'\n s = {i}\n')
            f.write('  N=p' + ' ' * 7 + 'a' + ' ' * 7 + '  other candidates\n')
            f.write(' ' + '-' * 47 + '\n')
            for j in range(len(arr)):
                print(j)
                integral.set_values(i, arr[j], 2, 1, sigma=1)
                mo, mo_val, cand = integral.first_optimal_a_candidates(1e-12)
                f.write(f'{arr[j]:6}   ')
                f.write(f'{mo:5}' + ' ' * 2 + ' | ')
                for k in range(len(cand)):
                    f.write(f'{cand[k]:5}' + ' ' * 2)
                f.write('\n')
    print('\n')


if __name__ == "__main__":
    main()
