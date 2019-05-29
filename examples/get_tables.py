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
    p_start = 99
    max_n_nodes = 1000
    integral = Mikor()
    integral.show_parameters()
    print('Spawning numbers...')

    with open('coefficients.txt', 'w') as f:
        f.write('Tables of optimal coefficients\n\n')

    for i in range(3, max_s + 1):
        p_num = p_start
        with open('coefficients.txt', 'a') as f:
            f.write(' N=p' + ' '*14 + 's = %i\n' % i)
            while p_num <= max_n_nodes:
                integral.set_values(i, 1, p_num)
                # f.write('%6i%12i%12i\n' % (p_num, 10 ** i, 30 ** i))
                # mo = integral.more_optimal(1.e-15)
                mo = np.ones(4)
                for j in range(len(mo)):
                    f.write(str(j) + ' ')
                f.write('\n')
                p_num += 1


if __name__ == "__main__":
    main()
