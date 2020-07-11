#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Vegas algorithm estimates

G. P. Lepage, J. Comput. Phys. 27 (1978) 192
https://doi.org/10.1016/0021-9991(78)90004-9
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2019 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

import vegas
import math
import numpy as np


def f(x):
    dim = len(x)
    norm = 1013.2118364296088 ** (dim / 4.)
    dx2 = 0.0
    for d in range(dim):
        dx2 += (x[d] - 0.5) ** 2
    return math.exp(-100. * dx2) * norm


def fcn1(x):
    f = 1
    for i in range(4):
        dblx = x[i]*x[i]
        if dblx > 1.0:
            dblx = 1.0
        f *= x[i]*math.sqrt(1. - dblx)
    return 81*f


integ = vegas.Integrator(4 * [[0, 1]])

# integ(fcn1, nitn=10, neval=2e5)
result = integ(fcn1, nitn=10, neval=10000)
print(result.summary())
print('result = %s   Q = %.2f' % (result, result.Q))

"""
@vegas.batchintegrand
def f_batch(x):
    # evaluate integrand at multiple points simultaneously
    dim = x.shape[1]
    norm = 1013.2118364296088 ** (dim / 4.)
    dx2 = 0.0
    for d in range(dim):
        dx2 += (x[:, d] - 0.5) ** 2
    return np.exp(-100. * dx2) * norm


integ = vegas.Integrator(4 * [[0, 1]])

integ(f_batch, nitn=10, neval=2e5)
result = integ(f_batch, nitn=10, neval=2e5)
# print(result.summary())
print('result = %s   Q = %.2f' % (result, result.Q))
"""