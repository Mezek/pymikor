#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test integrand suit by Genz

"""
__author__ = "Erik Bartoš"
__copyright__ = "Copyright © 2020 Erik Bartoš"
__email__ = "erik.bartos@gmail.com"

from pymikor import *
from integrand_suit import *


def one_fcn():
    print(np.finfo(np.float))

    nd = 13
    nod = 10003
    integral = PyMikor()
    integral.set_values(1, nd, nod, 1, sigma=2)
    fof = Integrand('FCN', nd)
    # fof.normalize_a(2, 600)
    result = integral(fof.corner_peak_fcn)
    exact_res = fof.exact_corner_peak()
    diff_res = (result - exact_res)
    rel_res = (result - exact_res) / exact_res
    print(f'\nFCN:')
    print(f'{result:.10e}')
    print(f'{exact_res:.10e}')
    print(f'{diff_res:.3e}')
    print(f'{rel_res:.3e}')


def main():
    with open('coefficients.txt', 'w') as f:
        f.write('Genz suit')

    integral = PyMikor()
    nd = (3, 5, 8, 10, 13, 15)
    prnb = (1259, 10007, 100003, 1000003)
    for idn in nd:
        with open('coefficients.txt', 'a') as f:
            f.write('\nDimension: ' + str(idn))
        for nod in prnb:
            integral.set_values(1, idn, nod, 1, sigma=2)
            # integral.show_parameters()
            fof = Integrand('FCN', idn)
            fof.normalize_a(2, 600)
            with open('coefficients.txt', 'a') as f:
                f.write(f'\nN={nod:12.0f}')
                # fof.show_parameters()

                f.write('   1:')
                result = integral(fof.oscillatory_fcn)
                exact_res = fof.exact_oscillatory()
                diff_res = (result - exact_res)/exact_res
                f.write(f'{diff_res:.3e}')
                print(f'\n1: Oscillatory:')
                print(f'{result:.10e}')
                print(f'{exact_res:.10e}')
                print(f'{diff_res:.3e}')

                f.write('   2:')
                result = integral(fof.product_peak_fcn)
                exact_res = fof.exact_product_peak()
                diff_res = (result - exact_res)/exact_res
                f.write(f'{diff_res:.3e}')
                print(f'\n2: Product peak:')
                print(f'{result:.10e}')
                print(f'{exact_res:.10e}')
                print(f'{diff_res:.3e}')

                f.write('   3:')
                result = integral(fof.corner_peak_fcn)
                exact_res = fof.exact_corner_peak()
                diff_res = (result - exact_res)/exact_res
                f.write(f'{diff_res:.3e}')
                print(f'\n5: Corner peak:')
                print(f'{result:.10e}')
                print(f'{exact_res:.10e}')
                print(f'{diff_res:.3e}')

                f.write('   4:')
                result = integral(fof.gaussian_fcn)
                exact_res = fof.exact_gaussian()
                diff_res = (result - exact_res)/exact_res
                f.write(f'{diff_res:.3e}')
                print(f'\n3: Gaussian:')
                print(f'{result:.10e}')
                print(f'{exact_res:.10e}')
                print(f'{diff_res:.3e}')

                f.write('   5:')
                result = integral(fof.c0_fcn)
                exact_res = fof.exact_c0()
                diff_res = result - exact_res
                f.write(f'{diff_res:.3e}')
                print(f'\n4: C0:')
                print(f'{result:.10e}')
                print(f'{exact_res:.10e}')
                print(f'{diff_res:.3e}')

                f.write('   6:')
                result = integral(fof.discontinuous_fcn)
                exact_res = fof.exact_discontinuous()
                diff_res = (result - exact_res)/exact_res
                f.write(f'{diff_res:.3e}')
                print(f'\n6: Discontinuous:')
                print(f'{result:.10e}')
                print(f'{exact_res:.10e}')
                print(f'{diff_res:.3e}')

    del integral


if __name__ == "__main__":
    # one_fcn()
    main()
