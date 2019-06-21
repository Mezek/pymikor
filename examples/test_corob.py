#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides tables for N=p

Testing functions of K. Zakrzewska, J. Dudek, N. Nazarewicz
https://doi.org/10.1016/0010-4655(78)90023-1
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

import sys
sys.path.append('../src')
from pymikor import *
from math import *


def fcn1(x):
    f = 1
    for i in range(4):
        dblx = x[i]*x[i]
        if dblx > 1.0:
            dblx = 1.0
        f *= x[i]*sqrt(1. - dblx)
    return 81*f


def fcn2(x):
    f = 1
    for i in range(4):
        f *= exp(x[i])/(math.e - 1.)
    return f


def fcn3(x):
    f = 1
    for i in range(4):
        f *= math.pi/2.*sin(math.pi*x[i])
    return f


def fcn4(x):
    f = 1
    for i in range(4):
        f *= 2/(1/pow(math.e, 2) - 1)*exp(-2*x[i])
    return f


def fcn5(x):
    f = 1
    for i in range(4):
        f *= 15./(1./pow(math.e, 15) - 1)*exp(-15*x[i])
    return f


def fcn6(x):
    f = 1
    for i in range(4):
        f *= 4/math.pi/(1 + x[i]*x[i])
    return f


def fcn7(x):
    f = 1/pow(0.34*0.26, 2)*abs((x[0] - 0.2)*(x[1] - 0.4)*(x[2] - 0.6)*(x[3] - 0.8))
    return f


def fcn8(x):
    n8 = 1.266065877752
    f = 1
    for i in range(4):
        f *= exp(sin(2*math.pi*x[i]))/n8
    return f


def fcn9(x):
    c = log(101)
    f = 1
    for i in range(4):
        f *= 1/(1.01 - x[i])/c
    return f


def fcn10(x):
    c = 6/pow(math.pi, 2)
    f = 1
    for i in range(4):
        if x[i] == 0.:
            continue
        f *= log(x[i])/(x[i] - 1)*c
    return f


def main():
    nodes_4_1 = np.array([[1069, 271], [2129, 766], [3001, 1466], [5003, 2053],
                          [6007, 1351], [8191, 3842], [10007, 1206], [28111, 3570]])

    nodes_4_3 = np.array([[251, 44], [631, 290], [1259, 483], [2503, 792],
                          [4001, 956], [6521, 3138], [10007, 1206]])

    integral = Mikor()
    # integral.set_values(3, 4, 10007, 1, sigma=2)
    # integral.set_dpq(3, 907, 31)
    integral.show_parameters()
    print('Spawning numbers...')

    t_fcn = {
        'fcn1': fcn1,
        'fcn2': fcn2,
        'fcn3': fcn3
    }
    u_fcn = {
        'fcn4': fcn4,
        'fcn5': fcn5,
        'fcn6': fcn6,
        'fcn7': fcn7,
        'fcn8': fcn8
    }
    w_fcn = {
        'fcn9': fcn9,
        'fcn10': fcn10
    }

    with open('coefficients.txt', 'w') as f:
        f.write('s = 4\n')

    for i in t_fcn:
        # coefficientsZ.txt
        with open('coefficients.txt', 'a') as f:
            f.write('\n' + '-' * 93 + '\n')
            f.write(f'Function {i}\n')
            f.write('-' * 93 + '\n')
            f.write(f'  N' + ' ' * 7 +
                    'sigma=1' + ' ' * 7 + 'sigma=2' + ' ' * 7 + 'sigma=3' + ' ' * 7 +
                    'sigma=4' + ' ' * 7 + 'sigma=5' + ' ' * 7 + 'sigma=6\n')
            f.write('-' * 93 + '\n')

        for j, item in enumerate(nodes_4_1):
            with open('coefficients.txt', 'a') as f:
                f.write(f' {item[0]:6}' + ' ' * 3)
                for s in range(1, 7):
                    integral.set_values(1, 4, 5050, 1, sigma=s)
                    integral.set_pa(item)
                    fcn_name = t_fcn[i]
                    result = integral(fcn_name)
                    f.write(f'{result:.9f}' + ' '*3)
                f.write('\n')

    for i in u_fcn:
        # coefficientsZ.txt
        with open('coefficients.txt', 'a') as f:
            f.write('\n' + '-' * 21 + '\n')
            f.write(f'Function {i}\n')
            f.write('-' * 21 + '\n')
            f.write(f'  N' + ' ' * 7 +
                    'sigma=3' + '\n')
            f.write('-' * 21 + '\n')

        for j, item in enumerate(nodes_4_3):
            with open('coefficients.txt', 'a') as f:
                f.write(f' {item[0]:6}' + ' ' * 3)
                for s in range(3, 4):
                    integral.set_values(1, 4, 5050, 1, sigma=s)
                    integral.set_pa(item)
                    fcn_name = u_fcn[i]
                    result = integral(fcn_name)
                    f.write(f'{result:.6f}' + ' '*3)
                f.write('\n')

    for i in w_fcn:
        # coefficientsZ.txt
        with open('coefficients.txt', 'a') as f:
            f.write('\n' + '-' * 53 + '\n')
            f.write(f'Function {i}\n')
            f.write('-' * 53 + '\n')
            f.write(f'  N' + ' ' * 7 +
                    'sigma=2' + ' ' * 4 + 'sigma=3' + ' ' * 4 + 'sigma=4' + ' ' * 4 + 'sigma=5\n')
            f.write('-' * 53 + '\n')

        for j, item in enumerate(nodes_4_3):
            with open('coefficients.txt', 'a') as f:
                f.write(f' {item[0]:6}' + ' ' * 3)
                for s in range(2, 6):
                    integral.set_values(1, 4, 5050, 1, sigma=s)
                    integral.set_pa(item)
                    fcn_name = w_fcn[i]
                    result = integral(fcn_name)
                    f.write(f'{result:.6f}' + ' '*3)
                f.write('\n')

    del integral


if __name__ == "__main__":
    main()
