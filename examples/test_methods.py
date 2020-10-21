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
    ndim = 7
    nods = 10009
    v_integ = vegas.Integrator(ndim * [[0, 1]])
    p_integ = PyMikor()
    p_integ.set_values(1, ndim, nods, 1, sigma=2)
    fof = Integrand('FCN', ndim)
    # fof.normalize_a(1, 500)
    fof.show_parameters()

    v_result = v_integ(fof.corner_peak_fcn).mean
    # v_result = v_integ(fof.oscillatory_fcn, nitn=10, neval=1e3).mean
    p_result = p_integ(fof.corner_peak_fcn)  # , eps=1e-4
    # p_integ.show_parameters()
    # # c_result = cuba Divone
    # exact_res = fof.exact_corner_peak()
    exact_res = fof.exact_corner_peak()
    print(f'\nExact result   : {exact_res:.12e}')

    v_rel_res = math.fabs((v_result - exact_res) / exact_res)
    print(f'       Vegas   : {v_result:.8e}')
    p_rel_res = math.fabs((p_result - exact_res) / exact_res)
    print(f'     PyMikor   : {p_result:.8e}')
    # # c_rel_res = (c_result - exact_res) / exact_res

    print(f'Relative res   : {v_rel_res:.3e} / {p_rel_res:.3e}')

    del p_integ


if __name__ == "__main__":
    main()
