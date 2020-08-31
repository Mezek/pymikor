#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test integrand suit by Genz

"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from integrand_suit import *


def fcn_osc(a, u):
    b = 2.*math.pi*u[0]
    s = math.fsum(a)
    prod = 1.
    for ael in a:
        prod = 2.*math.sin(ael/2.)/ael
    return math.cos((2.*b + s)/2.)*prod


def main():
    with open('coefficients.txt', 'w') as f:
        f.write('\n')

    fof = Integrand('FCN', 5)
    a = fof.a
    u = fof.u
    integral = Mikor()
    integral.set_values(2, 5, 1000, 1, sigma=2)
    integral.show_parameters()
    result = integral(fof.oscillatory_fcn)
    # integral.show_parameters()
    print(a, u)
    print(f'\nResult of integration   : {result}, {fcn_osc(a, u)}')

    del integral


if __name__ == "__main__":
    main()
