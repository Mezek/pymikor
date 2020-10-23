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


def format_num(f):
    return float("{:.3e}".format(f))


def proceed_err(ndim, nods, nt):
    p_integ = PyMikor()
    fof = Integrand('FCN', ndim)
    # fof.normalize_a(2, 100)
    exact_res = fof.exact_oscillatory()
    v_integ = vegas.Integrator(ndim * [[0, 1]])
    v_result = v_integ(fof.oscillatory_fcn).mean
    # v_result = v_integ(fof.oscillatory_fcn, nitn=10, neval=1e3).mean
    v_rel_res = math.fabs((v_result - exact_res) / exact_res)
    v_rel_res = format_num(v_rel_res)

    r_vec = []
    for tab_prime in nods:
        p_integ.set_values(1, ndim, tab_prime, 1, sigma=2)
        p_result = p_integ(fof.oscillatory_fcn)  # , eps=1e-4
        # p_integ.show_parameters()
        p_rel_res = math.fabs((p_result - exact_res) / exact_res)
        r_vec.append(format_num(p_rel_res))

    with open('data_pymikor.csv', 'a', newline='') as file:
        wr = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        wr.writerow([nt, ndim, v_rel_res] + r_vec)

    del p_integ, v_integ


def main():
    ndim = 4
    nods = np.array([1259, 10007, 100003, 1000003])

    with open('data_pymikor.csv', 'w', newline='') as file:
        wr = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        header = ['A', 'NDim', 'Vegas']
        for el in nods:
            header.append(el)
        wr.writerow(header)

    for i in range(10):
        proceed_err(ndim, nods, i+1)


if __name__ == "__main__":
    main()
