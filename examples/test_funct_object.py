#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Integrating functions

Methods for integrating by given function objects
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from math import *
from scipy.integrate import *
import time


def fcn1(x):
    f = 1
    for i in range(4):
        dblx = x[i]*x[i]
        if dblx > 1.0:
            dblx = 1.0
        f *= x[i]*sqrt(1. - dblx)
    return 81*f


def fcn1a(x, y, z, w):
    xx = x*sqrt(1. - x*x)
    yy = y*sqrt(1. - y*y)
    zz = z*sqrt(1. - z*z)
    ww = w*sqrt(1. - w*w)
    return 81*xx*yy*zz*ww


def fcn2(x, y, z):
    return x*y*z


def fcn7(x):
    return 3.*x[0]*x[0] + 4.*x[1]*x[2] + 8.*x[3]*x[4]*x[5] + 7.*pow(x[6], 6)


def main():
    # res2, err2 = nquad(fcn2, [[0, 1], [0, 1], [0, 1]])
    # print(res2)
    # options = {'epsabs': 1.5e-2, 'epsrel': 0, 'limit': 20}
    options = {'limit': 20}
#    res1a, err1a = nquad(fcn1a, [[0, 1], [0, 1], [0, 1], [0, 1]])#,
#                         opts=[options, options, options, options])
#    print(res1a, err1a)

    integral = PyMikor()
    integral.set_values(1, 4, 1259, 1, sigma=2)
    start_time = time.time()
    res1 = integral(fcn1)
    t_time = time.time() - start_time
    print(res1)
    print(f'{t_time} seconds')


if __name__ == "__main__":
    main()
