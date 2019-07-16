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
    integral.set_values(2, 4, 10000, 1, sigma=1)
    integral.set_dpq(3, 907, 31)
    integral.show_parameters()

    result = integral(fcn, eps=1e-5)
    # integral.show_parameters()
    print(f'\nResult of integration   : {result}')

    del integral


if __name__ == "__main__":
    main()
