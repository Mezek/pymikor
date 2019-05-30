#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *


"""
def get_optimal_table(self, s, n):
        self.set_values(s, 1, n)
"""


def main():
    max_s = 3
    p_start = 10009
    max_n_nodes = 10100
    integral = Mikor()
    integral.show_parameters()
    print('Spawning numbers...')

    with open('coefficients.txt', 'w') as f:
        f.write('Tables of optimal coefficients\n')

    for i in range(3, max_s + 1):
        p_num = p_start
        print(str(i), sep=' ', end=' ', flush=True)
        with open('coefficients.txt', 'a') as f:
            f.write('\n  N=p' + ' ' * 4 + 'H(a) - 1' + ' ' * 5 + 's = %i\n' % i)
            f.write('  ' + '-' * 25 + '\n')
            while p_num <= max_n_nodes:
                p_num = n_prime(p_num)
                integral.set_values(i, 1, p_num)
                mo = integral.more_optimal(1.e-10)
                for j in range(len(mo)):
                    f.write('%6i   ' % p_num)
                    opt_a = integral.calc_optimal_coeffs_a(mo[j])
                    opt_val = integral.h_for_coeffs(opt_a) - 1
                    f.write(f'{opt_val:10.6}' + ' ' * 2)
                    f.write(str(mo[j]) + ' ' * 2)
                    for k in range(2, len(opt_a)):
                        f.write(str(opt_a[k]) + ' ' * 2)
                    f.write('\n')
                p_num += 1000
    print('\n')


if __name__ == "__main__":
    main()
