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
    integral.set_values(13, 5, 1000)
    integral.show_parameters()
    print('H(z) =', integral.h_funct())

    a = -123.456
    print(fraction(a))


if __name__ == "__main__":
    main()