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
    r_vec = [nt, ndim]
    p_integ = PyMikor()
    fof = Integrand('FCN', ndim)
    # fof.normalize_a(1.5, 110)
    exact_res = fof.exact_oscillatory()
    v_integ = vegas.Integrator(ndim * [[0, 1]])
    v_result = []
    v_result.append(v_integ(fof.oscillatory_fcn, nitn=10, neval=1e3).mean)
    v_result.append(v_integ(fof.oscillatory_fcn, nitn=10, neval=1e5).mean)
    for v in v_result:
        v = math.fabs((v - exact_res) / exact_res)
        r_vec.append(format_num(v))

    for tab_prime in nods:
        p_integ.set_values(1, ndim, tab_prime, 1, sigma=2)
        # p_result = p_integ(fof.oscillatory_fcn)  # , eps=1e-4
        p_result = 1.
        # p_integ.show_parameters()
        p_rel_res = math.fabs((p_result - exact_res) / exact_res)
        r_vec.append(format_num(p_rel_res))

    with open('data_f_oscillatory.csv', 'a', newline='') as file:
        wr = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        wr.writerow(r_vec)

    del p_integ, v_integ


def main():
    ndim = [3, 5, 8, 10, 13, 15]
    nods = np.array([1259, 10007, 100003, 1000003])

    with open('data_f_oscillatory.csv', 'w', newline='') as file:
        wr = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        header = ['A', 'NDim', 'VegasA', 'VegasB']
        for el in nods:
            header.append(el)
        wr.writerow(header)
    for i in range(len(ndim)):
        for j in range(100):
            proceed_err(ndim[i], nods, j+1)
            # print(i, j+1, ndim[i], nods)


if __name__ == "__main__":
    main()
