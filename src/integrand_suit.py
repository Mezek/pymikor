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


class Integrand:

    def __init__(self, name, dimension):
        self.name = name
        self.__dim_n = dimension
        self.__a = np.random.rand(dimension)
        self.__u = np.random.rand(dimension)

    def oscillatory_fcn(self, x, *par):
        if len(x) != self.__dim_n:
            raise AttributeError('Dimension of arguments is not correct!')
        if len(*par) != len(x):
            raise AttributeError('Number of parameters is not correct!')
        res = 0.
        for i in range(len(x)):
            res += x[i]**2
        print('Arguments: ', *par)
        print('Random:    ', self.__a)
        return res

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
