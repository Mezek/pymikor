import math
import numpy as np
from itertools import count


class Mikor:

    def __init__(self):
        self.dimS = 4
        self.dimN = 1
        self.nodesN = 100

    def check_numbers(self):
        if self.nodesN <= self.dimS:
            raise ValueError('Integral dimension s must be < N nodes!')

    def set_values(self, dim_s, dim_n, nodes):
        """
        Class Mikor
        :param dim_s: Dimension of integral
        :param dim_n: Dimension of result
        :param nodes: Number of nodes
        :return:
        """
        self.dimS = dim_s
        self.dimN = dim_n
        self.nodesN = nodes
        assert (self.dimS < self.nodesN), "Integral dimension s must be < N nodes!"

    def is_prime(self, n):
        # if n in (2, 3, 5, 7, 11):  # special case small primes
        #    return True
        if n % 2 == 0 or n == 1:  # special case even numbers and 1
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def n_prime(self, n):
        """
        Find prime p >= n
        :param n: number
        :return: prime p >= n
        """
        next_prime = n
        while not self.is_prime(next_prime):
            next_prime = next(filter(self.is_prime, count(next_prime)))
        return next_prime

    def h_funct(self):
        s = self.dimS
        # n = self.nodes
        n = 13
        z = np.arange(1, n, 1)
        hval = pow(s, 3)/n
        return hval

    def find_min_h(self):
        a = []
        return a

    def show_parameters(self):
        print('Object class            :', self.__class__.__name__)
        print('dimension of integration:', self.dimS)
        print('dimension of result     :', self.dimN)
        print('number of nodes         :', self.nodesN)

