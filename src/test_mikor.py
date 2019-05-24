#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *


def f(x):
    df = 0
    for d in range(len(x)):
        df += x[d]
    return df


def main():
    integral = Mikor()
    integral.set_values(8, 2, 1011)
    integral.show_parameters()

    print(integral.optimal_coeffs(integral.first_optimal()[0]))


if __name__ == "__main__":
    main()