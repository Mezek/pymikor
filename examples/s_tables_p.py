#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides tables for N=p

Use it to check the original tables in paper of A.I.Saltykov
https://doi.org/10.1016/0041-5553(63)90134-4
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
    pa = ([23, 53])
    mn = ([23, 53, 101, 151, 307, 523, 829, 1259, 2129, 3001, 4001,5003,
           6007, 8191, 10007, 13001, 20011, 30011, 40009, 50021, 75011,
           100003, 200003, 500009, 1000003, 2000003, 5000011])

    integral = Mikor()
    # integral.show_parameters()
    print('Spawning numbers...')

    # coefficientsP.txt
    with open('coefficients.txt', 'w') as f:
        f.write('Tables of optimal coefficients\n')

    mn = np.asarray(mn)
    pa = np.asarray(pa)
    for i in range(3, 20):
        print(str(i), sep=' ', end=' ', flush=True)
        with open('coefficients.txt', 'a') as f:
            f.write(f'\n s = {i}\n')
            f.write('  N=p' + ' ' * 7 + 'H(a) - 1' + ' ' * 7 + 'a_2 -->\n')
            f.write(' ' + '-' * 34 + '\n')
            p_num = 1
            while p_num < len(pa):
                integral.set_values(i, mn[p_num], 2, 1, sigma=3)
                mo = integral.more_optimal(1.e-10)
                for j in range(len(mo)):
                    f.write(f'{mn[p_num]:6}   ')
                    opt_a = integral.calc_optimal_coefficients_a(mo[j])
                    opt_val = integral.h_for_coefficients(opt_a) - 1
                    f.write(f'{opt_val:12.6}' + ' ' * 2)
                    f.write(f'{mo[j]:5}' + ' ' * 2)
                    for k in range(2, len(opt_a)):
                        f.write(f'{opt_a[k]:5}' + ' ' * 2)
                    f.write('\n')
                p_num += 1
    print('\n')

    return

    for i in sv:
        arr = np.asarray(i)
        print(str(arr[0]), sep=' ', end=' ', flush=True)
        with open('coefficients.txt', 'a') as f:
            f.write(f'\n s = {arr[0]}\n')
            f.write('  N=p' + ' ' * 7 + 'H(a) - 1' + ' ' * 7 + 'a_2 -->\n')
            f.write(' ' + '-' * 34 + '\n')
            p_num = 1
            while p_num < len(arr):
                integral.set_values(arr[0], arr[p_num], 2, 1, sigma=3)
                mo = integral.more_optimal(1.e-10)
                for j in range(len(mo)):
                    f.write(f'{arr[p_num]:6}   ')
                    opt_a = integral.calc_optimal_coefficients_a(mo[j])
                    opt_val = integral.h_for_coefficients(opt_a) - 1
                    f.write(f'{opt_val:12.6}' + ' ' * 2)
                    f.write(f'{mo[j]:5}' + ' ' * 2)
                    for k in range(2, len(opt_a)):
                        f.write(f'{opt_a[k]:5}' + ' ' * 2)
                    f.write('\n')
                p_num += 1
    print('\n')


if __name__ == "__main__":
    main()
