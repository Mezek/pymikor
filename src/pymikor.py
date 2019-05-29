import math
import numpy as np
from itertools import count


def fraction(n):
    """
    Fractional part of real number n
    :param n: real number
    :return: fractional part
    """
    f, i = math.modf(n)
    # alternative: f = n - int(n)
    return f


def is_prime(n):
    """
    Check if n is prime number
    :param n: number
    :return: True/False
    """
    # if n in (2, 3, 5, 7, 11):  # special case small primes
    #    return True
    if n % 2 == 0 or n == 1:  # special case even numbers and 1
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def n_prime(n):
    """
    Find prime p >= n
    :param n: Number of nodes
    :return: prime p >= n
    """
    next_prime = n
    while not is_prime(next_prime):
        next_prime = next(filter(is_prime, count(next_prime)))
    return next_prime


class Mikor:

    def __init__(self):
        self.dim_s = 4
        self.dim_r = 1
        self.n_nodes = n_prime(1000)
        self.p_prime = self.n_nodes
        self.q_prime = 1
        self.a_arr = np.empty(self.dim_s)
        self.b_arr = np.empty(self.dim_s)

    def __del__(self):
        print('Object %s deleted' % self.__class__.__name__)

    def check_numbers(self):
        if self.n_nodes <= self.dim_s:
            raise ValueError('Integral dimension s must be < N nodes!')

    def set_values(self, dims, dres, nodes):
        """
        Class Mikor
        :param dims: Dimension of integral
        :param dres: Dimension of result
        :param nodes: Number of nodes, is converted to first prime number.
                      If nodes > 8000 divided to p, q
        :return:
        """
        self.dim_s = dims
        self.dim_r = dres
        self.n_nodes = int(nodes)
        assert (self.dim_s < nodes), "Integral dimension s must be < N nodes!"
        if nodes > 10007:
            self.p_prime = n_prime(int(pow(self.n_nodes, 2/3)))
            self.q_prime = n_prime(int(pow(self.n_nodes, 1/3)))
        else:
            self.p_prime = n_prime(self.n_nodes)
        self.a_arr = np.empty(self.dim_s)
        self.b_arr = np.empty(self.dim_s)

    def h_sum(self, upperb, z):
        """
        Summation in H(z) function without coefficient
        :param upperb: upper bound of summation
        :param z: polynomial parameter
        :return: sum in H(z) function
        """
        s = self.dim_s
        p = self.p_prime
        a = np.ones(s)
        sm_k = 0
        zs = 1
        for j in range(s):
            a[j] = zs / p
            zs = (zs*z) % p
        for k in range(1, upperb + 1):
            k_term = 1.
            for l in range(s):
                ent = fraction(k*a[l])
                k_term = k_term*(1. - ent - ent)
            sm_k = sm_k + k_term*k_term
        return sm_k

    def h_poly(self, z):
        """
        Equation (196) in Korobov's book
        :param z: polynomial parameter
        :return: sum k = 1,2,...,N
        """
        return pow(3, self.dim_s)/self.p_prime*self.h_sum(self.p_prime, z)

    def h_poly_chet(self, z):
        """
        Equation (206) in Korobov's book, faster summation
        :param z: polynomial parameter
        :return: sum k = 1,2,...,(N-1)/2
        """
        p = int((self.p_prime - 1)/2)
        chet = pow(3, self.dim_s)/self.p_prime*(1. + 2.*self.h_sum(p, z))
        return chet

    def first_optimal(self):
        """
        Find first optimal value z = a
        :return: tuple of (a value, H(a) value)
        """
        p = self.p_prime
        upran = int((p - 1)/2)
        optimal_a = 0
        optimal_val = 1e+18

        for i in range(1, upran + 1):
            h_sum = self.h_poly_chet(i)
            if h_sum < optimal_val:
                optimal_a = i
                optimal_val = h_sum
            if i % 1000 == 0:
                print('%i. iteration' % i)
        return optimal_a, optimal_val

    def more_optimal(self, err_limit):
        """
        Find more optimal values z = a, to check with Saltykov's values
        :param err_limit: error limit
        :return: array of optimal values
        """
        p = self.p_prime
        upran = int((p - 1)/2)
        first_a, first_val = self.first_optimal()
        arr = [first_a]

        for i in range(1, upran + 1):
            if i == first_a:
                continue
            h_sum = self.h_poly_chet(i)
            if h_sum <= (first_val + err_limit):
                arr.append(i)
        return arr

    def calc_optimal_coeffs_a(self, opt_val):
        """
        Calculate optimal coefficients a
        :param opt_val: 1st optimal value
        :return: array of [1,a,a^2,...,a^{s-1}]
        """
        s = self.dim_s
        self.a_arr[0] = 1
        self.a_arr[1] = opt_val
        for i in range(2, s):
            self.a_arr[i] = (self.a_arr[i-1]*opt_val) % self.p_prime
        return self.a_arr.astype(int)

    def get_opt_coeffs(self):
        return self.a_arr

    def h_for_coeffs(self, o):
        if len(o) != self.dim_s:
            raise ValueError('Array dimension must be equal to s!')
        s = self.dim_s
        p = self.p_prime
        upperb = int((p - 1)/2)
        sm_k = 0
        for k in range(1, upperb + 1):
            k_term = 1.
            for l in range(s):
                ent = fraction(k*o[l] / p)
                k_term = k_term*(1. - ent - ent)
            sm_k = sm_k + k_term*k_term
        return pow(3, s)/p*(1. + 2*sm_k)

    def show_parameters(self):
        print('Object class            :', self.__class__.__name__)
        print('dimension of integration:', self.dim_s)
        print('dimension of result     :', self.dim_r)
        print('number of nodes         :', self.n_nodes)
        print('p - prime               :', self.p_prime)
        print('q - prime               :', self.q_prime)
        print('N = p.q                 :', self.p_prime*self.q_prime)
