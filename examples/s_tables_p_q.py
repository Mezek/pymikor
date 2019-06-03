#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *


def main():
    max_s = 9
    p_start = 99
    p_step = 1000
    max_n_nodes = 100000
    integral = Mikor()
    integral.show_parameters()
    print('Spawning numbers...')

    # coefficientsPQ.txt
    with open('coefficients.txt', 'w') as f:
        f.write('Tables of optimal coefficients\n')


if __name__ == "__main__":
    main()
