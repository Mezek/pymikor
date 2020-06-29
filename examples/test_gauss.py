#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""General integration using Gaussian quadrature

Methods for integrating functions objects
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from scipy.integrate import quad


def integrand(x, a, b):
    return a*x**2 + b


def main():
    I = quad(integrand, 0, 1, args=(2, 1))
    print("Integral = ", I)


if __name__ == "__main__":
    main()
