#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Integration of function

Evaluation of known integrals
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *


def fcn1(x):
    return np.exp(x[1] - x[0])


def fcn_la(a1, a2, m1, m2, lp, mp, gp):
    om1 = m1/(m1 + m2)
    om2 = m2/(m1 + m2)
    a = 1./lp/lp + a1 + a2
    mp2 = mp*mp
    ear = -a1*m1*m1 - a2*m2*m2 + (a1*om1*om1 + a2*om2*om2)*mp2\
          - pow((a1*om1 - a2*om2), 2)*mp2/a
    e_t = np.exp(ear)
    m_t = (m1 - m2)/pow(a, 3)*(a1*om1 - a2*om2) + (m1*om2 + m2*om1)/pow(a, 2)
    return 3./4.*gp/pow(np.pi, 2)*e_t*m_t


def fcn_p(x, *args):
    m1 = 0.235
    m2 = 0.235
    lp = 0.87
    # lcut = 0.181
    mp = 0.14
    gp = 5.133

    t = x[0]
    a = x[1]
    tm1 = 1. - t
    am1 = 1. - a
    ddx = t/pow(tm1, 3)
    ddy = fcn_la(t*a/tm1, t*am1/tm1, m1, m2, lp, mp, gp)
    return ddx*ddy


def main():

    integral = Mikor()

    # # fcn1
    # x_lim = [[0., 0.5] for _ in range(2)]
    # integral.set_values(3, 2, 1009, 1, sigma=2, limits=x_lim)
    # integral.show_parameters()
    # result = integral(fcn1)
    # ex_fcn1 = np.exp(-0.5) + np.exp(0.5) - 2.
    # print(f'\nResult: {result}')
    # print(f'Exact:  {ex_fcn1}')
    # print(f'Diff:  ', (result - ex_fcn1))

    # fcn2
    l_cut = 0.181
    x_lim = [[0., 1./(l_cut*l_cut + 1.)], [0., 1.]]
    integral.set_values(3, 2, 1003, 1, sigma=2, limits=x_lim)
    integral.show_parameters()
    result = integral(fcn_p)
    print(f'\nResult: {result}')

    v = np.array([1, 2, 3])
    normalized_v = v / np.sqrt(np.sum(v ** 2))
    print(normalized_v)

    del integral


if __name__ == "__main__":
    main()
