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


class Integrand:

    def __init__(self, name, dimension):
        self.name = name
        self.__dim_n = dimension
        self.__a = np.random.rand(dimension)
        self.__u = np.random.rand(dimension)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if len(a) != self.__dim_n:
            raise AttributeError('Check dimension of a-parameters!')
        self.__a = a

    @property
    def u(self):
        return self.__u

    @u.setter
    def u(self, u):
        if len(u) != self.__dim_n:
            raise AttributeError('Check dimension of u-parameters!')
        self.__u = u

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
        return np.cos(2.*np.pi*self.__u[0] + sma)

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
