#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Erik Bartoš <erik.bartos@gmail.com>

from pymikor import *
import vegas


def fcn(x):
    return 3.*x[0]*x[0] + 4.*x[1]*x[2]


def fcn1(x):
    df = 0
    for d in range(len(x)):
        df += x[d]
    return df


def fcn2(x):
    df = 1
    for d in range(len(x)):
        df *= x[d]
    return df


def fcn3(x):
    fc = 0
    for i in range(4):
        fc += 0.5*math.pi*math.sin(math.pi*x[i])
    return fc


def fcn_g1(x):
    fc = math.exp(x[0]*x[1]*x[2])
    return fc


def fcn_g2(x):
    fc = 1.
    a = np.array([1, 0.5, 0.2, 0.2, 0.2])
    for i in range(5):
        dd = 0.
        for j in range(5):
            if j != i:
                dd += x[j]
        ss = 0.5*a[i]*x[i]*x[i]*(2. + math.sin(dd))
        fc *= math.exp(ss)
    return fc


def fcn_g3(x):
    fc = 1
    for i in range(8):
        fc *= math.exp(0.1*x[i])
    return fc


def fcn_g4(x):
    xx = 1.
    for i in range(20):
        xx *= x[i]
    return math.exp(xx)


def fcn_fa(x):
    xx = 1.
    for i in range(10):
        xx *= (i + 1)
        for j in range(i):
            xx *= x[i]
    return xx


def fcn_fb(x):
    xx = 0.
    if x[1] <= 0.5 and x[2] <= 1./3. and x[3] <= 2./3.:
        if 1./3. <= x[4] <= 0.5:
            xx = 1.
    return xx


def fcn_f5(x):
    xx = 1.
    for i in range(5):
        xx *= 1./math.sqrt(2.*math.pi)*math.exp(-0.5*x[i]*x[i])
    return xx


def fcn_f10(x):
    xx = 1.
    for i in range(10):
        xx *= 1./math.sqrt(2.*math.pi)*math.exp(-0.5*x[i]*x[i])
    return xx


def main():
    integral = PyMikor()
    """
    # Listing example 1
    integral.set_values(2, 4, 1009, 1, sigma=2,
                        limits=[[0, 1], [0, 1], [0, 1], [0, 1]])
    # integral.set_dpq(3, 907, 31)
    integral.show_parameters()

    result = integral(fcn, eps=1e-5, stat=1)
    # integral.show_parameters()
    print(f'\nResult of integration   : {result}')
    """
    integral.set_values(1, 3, 10009, 1, sigma=2,
                        limits=[[0, 1], [0, 1], [0, 1]])
    # integral.tabulated_optimals()
    p_result = integral(fcn_g1, eps=1e-5, stat=1)
    print(f'PyMikor   : {p_result:.8e}')
    v_integ = vegas.Integrator(3 * [[0, 1]])
    v_result = v_integ(fcn_g1, nitn=10, neval=1e3).mean
    print(f'  Vegas   : {v_result:.12e}')
    print(f' Approx   : {1.14649907}')
    """
    integral.set_values(1, 5, 100009, 1, sigma=2,
                        limits=[[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]])
    p_result = integral(fcn_g2, eps=1e-5)
    print(f'PyMikor   : {p_result:.8e}')
    v_integ = vegas.Integrator(5 * [[0, 1]])
    v_result = v_integ(fcn_g2, nitn=10, neval=1e4).mean
    print(f'  Vegas   : {v_result:.8e}')
    print(f' Approx   : {2.923651}')
    """
    """
    integral.set_values(1, 8, 100009, 1, sigma=2,
                        limits=[[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
                                [0, 1], [0, 1]])
    p_result = integral(fcn_g3, eps=1e-5)
    print(f'PyMikor   : {p_result:.8e}')
    e_result = math.pow((math.exp(0.1) - 1.)/0.1, 8)
    print(f'  Exact   : {e_result:.12e}')
    """
    """
    integral.set_values(1, 20, 100009, 1, sigma=2,
                        limits=[[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
                                [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
                                [0, 1], [0, 1], [0, 1], [0, 1]])
    p_result = integral(fcn_g4)
    print(f'PyMikor   : {p_result:.12e}')
    v_integ = vegas.Integrator(20 * [[0, 1]])
    v_result = v_integ(fcn_g4, nitn=10, neval=1e3).mean
    print(f'  Vegas   : {v_result:.12e}')
    print(f' Approx   : {1.00000949634}')
    """
    """
    integral.set_values(1, 10, 100009, 1, sigma=2,
                        limits=[[0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
                                [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]])
    p_result = integral(fcn_fa, stat=True)
    print(f'PyMikor   : {p_result:.12e}')
    v_integ = vegas.Integrator(10 * [[0, 1]])
    v_result = v_integ(fcn_fa, nitn=10, neval=1e4).mean
    print(f'  Vegas   : {v_result:.12e}')
    print(f'  Exact   : {1.:.12e}')
    """
    """
    integral.set_values(1, 5, 1000009, 1, sigma=2,
                        limits=[[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]])
    p_result = integral(fcn_fb, stat=True)
    print(f'PyMikor   : {p_result:.12e}')
    v_integ = vegas.Integrator(5 * [[0, 1]])
    v_result = v_integ(fcn_fb, nitn=10, neval=1e5).mean
    print(f'  Vegas   : {v_result:.12e}')
    print(f'  Exact   : {1./54.:.12e}')
    """
    """
    integral.set_values(2, 5, 10009, 1, sigma=2,
                        limits=[[-5, 5], [-5, 5], [-5, 5], [-5, 5], [-5, 5]])
    p_result = integral(fcn_f5, stat=True)
    print(f'PyMikor   : {p_result:.12e}')
    v_integ = vegas.Integrator(5 * [[-5, 5]])
    v_result = v_integ(fcn_f5, nitn=10, neval=1e4).mean
    print(f'  Vegas   : {v_result:.12e}')
    print(f'  Exact   : {1.:.12e}')
    """
    """
    integral.set_values(2, 10, 10009, 1, sigma=2,
                        limits=[[-5, 5], [-5, 5], [-5, 5], [-5, 5], [-5, 5],
                                [-5, 5], [-5, 5], [-5, 5], [-5, 5], [-5, 5]])
    p_result = integral(fcn_f10, stat=True)
    print(f'PyMikor   : {p_result:.12e}')
    v_integ = vegas.Integrator(10 * [[-5, 5]])
    v_result = v_integ(fcn_f10, nitn=10, neval=1e4).mean
    print(f'  Vegas   : {v_result:.12e}')
    print(f'  Exact   : {1.:.12e}')
    """

    del integral


if __name__ == "__main__":
    main()
