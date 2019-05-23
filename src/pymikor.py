import math
import numpy as np
from decimal import *
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
        self.dimS = 4
        self.dimR = 1
        self.nNodes = 100

    def check_numbers(self):
        if self.nNodes <= self.dimS:
            raise ValueError('Integral dimension s must be < N nodes!')

    def set_values(self, dim_s, dim_r, nodes):
        """
        Class Mikor
        :param dim_s: Dimension of integral
        :param dim_r: Dimension of result
        :param nodes: Number of nodes
        :return:
        """
        self.dimS = dim_s
        self.dimR = dim_r
        self.nNodes = nodes
        assert (self.dimS < self.nNodes), "Integral dimension s must be < N nodes!"

    def n_prime(self):
        """
        Find prime p >= n
        :return: prime p >= n
        """
        next_prime = self.nNodes
        while not is_prime(next_prime):
            next_prime = next(filter(is_prime, count(next_prime)))
        return next_prime

    def h_poly_orig(self):
        p = self.n_prime()
        z = np.arange(1, p, 1)
        return z

    def h_poly(self, z):
        s = self.dimS
        # n = self.nodes
        n = 13
        hval = pow(s, 3) / n
        return hval

    def first_optimal(self):
        print('Optimal coefficient:')
        pno = self.n_prime()
        s = self.dimS
        print('nodes %s : %s prime' % (self.nNodes, pno))

        p = int((pno - 1)/2)
        z = np.arange(1, p + 1, 1)
        print('z =', z[-5:])
        """
        for i in range(1, p + 1):
            a = np.ones(s)
            ak = np.ones(s)
            b = np.ones(s)
            zs = 1
            for j in range(s):
                a[j] = zs/p
                zs = zs*i % p
                ak[j] = fraction(a[j])

            for j in range(s):
                b[j] = fraction(pow(i, j)/p)

            if i > 500:
                print(i, ak, b, ak - b)
        """
        c = Decimal(1008**13 / 5)
        print(c, Decimal(c*5), fraction(c))
        return 0

    def optimal_coeffs(self):
        return 0

    def show_parameters(self):
        print('Object class            :', self.__class__.__name__)
        print('dimension of integration:', self.dimS)
        print('dimension of result     :', self.dimR)
        print('number of nodes         :', self.nNodes)
