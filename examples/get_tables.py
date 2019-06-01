#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *


def get_table_for_p():
    max_s = 3
    p_start = 99
    max_n_nodes = 6000
    integral = Mikor()
    integral.show_parameters()
    print('Spawning numbers...')

    with open('coefficients.txt', 'w') as f:
        f.write('Tables of optimal coefficients\n')

    for i in range(3, max_s + 1):
        p_num = p_start
        print(str(i), sep=' ', end=' ', flush=True)
        with open('coefficients.txt', 'a') as f:
            f.write('\n  N=p' + ' ' * 6 + 'H(a) - 1' + ' ' * 5 + f's = {i}\n')
            f.write('  ' + '-' * 27 + '\n')
            while p_num <= max_n_nodes:
                p_num = n_prime(p_num)
                integral.set_values(i, 1, p_num)
                mo = integral.more_optimal(1.e-10)
                for j in range(len(mo)):
                    f.write(f'{p_num:6}   ')
                    opt_a = integral.calc_optimal_coefficients_a(mo[j])
                    opt_val = integral.h_for_coeffs(opt_a) - 1
                    f.write(f'{opt_val:12.6}' + ' ' * 2)
                    f.write(f'{mo[j]}' + ' ' * 2)
                    for k in range(2, len(opt_a)):
                        f.write(f'{opt_a[k]}' + ' ' * 2)
                    f.write('\n')
                p_num += 1000
    print('\n')


def get_table_for_p_q():
    max_s = 9
    p_start = 99
    max_n_nodes = 100000
    integral = Mikor()
    integral.show_parameters()
    print('Spawning numbers...')

    with open('coefficientsPQ.txt', 'w') as f:
        f.write('Tables of optimal coefficients\n')


def main():
    # get_table_for_p()
    get_table_for_p_q()


if __name__ == "__main__":
    main()
