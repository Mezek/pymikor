#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Comparison of algorithms: PyMikor, Vegas, Cuba
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from integrand import *
import vegas


def main():
    ndim = 3
    nods = 10009
    v_integ = vegas.Integrator(ndim * [[0, 1]])
    p_integ = PyMikor()
    p_integ.set_values(1, ndim, nods, 1, sigma=2)
    fof = Integrand('FCN', ndim)
    fof.normalize_a(5, 100)

    v_result = v_integ(fof.oscillatory_fcn)
    # v_result = v_integ(fof.oscillatory_fcn, nitn=10, neval=1e3)
    p_result = p_integ(fof.oscillatory_fcn)  # , eps=1e-4
    p_integ.show_parameters()
    # # c_result = cuba Divone
    # exact_res = fof.exact_corner_peak()
    exact_res = fof.exact_oscillatory()

    v_rel_res = (v_result - exact_res) / exact_res
    p_rel_res = (p_result - exact_res) / exact_res
    # # c_rel_res = (c_result - exact_res) / exact_res

    print(f'\nResult of integration   : {exact_res}')
    print(f'\nRelative result         : {v_rel_res} / {p_rel_res}')

    del p_integ


if __name__ == "__main__":
    # one_fcn()
    main()
