#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compare integration result

Fortran and Python comparison of 8-dim integral
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def fcn(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    t = x[3]
    y1 = x[4]
    y2 = x[5]
    z = x[6]
    xi = x[7]

    x1m1 = 1. - x1
    x2m1 = 1. - x2
    x3m1 = 1. - x3
    tm1 = 1. - t
    y1m1 = 1. - y1
    y2m1 = 1. - y2
    zm1 = 1. - z
    xim1 = 1. - xi

    eps1 = 52.768
    # eta = 1.622
    eta = 26.6597

    smu2 = x1*t*eps1 + tm1*eta
    alpha2 = y1*y2*(1. - y1*y2)
    al2 = y2*y1m1/(1. - y1*y2)

    delta2 = ((y2*y1m1)*(y2*y1m1) + eps1*(y1*y2*x3 + x2*y2m1))/alpha2
    d2 = pow((xi*(zm1 + z*al2)), 2) + xi*z*delta2 + smu2*xim1

    a = y2*y1m1
    b = y1*y2
    rho = xi*(zm1 + al2*z)

    a1 = (-3. - 9.*rho)/8.
    a2 = -3./4.*pow(rho, 3)
    b1 = a*b*.25
    b2 = a*a*.5*(-1 - rho) + a*b*rho*(-.5 + .25*rho)
    b3 = 0.

    dcom = -2.*a1/pow(d2, 3) + 3.*a2/pow(d2, 4) + 3*z*xi/alpha2*(-b1/pow(d2, 3) + b2/pow(d2, 4) - 2.*b3/pow(d2, 5))
    dgam = t*y1*y2m1*z*pow(y2*xi*xim1/alpha2, 2)

    return dgam*dcom


def main():
    integral = Mikor()
    integral.set_values(1, 8, 1000, 1, sigma=2)
    # integral.set_dpq(7, 907, 31)
    integral.show_parameters()

    result = integral(fcn, eps=1e-4)
    rz = result*4*52.768*3
    print(f'\nResult: {rz}')

    del integral


if __name__ == "__main__":
    main()
