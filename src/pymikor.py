import math
import numpy as np
from itertools import count


def fraction(n):
    f, i = math.modf(n)
    # alternative: f = n - int(n)
    return f


def is_prime(n):
    # if n in (2, 3, 5, 7, 11):  # special case small primes
    #    return True
    if n % 2 == 0 or n == 1:  # special case even numbers and 1
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


class Mikor:

    def __init__(self):
        self.dim_s = 4
        self.dim_r = 1
        self.n_nodes = self.n_prime(100)

    def check_numbers(self):
        if self.n_nodes <= self.dim_s:
            raise ValueError('Integral dimension s must be < N nodes!')

    def set_values(self, dims, dres, nodes):
        """
        Class Mikor
        :param dims: Dimension of integral
        :param dres: Dimension of result
        :param nodes: Number of nodes, is converted to first prime number
        :return:
        """
        self.dim_s = dims
        self.dim_r = dres
        self.n_nodes = self.n_prime(nodes)
        assert (self.dim_s < self.n_nodes), "Integral dimension s must be < N nodes!"

    def n_prime(self, nodes):
        """
        Find prime p >= n
        :param nodes: Number of nodes
        :return: prime p >= n
        """
        next_prime = nodes
        while not is_prime(next_prime):
            next_prime = next(filter(is_prime, count(next_prime)))
        return next_prime

    def h_sum(self, s, ub, z):
        return 0

    def h_poly(self, z):
        return 0

    def h_poly_chet(self, z):
        return 0

    def first_optimal(self):
        n_orig = self.n_nodes
        s = self.dim_s
        p = int((n_orig - 1)/2)
        z = np.arange(1, p + 1, 1)
        # print('z =', z[-5:])
        optimal_a = 0
        optimal_val = 1e+18

        for i in range(1, p + 1):
            a = np.ones(s)
            hpoly = 0
            zs = 1
            for j in range(s):
                a[j] = zs/p
                zs = (zs*i) % p
            for k in range(1, p + 1):
                kterm = 1.
                for l in range(s):
                    ent = fraction(k*a[l])
                    kterm = kterm*(1. - ent - ent)
                hpoly = hpoly + kterm*kterm
            if hpoly < optimal_val:
                optimal_a = i
                optimal_val = hpoly
            if i % 1000 == 0:
                print('%i. iteration' % i)
        return optimal_a, optimal_val

    def optimal_coeffs(self, opt):
        s = self.dim_s
        a = np.ones(s)
        a[1] = opt
        for i in range(2, s):
            a[i] = (a[i-1]*opt) % self.n_nodes
        return a

    def show_parameters(self):
        print('Object class            :', self.__class__.__name__)
        print('dimension of integration:', self.dim_s)
        print('dimension of result     :', self.dim_r)
        print('number of nodes         :', self.n_nodes)
