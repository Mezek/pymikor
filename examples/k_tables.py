#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Results of integrations

Use it to check the original tables in book of N.M.Korobov
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def fcn1(x):
    f = 1
    for i in range(4):
        f *= x[i]
    return 16*f


def fcn2(x):
    f = (x[0] + x[1] - x[2] + x[3])
    return f


def fcn3(x):
    c = 1./(math.e - 8./3.)
    f = pow(x[0], 3)*pow(x[1], 2)*x[2]*math.exp(x[0]*x[1]*x[2]*x[3])
    return c*f


def fcn4(x, n=10):
    f = 1. + math.sin(math.pi*n*(x[0] + x[1] - x[2] + 2.*x[3]))
    return f


def fcn5(x, m=30):
    f = 1.
    for i in range(4):
        denom = (1. - x[i])*(1. - x[i])
        f *= math.exp(-m*x[i]*x[i]/denom) / denom
    return 16.*m*m/pow(math.pi, 2)*f


def integrator(f, t):
    res = list(map(lambda x: x(t), f))
    return res


def main():
    integral = Mikor()
    integral.set_values(4, 4, 40000, 1, sigma=3)
    integral.show_parameters()

    k_fcn = [fcn1, fcn2, fcn3, fcn4, fcn5]

    print('Results of integration:')
    for i, item in enumerate(k_fcn):
        result = integral(item)
        print(f'{i+1}. = {result}')


if __name__ == "__main__":
    main()
