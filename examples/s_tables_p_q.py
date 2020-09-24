#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides tables for N=p.q

Use it to check the original tables in paper of A.I.Saltykov
https://doi.org/10.1016/0041-5553(63)90134-4
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"


from pymikor import *


def main():
    sv = ([[3, 691, 29], [3, 907, 31], [3, 1259, 31], [3, 1543, 37], [3, 1907, 43], [3, 2129, 47]],
          [[4, 691, 29], [4, 907, 31], [4, 1259, 31], [4, 1543, 37], [4, 1907, 43], [4, 2129, 47]],
          [[5, 653, 23], [5, 691, 29], [5, 1069, 31], [5, 1381, 37], [5, 1733, 41], [5, 2129, 47]],
          [[6, 653, 23], [6, 691, 29], [6, 1069, 31], [6, 1381, 37], [6, 1733, 41], [6, 2129, 47]],
          [[7, 653, 23], [7, 787, 23], [7, 829, 29], [7, 1069, 31], [7, 1249, 37], [7, 1543, 37],
           [7, 1733, 41], [7, 2129, 47]],
          [[8, 829, 29], [8, 1069, 31], [8, 1249, 37], [8, 1543, 37], [8, 1733, 41], [8, 2129, 47]],
          [[9, 1069, 31], [9, 1249, 37], [9, 1543, 37], [9, 1733, 41], [9, 2129, 47], [9, 3001, 53]],
          [[10, 4507, 19], [10, 4507, 23], [10, 5003, 23], [10, 4507, 29], [10, 5003, 29], [10, 5003, 31]])

    integral = PyMikor()
    # integral.show_parameters()
    print('Spawning numbers...')

    # coefficientsPQ.txt
    with open('coefficients.txt', 'w') as f:
        f.write('Tables of optimal coefficients\n')

    for i in sv:
        with open('coefficients.txt', 'a') as f:
            arr = np.asarray(i)
            print(str(arr[0][0]), sep=' ', end=' ', flush=True)
            f.write(f'\n s = {arr[0][0]}\n')
            f.write('  N=pq' + ' ' * 7 + 'p' + ' ' * 5 + 'q' + ' ' * 5 +
                    'a' + ' ' * 5 + 'b' + ' ' * 5 + 'H(b) - 1' + ' ' * 7 + 'a_2 -->\n')
            f.write(' ' + '-' * 60 + '\n')
            for j in range(len(arr)):
                integral.set_dpq(arr[j][0], arr[j][1], arr[j][2])
                c = integral.optimal_coefficients()

                f.write(f'{arr[j][1]*arr[j][2]:6} ' + f'{arr[j][1]:6} ' + f'{arr[j][2]:6} ')
                f.write(f'{integral.a_opt:5}' + ' ' * 2)
                f.write(f'{integral.b_opt:5}' + ' ' * 2)
                f.write(f'{integral.b_opt_value - 1:12.6}' + ' ' * 2)
                for k in range(1, len(c)):
                    f.write(f'{c[k]:6.0f}' + ' ' * 2)
                f.write('\n')


if __name__ == "__main__":
    main()
