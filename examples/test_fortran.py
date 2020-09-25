#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Compare integration result

Fortran and Python comparison of 8-dim integral
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def fcn1(x):
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


def fcn2(x):
    qm = 280. / 105.
    xx = x[0]
    t = x[1]
    x3 = x[2]
    z1 = x[3]
    z2 = x[4]
    rho = x[5]
    y = x[6]
    aph1 = x[7]
    aph2 = x[8]
    aph3 = x[9]

    xm1 = 1. - xx
    x3m1 = 1. - x3
    x1 = 1. - x3 - x3m1 * t
    x2 = x3m1 * t
    x2m1 = 1. - x2
    ym1 = 1. - y
    rhom1 = 1. - rho
    z1m1 = 1. - z1
    aph1m1 = 1. - aph1
    aph2m1 = 1. - aph2

    dgam = z2 * aph2 / xx / xm1 * aph3*aph3 / x3

    gam1 = aph1m1 + aph1 * x2 / x3m1
    z = pow(aph2*aph3*gam1, 2) - aph2*aph3*(aph1m1 + aph1 * x2 * x2m1 / x3 / x3m1)
    c1 = aph2 * aph2m1 * pow(aph3, 2) * gam1 / z
    del1 = (pow(aph3, 2) * pow(aph2m1, 2) + aph1 * aph2 * aph3 * pow(qm, 2) / x3 / x3m1) / z

    sqm1 = qm*qm / xx / xm1
    eta = 82.176

    d1 = rho*rho * pow(ym1 - y * c1, 2) + rhom1 * z2 * (z1 * eta + z1m1 * sqm1) - rho * y * del1

    a = aph2m1 * aph3
    b = aph2 * aph3 * gam1
    rc = rho * (ym1 - c1 * y)

    a1 = 8. / 3. * y * rho * (2. * a*a + 2. * rc * a * (a + b) - a * b * rc*rc) / z - 8. * pow(rc, 3)
    a2 = 4. + 12. * rc + 4. * y * rho * a * b / z

    expr = 2.*rho*pow(rhom1, 2)*(a1/pow(d1, 3) + a2/pow(d1, 2)) * pow(qm, 4) / z
    return expr*dgam


def main():
    integral = PyMikor()

    # fcn1
    x_lim = [[0.0001, 0.9999] for _ in range(8)]
    integral.set_values(1, 8, 100003, 1, sigma=2, limits=x_lim)

    # fcn2
    # x_lim = [[0.00001, 0.99999] for _ in range(10)]
    # integral.set_values(1, 10, 1000003, 1, sigma=2, limits=x_lim)

    integral.show_parameters()

    result = integral(fcn1)*4*pow(52.768, 3)
    # result = integral(fcn2)

    print(f'\nResult: {result}')

    del integral


if __name__ == "__main__":
    main()
