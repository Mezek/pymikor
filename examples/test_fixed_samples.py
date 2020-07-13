#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Integrating functions

Methods for integrating by given fixed samples
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from math import *
from scipy.integrate import *
import sympy


def fcn1(x):
    f = 1
    for i in range(6):
        dblx = x[i]*x[i]
        if dblx > 1.0:
            dblx = 1.0
        f *= x[i]*sqrt(1. - dblx)
    return 729*f


def fcn2(x):
    f = 1
    for i in range(6):
        f *= exp(x[i])/(math.e - 1.)
    return f


def fcn3(x):
    f = 1
    for i in range(6):
        f *= math.pi/2.*sin(math.pi*x[i])
    return f


def fcn7(x):
    return 3.*x[0]*x[0] + 4.*x[1]*x[2] + 8.*x[3]*x[4]*x[5] + 7.*pow(x[6], 6)


def fcn1s(x):
    return x*sqrt(1. - x*x)


def fcn2s(x):
    return exp(x)/(math.e - 1.)


def fcn3s(x):
    return math.pi/2.*sin(math.pi*x)


def prime_val(i):
    x = np.linspace(0, 1, i)
    fcn2sv = np.vectorize(fcn2s)
    res1a = simps(fcn2sv(x), x)
    res1b = trapz(fcn2sv(x), x)

    print("Number: ", i)
    print("Simps: ", np.power(res1a, 6))
    print("Trapz: ", np.power(res1b, 6))

    integral = Mikor()
    integral.set_values(1, 6, i, 1, sigma=3, eps=0.)
    # integral.show_parameters()
    res1 = integral(fcn2)
    print("Mikor: ", res1)


def main():
    fs = np.array([# 53, 101, 151, 307, 523, 829,
                    1259, 2129, 3001, 4001, 5003,
                   6007, 8191, 10007, 13001, 20011, 30011, 40009, 50021])
    # for i in fs:
    #    prime_val(n_prime(i))

    x = np.linspace(0, 1, 20)
    y = np.linspace(0, 1, 30)
    z = np.cos(x[:, None]) ** 4 + np.sin(y) ** 2
    print(simps(simps(z, y), x))
    xx, yy = sympy.symbols('x y')
    print(sympy.integrate(sympy.cos(xx) ** 4 + sympy.sin(yy) ** 2, (xx, 0, 1), (yy, 0, 1)).evalf())

    x, y, z, w = sympy.symbols("x y z w")
    f = x*sympy.sqrt(1. - x*x)*y*sympy.sqrt(1. - y*y)*z*sympy.sqrt(1. - z*z)*w*sympy.sqrt(1. - w*w)
    res = sympy.integrate(f, (w, 0, 1), (z, 0, 1), (y, 0, 1), (x, 0, 1))
    print(81*res)


if __name__ == "__main__":
    main()
