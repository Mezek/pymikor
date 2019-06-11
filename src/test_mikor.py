#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *


def fcn(x):
    return 3.*x[0]*x[0] + 4.*x[1]*x[2]


def fcn1(x):
    df = 0
    for d in range(len(x)):
        df += x[d]
    return df


def fcn2(x):
    df = 1
    for d in range(len(x)):
        df *= x[d]
    return df


def fcn3(x):
    fc = 0
    for i in range(4):
        fc += 0.5*math.pi*math.sin(math.pi*x[i])
    return fc


def main():
    integral = Mikor()
    integral.set_values(2, 50000, 2)
    # integral.set_dpq(3, 907, 31)
    integral.show_parameters()

    result = integral(fcn1, name='Fcn progress')
    print(f'Result of integration   : {result}')

    # x = np.array([0.1, 0.2, 0.3, 0.4])
    # print(fcn3(x))

    """
    result1 = integral(fcn1, name='F1')
    result2 = integral(fcn2, name='F2')

    print(f'Result of integration   : {result1}')
    print(f'Result of integration   : {result2}')
    """

    del integral


if __name__ == "__main__":
    main()
