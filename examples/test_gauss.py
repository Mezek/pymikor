#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""General integration using Gaussian quadrature

Methods for integrating functions objects
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from math import *
from scipy.integrate import *


def fcn7(x):
    return 3.*x[0]*x[0] + 4.*x[1]*x[2] + 8.*x[3]*x[4]*x[5] + 7.*pow(x[6], 6)


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


def fcn_test(x, y, z):
    return x*y*z


def main():
    # result, error = nquad(fcn_test, [[0, 1], [0, 1], [0, 1]])
    options = {'epsabs': 1.5e-03, 'epsrel': 1.5e-03, 'limit': 10}
    result, error = nquad(fcn1a, [[0, 1], [0, 1], [0, 1], [0, 1]], opts=[options,options,options,options])

    print("Result = ", result, error)

#    integral = Mikor()
#    integral.set_values(3, 2, 1000, 1, sigma=2)
#    result = integral(fcn1, eps=1e-4)
#    print(result)


if __name__ == "__main__":
    main()
