#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides tables for Mikor subroutine
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def main():
    sv = ([3, 101, 199, 307, 523, 701, 1069, 1543, 2129, 3001, 4001, 5003, 6007, 8191, 10007],
          [4, 307, 523, 701, 829, 1069, 1543, 2129, 3001, 4001, 4097, 5003, 6007, 6023, 8191, 10007, 12029, 24041],
          [5, 1069, 1543, 2129, 3001, 4001, 5003, 6007, 8191, 10007],
          [6, 2129, 3001, 4001, 5003, 6007, 6023, 8191, 10007, 12029, 24041])
    mn = np.array([23, 53, 101, 151, 307, 523, 829, 1259, 2129, 3001, 4001, 5003,
                   6007, 8191, 10007, 13001, 20011, 30011, 40009, 50021, 75011,
                   100003, 200003, 500009, 1000003, 2000003, 5000011])
    mn = np.array([5003, 6007])

    integral = Mikor()
    # integral.show_parameters()
    print('Spawning numbers...')

    with open('coefficients.txt', 'w') as f:
        f.write('Tables of optimal coefficients\n')

    arr = mn
    for i in range(10, 11):
        print(str(i), sep=' ', end=' ', flush=True)
        with open('coefficients.txt', 'a') as f:
            f.write(f'\n s = {i}\n')
            f.write('  N=p' + ' ' * 7 + 'a_2 -->\n')
            f.write(' ' + '-' * 34 + '\n')
            for j in range(len(arr)):
                print(j)
                integral.set_values(i, arr[j], 2, 1, sigma=3)
                mo, mo_val = integral.first_optimal_a()
                f.write(f'{arr[j]:6}   ')
                opt_a = integral.calc_optimal_coefficients_a(mo)
                f.write(f'{mo:5}' + ' ' * 2)
                for k in range(2, len(opt_a)):
                    f.write(f'{opt_a[k]:5}' + ' ' * 2)
                f.write('\n')
    print('\n')


if __name__ == "__main__":
    main()
