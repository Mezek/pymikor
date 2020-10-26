#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Data calculation

Produce data for PyMikor + PyCuba
"""
from __future__ import absolute_import, unicode_literals, print_function

__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from integrand import *
import csv
import pycuba


def format_num(f):
    return float("{:.3e}".format(f))


def IntegCuba(ndim, xx, ncomp, ff, userdata):
    # x, y, z = [xx[i] for i in range(ndim.contents.value)]
    result = xx[0] ** 2 * xx[1] ** 3 * xx[2] * 24.
    ff[0] = result
    print(ave)
    return 0


def print_header(name):
    print('-------------------- %s test -------------------' % name)


def print_results(name, results):
    keys = ['nregions', 'neval', 'fail']
    text = ["%s %d" % (k, results[k]) for k in keys if k in results]
    print("%s RESULT:\t" % name.upper() + "\t".join(text))
    for comp in results['results']:
        print("%s RESULT:\t" % name.upper() +
              "%(integral).8f +- %(error).8f\tp = %(prob).3f\n" % comp)


def proceed_err(ndim, nods, nt):
    r_vec = [nt, ndim]
    p_integ = PyMikor()
    fof = Integrand('FCN', ndim)
    # fof.normalize_a(1.5, 110)
    exact_res = fof.exact_oscillatory()

    NDIM = 3
    NCOMP = 1

    NNEW = 1000
    NMIN = 2
    FLATNESS = 50.

    KEY1 = 47
    KEY2 = 1
    KEY3 = 1
    MAXPASS = 5
    BORDER = 0.
    MAXCHISQ = 10.
    MINDEVIATION = .25
    NGIVEN = 0
    LDXGIVEN = NDIM
    NEXTRA = 0
    MINEVAL = 0
    MAXEVAL = 50000

    KEY = 0

    global ave
    ave = fof.a

    print_header('Vegas')
    vrs = pycuba.Vegas(IntegCuba, NDIM, verbose=0)
    print_results('Vegas', vrs)
    v_result = []
    v_result.append(vrs['results'][0]['integral'])

    print_header('Divonne')
    cub = pycuba.Divonne(IntegCuba, NDIM, mineval=MINEVAL, maxeval=MAXEVAL,
                         key1=KEY1, key2=KEY2, key3=KEY3, maxpass=MAXPASS,
                         border=BORDER, maxchisq=MAXCHISQ, mindeviation=MINDEVIATION,
                         ldxgiven=LDXGIVEN, verbose=0)
    print_results('Divonne', cub)
    v_result.append(cub['results'][0]['integral'])

    for v in v_result:
        v = math.fabs((v - exact_res) / exact_res)
        r_vec.append(format_num(v))

    for tab_prime in nods:
        p_integ.set_values(1, ndim, tab_prime, 1, sigma=2)
        p_result = p_integ(fof.oscillatory_fcn)  # , eps=1e-4
        # p_integ.show_parameters()
        p_rel_res = math.fabs((p_result - exact_res) / exact_res)
        r_vec.append(format_num(p_rel_res))

    with open('data_f_osc_cuba.csv', 'a', newline='') as file:
        wr = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        wr.writerow(r_vec)

    del p_integ


def main():
    ndim = [3]
    nods = np.array([1259, 10007])

    with open('data_f_osc_cuba.csv', 'w', newline='') as file:
        wr = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        header = ['A', 'NDim', 'Vegas', 'PyCuba']
        for el in nods:
            header.append(el)
        wr.writerow(header)

    for i in range(len(ndim)):
        for j in range(1):
            proceed_err(ndim[i], nods, j+1)
            # print(i, j+1, ndim[i], nods)


if __name__ == "__main__":
    main()
