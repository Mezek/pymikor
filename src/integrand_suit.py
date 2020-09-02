# Created by Erik Bartoš in 2020.
# Copyright © 2020 Erik Bartoš <erik.bartos@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version (see <http://www.gnu.org/licenses/>).
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import numpy as np
import math
import scipy.special as spec


def normalize_2(v):
    """
    Normalize vector with Euclidean norm
    :param v: input vector
    :return: normalised vector
    """
    return v/np.linalg.norm(v)


def norm1(v):
    """
    Calculate Taxicab norm of vector
    :param v: input vector
    :return: norm of vector
    """
    return math.fsum(np.fabs(v))


def norm2(v):
    """
    Calculate Euclidean norm of vector
    :param v: input vector
    :return: norm of vector
    """
    return math.sqrt(math.fsum(v*v))


class Integrand:

    def __init__(self, name, dimension):
        self.name = name
        self.__dim_n = dimension
        self.__a_pr = np.random.rand(dimension)
        self.__u = np.random.rand(dimension)
        self.__a = self.normalize_a(1, 1)

    @property
    def a_pr(self):
        return self.__a_pr

    @a_pr.setter
    def a_pr(self, apr):
        if len(apr) != self.__dim_n:
            raise AttributeError('Check dimension of a-prime parameters!')
        self.__a_pr = apr

    @property
    def u(self):
        return self.__u

    @u.setter
    def u(self, u):
        if len(u) != self.__dim_n:
            raise AttributeError('Check dimension of u parameters!')
        self.__u = u

    @property
    def a(self):
        return self.__a

    def normalize_a(self, e, h):
        """
        Normalize vector by Genz's condition
        :param e: number
        :param h: number
        :return: normalized vector
        """
        c_factor = h/math.pow(self.__dim_n, e)
        c = c_factor/norm1(self.__a_pr)
        self.__a = self.__a_pr * c
        return self.__a

    def show_parameters(self):
        print(f'\nObject class    : {self.__class__.__name__}')
        print(f'Object name     : {self.name}')
        print(f'dimension       : {self.__dim_n}')
        print(f'a-prime vector  : {self.__a_pr}')
        print(f'a vector        : {self.__a}')
        print(f'u vector        : {self.__u}')

    def check_x(self, dmx):
        """
        Check dimension of x-variable
        :param dmx: length of x-variable
        :return: implicit None
        """
        if dmx != self.__dim_n:
            raise AttributeError('Check dimension of x-variable!')

    def oscillatory_fcn(self, x):
        """
        Oscillatory function
        :param x: x-variable
        :return: f_1(x)
        """
        self.check_x(len(x))
        sma = 0.
        for i in range(self.__dim_n):
            sma += self.__a[i]*x[i]
        return math.cos(2.*math.pi*self.__u[0] + sma)

    def product_peak_fcn(self, x):
        """
        Product peak function
        :param x: x-variable
        :return: f_2(x)
        """
        self.check_x(len(x))
        res = 1.
        for i in range(self.__dim_n):
            res *= 1./(1./math.pow(self.__a[i], 2) + math.pow(x[i] - self.__u[i], 2))
        return res

    def corner_peak_fcn(self, x):
        """
        Corner peak function
        :param x: x-variable
        :return: f_3(x)
        """
        self.check_x(len(x))
        sma = 0.
        for i in range(self.__dim_n):
            sma += self.__a[i]*x[i]
        return 1./math.pow(1. + sma, (self.__dim_n + 1))

    def gaussian_fcn(self, x):
        """
        Gaussian function
        :param x: x-variable
        :return: f_4(x)
        """
        self.check_x(len(x))
        sma = 0.
        for i in range(self.__dim_n):
            sma += math.pow(self.__a[i]*(x[i] - self.__u[i]), 2)
        return math.exp(- sma)

    def c0_fcn(self, x):
        """
        C^0 function
        :param x: x-variable
        :return: f_5(x)
        """
        self.check_x(len(x))
        sma = 0.
        for i in range(self.__dim_n):
            sma += self.__a[i]*math.fabs(x[i] - self.__u[i])
        return math.exp(- sma)

    def discontinuous_fcn(self, x):
        """
        Discontinuous function
        :param x: x-variable
        :return: f_6(x)
        """
        self.check_x(len(x))
        if x[0] > self.__u[0] or x[1] > self.__u[1]:
            return 0.
        else:
            sma = 0.
            for i in range(self.__dim_n):
                sma += self.__a[i]*x[i]
            return math.exp(sma)

    def exact_oscillatory(self):
        """
        Integration of f_1(x) in limits [0, 1]^n
        :return: value of n-integral
        """
        b = 2. * math.pi * self.__u[0]
        prod = 1.
        for ael in self.__a:
            prod *= 2. * math.sin(ael / 2.) / ael
        return math.cos((2. * b + math.fsum(self.__a)) / 2.) * prod

    def exact_product_peak(self):
        """
        Integration of f_2(x) in limits [0, 1]^n
        :return: value of n-integral
        """
        prod = 1.
        for i in range(0, len(self.__a)):
            ael = self.__a[i]
            prod *= ael * (math.atan(ael*(1. - self.__u[i])) - math.atan(ael*(-self.__u[i])))
        return prod

    def exact_gaussian(self):
        """
        Integration of f_4(x) in limits [0, 1]^n
        :return: value of n-integral
        """
        prod = 1.
        for i in range(0, len(self.__a)):
            prod *= math.sqrt(math.pi)/2./self.__a[i]*(spec.erf(self.__a[i]*(1. - self.__u[i]))
                                                       - spec.erf(-self.__a[i]*self.__u[i]))
        return prod

    def exact_c0(self):
        """
        Integration of f_5(x) in limits [0, 1]^n
        :return: value of n-integral
        """
        prod = 1.
        for i in range(0, len(self.__a)):
            ael = self.__a[i]
            uel = self.__u[i]
            prod *= (math.exp(ael*(1. - uel)) + math.exp(ael*uel) - 2.)/ael
        return prod
