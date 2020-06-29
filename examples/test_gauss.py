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
    for i in range(1):
        dblx = x[i]*x[i]
        if dblx > 1.0:
            dblx = 1.0
        f *= x[i]*sqrt(1. - dblx)
    return 81*f


def fcn_a(x):
    f = 1
    for i in range(3):
        f *= x[i]
    return f


def main():
    #I = quad(fcn_a, 0, 1)
    #print("Integral = ", I)

    fcn_t = lambda z, y, x: x*y*z
    J = tplquad(fcn_t, 0, 1, lambda x: 0, lambda x: 1, lambda x, y: 0, lambda x, y: 1)
    print(J)

#    integral = Mikor()
#    integral.set_values(3, 2, 1000, 1, sigma=2)
#    result = integral(fcn1, eps=1e-4)
#    print(result)


if __name__ == "__main__":
    main()
