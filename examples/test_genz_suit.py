#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test integrand suit by Genz

"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

import math
from pymikor import *
from integrand_suit import *


def fcn_osc(a, u):
    fu = math.cos(2.*math.pi*u[0] + math.fsum(a))
    fd = math.cos(2.*math.pi*u[0])
    print(fu, fd)
    prod = 1.
    for e in a:
        print(e)
        prod *= e
    return (fu - fd)*prod


def main():
    with open('coefficients.txt', 'w') as f:
        f.write('\n')

    fof = Integrand('FCN', 4)
    a = fof.a
    u = fof.u
    integral = Mikor()
    integral.set_values(1, 4, 10000, 1, sigma=2)
    integral.show_parameters()
    result = integral(fof.oscillatory_fcn)
    # integral.show_parameters()
    print(f'\nResult of integration   : {result}, {fcn_osc(a, u)}')

    del integral


if __name__ == "__main__":
    main()
