#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Data calculation

Produce data for PyMikor
"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from integrand import *
import csv
import vegas


def main():
    with open('data_pymikor.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["1", "a", "A"])
        writer.writerow(["2", "b", "B"])

    ndim = 4
    nods = 10009
    occur = 5
    v_integ = vegas.Integrator(ndim * [[0, 1]])
    p_integ = PyMikor()
    p_integ.set_values(1, ndim, nods, 1, sigma=2)
    fof = Integrand('FCN', ndim)
    # fof.normalize_a(2, 100)

    # v_result = v_integ(fof.oscillatory_fcn).mean
    # v_result = v_integ(fof.oscillatory_fcn, nitn=10, neval=1e3).mean

    rvec = []
    for i in range(occur):
        fof.reset_a()
        p_result = p_integ(fof.oscillatory_fcn)  # , eps=1e-4
        # p_integ.show_parameters()
        exact_res = fof.exact_oscillatory()
        p_rel_res = math.fabs((p_result - exact_res) / exact_res)
        # print(f'Relative res   : {p_rel_res:.3e}')
        rvec.append(float("{:.3e}".format(p_rel_res)))
    print(rvec)

    del p_integ


if __name__ == "__main__":
    main()
