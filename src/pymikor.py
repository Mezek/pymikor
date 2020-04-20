# Created by Erik Bartoš in 2019.
# Copyright © 2019 Erik Bartoš <erik.bartos@gmail.com>
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

import math
import numpy as np
import scipy.special
import warnings
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


def egcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, y = egcd(a, b)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % b


class Mikor:

    def __init__(self):
        self.strategy = 1
        self.dim_s = 1
        self.dim_r = 1
        self.n_nodes = n_prime(1000)
        self.p_prime = self.n_nodes
        self.q_prime = 1
        self.sigma = 2
        self.req_eps = 1e-5
        self.eps_flag = False
        self.a_opt = 0
        self.a_opt_value = 0
        self.b_opt = 0
        self.b_opt_value = 0
        self.a_arr = np.empty(self.dim_s)
        self.b_arr = np.empty(self.dim_s)
        self.c_arr = np.empty(self.dim_s)
        self.v_arr = np.empty(self.sigma)

        self.pp = np.array([
            #  3
            [[23, 8], [53, 17], [101, 40], [151, 20], [307, 75], [523, 78],
             [829, 116], [1259, 433], [2129, 937], [3001, 276], [4001, 722],
             [5003, 1476], [6007, 592], [8191, 739], [10007, 544], [13001, 4969],
             [20011, 6880], [30011, 10180], [40009, 16592], [50021, 12962], [75011, 26279],
             [100003, 13758], [200003, 79253], [500009, 33606], [1000003, 342972],
             [2000003, 920849], [5000011, 889866]],
            #  4
            [[23, 5], [53, 12], [101, 15], [151, 22], [307, 42], [523, 178],
             [829, 350], [1259, 550], [2129, 970], [3001, 174], [4001, 956],
             [5003, 2053], [6007, 2610], [8191, 2488], [10007, 1784], [13001, 4796],
             [20011, 6016], [30011, 12084], [40009, 9023], [50021, 23277],
             [75011, 13715], [100003, 12475], [200003, 17914], [500009, 127616],
             [1000003, 33889], [2000003, 317039], [5000011, 1305459]],
            #  5
            [[101, 21], [151, 58], [307, 127], [523, 237], [829, 146], [1259, 302],
             [2129, 720], [3001, 408], [4001, 1534], [5003, 840], [6007, 509],
             [8191, 1386], [10007, 198], [13001, 1864], [20011, 9432], [30011, 13604],
             [40009, 12216], [50021, 7255], [75011, 16449], [100003, 11729],
             [200003, 62638], [500009, 32497], [1000003, 335440], [2000003, 701679],
             [5000011, 1516505]],
            #  6
            [[151, 18], [307, 74], [523, 164], [829, 289], [1259, 200], [2129, 727],
             [3001, 322], [4001, 1780], [5003, 2208], [6007, 312], [8191, 3699],
             [10007, 2399], [13001, 1940], [20011, 6387], [30011, 6645], [40009, 4902],
             [50021, 15683], [75011, 2127], [100003, 6798], [200003, 99038], [500009, 174069],
             [1000003, 127632], [2000003, 752526], [5000011, 60100]],
            #  7
            [[523, 27], [829, 175], [1259, 227], [2129, 718], [3001, 170], [4001, 115],
             [5003, 1573], [6007, 1508], [8191, 2107], [10007, 2304], [13001, 4797],
             [20011, 3851], [30011, 8784], [40009, 14905], [50021, 23981], [75011, 12914],
             [100003, 18083], [200003, 72045], [500009, 75479], [1000003, 119956],
             [2000003, 259724]],
            #  8
            [[829, 32], [1259, 392], [2129, 86], [3001, 955], [4001, 1728], [5003, 2362],
             [6007, 1253], [8191, 2602], [10007, 1905], [13001, 1352], [20011, 7191],
             [30011, 7011], [40009, 9946], [50021, 10899], [75011, 17605], [100003, 15120],
             [200003, 39993], [500009, 42535], [1000003, 230727], [2000003, 832685]],
            #  9
            [[2129, 636], [3001, 108], [4001, 1234], [5003, 526], [6007, 2633],
             [8191, 3052], [10007, 4748], [13001, 3391], [20011, 6181], [30011, 2348],
             [40009, 10979], [50021, 5358], [75011, 10460], [100003, 48635],
             [200003, 2611], [500009, 10374], [1000003, 26697], [2000003, 312566]],
            # 10
            [[5003, 592], [6007, 1262], [8191, 1751], [10007, 1554], [13001, 3466],
             [20011, 6951], [30011, 8883], [40009, 15619], [50021, 9224], [75011, 31958],
             [100003, 833]],
            # 11
            [[8191, 349], [10007, 480], [13001, 5116], [20011, 8978], [30011, 12217],
             [40009, 9873], [50021, 5346], [75011, 11723], [100003, 45273]],
            # 12
            [[10007, 2123], [13001, 6426], [20011, 9832], [30011, 10777], [40009, 15380],
             [50021, 5963], [75011, 14706], [100003, 35982]],
            # 13
            [[13001, 463], [20011, 9721], [30011, 13148], [40009, 5491], [50021, 22854],
             [75011, 28319], [100003, 37813]],
            # 14
            [[20011, 235], [30011, 602], [40009, 19668], [50021, 2711], [75011, 34855],
             [100003, 4329]],
            # 15
            [[30011, 584], [40009, 3054], [50021, 14360], [75011, 6348], [100003, 11971]],
            # 16
            [[40009, 2648], [50021, 1616], [75011, 15486], [1000003, 106257]],
            # 17
            [[50021, 251], [75011, 15424], [1000003, 106245]],
            # 18
            [[75011, 4651], [1000003, 106257]],
            # 19
            [[1000003, 106245]],
            # 20
            [[1000003, 106233]]
            # [30011, 1], [40009, 1], [50021, 1], [75011, 1], [100003, 1], [200003, 1],
            # [500009, 1], [1000003, 1], [2000003, 1], [5000011, 1]]
        ])

        self.qq = np.array([
            #  3
            [[691, 29, 176, 20], [907, 31, 402, 12], [1259, 31, 535, 26], [1543, 37, 355, 14],
             [2129, 47, 937, 45], [3001, 53, 772, 24], [4001, 53, 722, 35], [5003, 61, 1476, 55],
             [6007, 79, 592, 13], [8191, 89, 739, 76], [10007, 101, 544, 94]],
            #  4
            [[691, 29, 132, 19], [907, 31, 376, 10], [1259, 31, 483, 9], [1543, 37, 663, 17],
             [2129, 47, 766, 5], [3001, 53, 1466, 18], [4001, 53, 956, 20], [5003, 61, 2053, 58],
             [6007, 79, 1351, 18], [8191, 89, 3842, 33], [10007, 101, 1206, 12]],
            #  5
            [[907, 31, 53, 4], [1259, 31, 321, 2], [1543, 37, 58, 6], [2129, 47, 618, 39],
             [3001, 53, 890, 40], [4001, 53, 1534, 38], [5003, 61, 840, 22], [6007, 79, 509, 61],
             [8191, 89, 2228, 47], [10007, 101, 1870, 22], [13001, 113, 1864, 3]],
            #  6
            [[1259, 31, 200, 4], [1543, 37, 342, 2], [2129, 47, 727, 37], [3001, 53, 233, 28],
             [4001, 53, 1780, 51], [5003, 61, 2208, 22], [6007, 79, 1521, 70], [8191, 89, 3699, 48],
             [10007, 101, 2240, 31], [13001, 113, 1940, 29], [20011, 139, 6387, 80]],
            #  7
            [[1543, 37, 207, 8], [2129, 47, 718, 30], [3001, 53, 170, 39], [4001, 53, 115, 17],
             [5003, 61, 1573, 2], [6007, 79, 1508, 3], [8191, 89, 2107, 33], [10007, 101, 2304, 57],
             [13001, 113, 4797, 3], [20011, 139, 4791, 92], [30011, 173, 8784, 130]],
            #  8
            [[2129, 47, 86, 20], [3001, 53, 955, 15], [4001, 53, 1728, 2], [5003, 61, 2362, 47],
             [6007, 79, 1253, 72], [8191, 89, 2602, 78], [10007, 101, 1905, 87], [13001, 113, 1352, 107],
             [20011, 139, 7191, 105], [30011, 173, 7011, 10], [40009, 199, 9946, 24]],
            #  9
            [[2129, 47, 636, 17], [3001, 53, 108, 26], [4001, 53, 1234, 27], [5003, 61, 526, 24],
             [6007, 79, 2633, 6], [8191, 89, 3052, 83], [10007, 101, 4748, 69], [13001, 113, 3391, 85],
             [20011, 139, 6181, 136], [30011, 173, 2348, 45], [40009, 199, 10979, 13]],
            # 10
            [[3001, 53, 855, 9], [4001, 53, 1828, 3], [5003, 61, 592, 11], [6007, 79, 1262, 27],
             [8191, 89, 1751, 44], [10007, 101, 1554, 78], [13001, 113, 3466, 67], [20011, 139, 6951, 4],
             [30011, 173, 8883, 78], [40009, 199, 15619, 159]],
            # 11
            [[4001, 53, 1887, 6], [5003, 61, 1485, 41], [6007, 79, 1298, 16], [8191, 89, 349, 78],
             [10007, 101, 480, 56], [13001, 113, 5116, 10], [20011, 139, 8978, 93],
             [30011, 173, 12217, 129], [40009, 199, 9873, 151], [50021, 223, 5346, 79]],
            # 12
            [[5003, 61, 1494, 58], [6007, 79, 2991, 63], [8191, 89, 3147, 77], [10007, 101, 2123, 57],
             [13001, 113, 6426, 59], [20011, 139, 9832, 124], [30011, 173, 10777, 150],
             [40009, 199, 15380, 4], [50021, 223, 5963, 213]],
            # 13
            [[6007, 79, 1330, 58], [8191, 89, 2, 61], [10007, 101, 684, 90], [13001, 113, 463, 8],
             [20011, 139, 9721, 13], [30011, 173, 13148, 85], [40009, 199, 5491, 105],
             [50021, 223, 22854, 161]],
            # 14
            [[8191, 89, 2, 75], [10007, 101, 684, 19], [13001, 113, 1862, 64], [20011, 139, 235, 80],
             [30011, 173, 602, 34], [40009, 199, 19668, 48], [50021, 223, 2711, 96]],
            # 15
            [[10007, 101, 1447, 53], [13001, 113, 155, 23], [20011, 139, 3043, 101],
             [30011, 173, 584, 29], [40009, 199, 3054, 72], [50021, 223, 14360, 58]],
            # 16
            [[13001, 113, 6500, 12], [20011, 139, 2964, 31], [30011, 173, 5738, 163],
             [40009, 199, 2648, 116], [50021, 223, 1616, 135]],
            # 17
            [[20011, 139, 1249, 9], [30011, 173, 722, 22], [40009, 199, 2648, 145],
             [50021, 223, 251, 174]],
            # 18
            [[30011, 173, 7653, 38], [40009, 199, 2648, 111], [50021, 223, 8080, 74]],
            # 19
            [[40009, 199, 2, 174], [50021, 223, 251, 202]],
            # 20
            [[50021, 223, 2, 131]]
        ])

    def __del__(self):
        # print(f'Object {self.__class__.__name__} deleted')
        print('\n')

    def empty_arrays(self, dimension):
        self.dim_s = dimension
        self.a_arr = np.empty(self.dim_s)
        self.b_arr = np.empty(self.dim_s)
        self.c_arr = np.empty(self.dim_s)

    def set_values(self, strategy, dimension, nodes=1009, sec_nodes=1, **kwargs):
        """
        :param strategy: Set variant of integration
                          1 - automatic predefined p
                          2 - automatic predefined p, q
                          3 - N = p
                          4 - N = p.q
        :param dimension: Dimension of integral
        :param nodes: Number of nodes N1
        :param sec_nodes: Number of nodes N2
        :return:
        """
        self.strategy = strategy
        self.empty_arrays(dimension)
        self.p_prime = n_prime(nodes)

        assert (self.dim_s >= 2), 'Integral dimension s must be >= 2!'
        if self.dim_s == 2:
            assert (self.strategy == 3), 'For dimension=2 only strategy=3 is available!'

        # Setting of p, q for strategy
        assert (self.strategy <= 4), 'Too high strategy!'
        assert (self.strategy > 0), 'Unknown strategy for the integration!'
        if self.strategy == 1:
            self.choose_p(0)
        if self.strategy == 2:
            self.choose_pq(0)
        if self.strategy == 3:
            self.q_prime = 1
        if self.strategy == 4 and sec_nodes == 1:
            self.p_prime = n_prime(int(pow(nodes, 2/3)))
            self.q_prime = n_prime(int(pow(nodes, 1/3)))
        if self.strategy == 4 and sec_nodes > 1:
            self.q_prime = n_prime(sec_nodes)
        self.n_nodes = self.p_prime*self.q_prime

        # Warnings for strategy 3 or 4
        if strategy == 3 and nodes >= 10000:
            warnings.warn('Slow computation, number of nodes too large.')

        assert (self.dim_s < self.n_nodes), 'Integral dimension s must be < N nodes!'

        for k in kwargs:
            if k == 'sigma':
                self.sigma = kwargs[k]
                if self.sigma < 1:
                    raise AttributeError(f'{k} must be greater then {self.sigma}')
                self.v_arr = np.empty(self.sigma)
            elif k == 'eps':
                self.req_eps = kwargs[k]
                self.eps_flag = True
            else:
                raise AttributeError(f'no attribute named {k}')

    def show_parameters(self):
        print(f'\nObject class            : {self.__class__.__name__}')
        print(f'dimension of integration: {self.dim_s}')
        print(f'dimension of result     : {self.dim_r}')
        print(f'p - prime               : {self.p_prime}')
        print(f'q - prime               : {self.q_prime}')
        print(f'number of nodes         : {self.n_nodes}')
        print(f'sigma                   : {self.sigma}')
        print(f'relative eps            : {self.req_eps}  flag: {self.eps_flag}')
        print(f'strategy                : {self.strategy}')

    def choose_p(self, i):
        """ Choose p value from array """
        dim = self.dim_s - 3
        self.p_prime = self.pp[dim][i][0]
        self.q_prime = 1
        self.a_opt = self.pp[dim][i][1]
        self.b_opt = 0

    def choose_pq(self, i):
        """ Choose p, q values from arrays """
        dim = self.dim_s - 3
        self.p_prime = self.qq[dim][i][0]
        self.q_prime = self.qq[dim][i][1]
        self.a_opt = self.qq[dim][i][2]
        self.b_opt = self.qq[dim][i][3]

    def set_dpq(self, dimension, p, q):
        self.empty_arrays(dimension)
        self.p_prime = n_prime(p)
        if q == 1:
            self.strategy = 3
        else:
            self.strategy = 4
            self.q_prime = n_prime(q)
        self.n_nodes = p*q

    def set_pa(self, pa):
        self.p_prime = n_prime(pa[0])
        self.n_nodes = self.p_prime
        self.a_opt = pa[1]

    def set_eps(self, eps):
        self.req_eps = eps
        self.eps_flag = True

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
            for ls in range(s):
                ent = fraction(k*a[ls])
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

    def h_for_coefficients(self, aopt):
        """
        Summation in H(z) fuction for a coefficients
        :param aopt: array of parameters
        :return: sum k = 1,2,...,N=p.q
        """
        if len(aopt) != self.dim_s:
            raise ValueError('Array dimension must be equal to s!')
        s = self.dim_s
        p = self.p_prime
        upperb = int((p - 1)/2)
        sm_k = 0
        for k in range(1, upperb + 1):
            k_term = 1.
            for ls in range(s):
                ent = fraction(k*aopt[ls] / p)
                k_term = k_term*(1. - ent - ent)
            sm_k = sm_k + k_term*k_term
        return pow(3, s)/p*(1. + 2*sm_k)

    def first_optimal_a(self, prt=0):
        """
        Find first optimal value z = a

        :param prt: 0 - no print, 1 - print iteration progress
        :return: tuple of (a value, H(a) value)
        """
        up_ran = int((self.p_prime - 1)/2)
        optimal_a = 0
        optimal_val = 1e+18

        for i in range(1, up_ran + 1):
            h_sum = self.h_poly_chet(i)
            if h_sum < optimal_val:
                optimal_a = i
                optimal_val = h_sum
            if prt != 0 and i % 1000 == 0:
                print(f'{i}. iteration')
        self.a_opt = optimal_a
        self.a_opt_value = optimal_val
        return optimal_a, optimal_val

    def first_optimal_a_candidates(self, eps):
        """
        Find first optimal values z = a
        :return:
        """
        up_ran = self.p_prime
        optimal_a = 0
        optimal_val = 1e+18
        flag_o = False
        cand = []

        for i in range(1, up_ran + 1):
            h_sum = self.h_poly(i)
            # print(i, h_sum)
            if abs(h_sum - optimal_val) < eps:
                # print(f'{optimal_a}, {i}: {h_sum}')
                if flag_o is False:
                    cand.append([optimal_a, optimal_val])
                    flag_o = True
                cand.append([i, h_sum])
            if h_sum < optimal_val:
                optimal_a = i
                optimal_val = h_sum
        return optimal_a, optimal_val, cand

    def h_tilde_sum(self, upperb, z, a_arg):
        """
        Summation in h(z) function without coefficient
        :param upperb: upper bound of summation
        :param z: polynomial parameter
        :param a_arg: array a_arr calculated before
        :return: sum in h(z) function
        """
        s = self.dim_s
        p = self.p_prime
        q = self.q_prime
        b = np.ones(s)
        sm_k = 0
        zs = 1
        for j in range(s):
            b[j] = zs / q + a_arg[j] / p
            zs = (zs*z) % q
        for k in range(1, upperb + 1):
            k_term = 1.
            for ls in range(s):
                ent = fraction(k*b[ls])
                k_term = k_term*(1. - ent - ent)
            sm_k = sm_k + k_term*k_term
        return sm_k

    def h_tilde_poly(self, z):
        """
        Equation (207) in Korobov's book
        :param z: polynomial parameter
        :return: sum k = 1,2,...,N=p.q
        """
        nn = self.n_nodes
        return pow(3, self.dim_s) / nn * self.h_tilde_sum(nn, z, self.a_arr)

    def find_optimal_b(self):
        """
        Find first optimal value z = b
        :return: tuple of (b value, H(b) value)
        """
        q = self.q_prime
        # upran = int((q - 1)/2)
        optimal_b = 0
        optimal_val = 1e+28

        for i in range(1, q):
            h_sum = self.h_tilde_poly(i)
            # print(i, h_sum)
            if h_sum < optimal_val:
                optimal_b = i
                optimal_val = h_sum
            if i % 10 == 0:
                print(f'{i}. iteration')
        self.b_opt = optimal_b
        self.b_opt_value = optimal_val
        return optimal_b, optimal_val

    def first_optimal_b(self, first_a=None):
        if first_a is None:
            first_a, opt_a_val = self.first_optimal_a(0)
        if first_a < 1 or first_a > self.p_prime:
            warnings.warn('Check first optimal a!')
        self.a_opt = first_a
        self.calc_optimal_coefficients_a(first_a)
        return self.find_optimal_b()

    def more_optimal(self, err_limit):
        """
        Find more optimal values z = a, to check with Saltykov's values
        :param err_limit: error limit
        :return: array of optimal values
        """
        p = self.p_prime
        upran = int((p - 1)/2)
        first_a, first_val = self.first_optimal_a()
        arr = [first_a]

        for i in range(1, upran + 1):
            if i == first_a:
                continue
            h_sum = self.h_poly_chet(i)
            if h_sum <= (first_val + err_limit):
                arr.append(i)
        return arr

    def calc_fibonacci(self):
        """
        Calculate coefficients for s=2
        :return: array of [1, Q_{N-1}]
        """
        a = 1
        b = 1
        while b < self.n_nodes:
            k = a + b
            if k > self.n_nodes:
                break
            a = b
            b = k
        self.n_nodes = b
        return np.array([1, a])

    def calc_optimal_coefficients_a(self, opt_val):
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
        return self.a_arr

    def calc_optimal_coefficients_b(self, opt_val):
        """
        Calculate optimal coefficients b
        :param opt_val: 1st optimal value
        :return: array of [1,b,b^2,...,b^{s-1}]
        """
        s = self.dim_s
        self.b_arr[0] = 1
        self.b_arr[1] = opt_val
        for i in range(2, s):
            self.b_arr[i] = (self.b_arr[i-1]*opt_val) % self.q_prime
        return self.b_arr

    def calc_optimal_coefficients_c(self):
        """
        Calculate optimal coefficients with congruence root
        :return: array of [1,c,c^2,...,c^{s-1}]
        """
        s = self.dim_s
        p = self.p_prime
        q = self.q_prime
        n = p * q
        w = mod_inv(p + q, n)
        for i in range(s):
            m = p*self.b_arr[i] + q*self.a_arr[i]
            self.c_arr[i] = (m * w) % n

    def optimal_coefficients(self):
        """
        Provides optimal coefficients based on strategy and dimension
        :return: array of [1,c,c^2,...,c^{s-1}]
        """
        res_arr = self.a_arr
        if self.dim_s == 2:
            res_arr = self.calc_fibonacci()
        else:
            if self.strategy == 1:
                self.calc_optimal_coefficients_a(self.a_opt)
                res_arr = self.a_arr
            elif self.strategy == 2:
                self.calc_optimal_coefficients_a(self.a_opt)
                self.calc_optimal_coefficients_b(self.b_opt)
                self.calc_optimal_coefficients_c()
                res_arr = self.c_arr
            else:
                self.a_opt, self.a_opt_value = self.first_optimal_a()
                self.calc_optimal_coefficients_a(self.a_opt)
                if self.strategy == 3:
                    res_arr = self.a_arr
                if self.strategy == 4:
                    self.b_opt, self.b_opt_value = self.first_optimal_b(self.a_opt)
                    self.calc_optimal_coefficients_b(self.b_opt)
                    self.calc_optimal_coefficients_c()
                    res_arr = self.c_arr
        return res_arr

    def calc_aux_period_coefficients(self):
        """
        Calculate auxiliary period coefficients
        :return: array of coefficients v_arr
        """
        s_sign = 1
        k1 = self.sigma - 1
        for i in range(self.sigma):
            self.v_arr[i] = scipy.special.binom(k1, i)*s_sign/(i+1 + k1)
            s_sign = -s_sign

    def periodization_fcn(self, x):
        """
        Periodizing of function
        :param x: parameter
        :return: function psi and derivation of psi
        """
        sig = self.sigma
        if sig == 1:
            return x, 1
        psi = 0
        k1 = sig - 1
        t = pow(x, k1)
        cp = (2*sig - 1)*scipy.special.binom(2*sig - 2, sig - 1)
        self.calc_aux_period_coefficients()
        for i in range(sig):
            t = t * x
            psi = psi + self.v_arr[i]*t
        psi = psi * cp
        der_psi = cp*pow(x*(1. - x), k1)
        return psi, der_psi

    def integral_value(self, mi_a_arr, integrand_fcn):
        """
        Calculation of integral with periodization function
        :param mi_a_arr: argument vector
        :param integrand_fcn: integrated function
        :return: value of integral
        """
        trans_x = np.empty(self.dim_s)
        mi_f = 0.
        for i in range(1, self.n_nodes + 1):
            mi_drv = 1.
            for j in range(self.dim_s):
                a_element = mi_a_arr[j]*i/self.n_nodes
                x = fraction(a_element)
                psi, der_psi = self.periodization_fcn(x)
                trans_x[j] = psi
                # print(x, psi, der_psi)
                mi_drv = mi_drv * der_psi
            mi_f += integrand_fcn(trans_x) * mi_drv
        return mi_f/self.n_nodes

    def __call__(self, integrand_fcn, **kwargs):
        for k in kwargs:
            if k == 'strategy':
                print(f'strategy = {kwargs[k]}')
            elif k == 'eps':
                self.set_eps(kwargs[k])
            else:
                raise AttributeError(f'no attribute named {k}')

        integral = self.integral_value(self.optimal_coefficients(), integrand_fcn)

        # TODO: eps with dimension 2

        # TODO: classic eps for strategy 1, 2
        """
        # absolute error
        # TODO: next IF will be checking eps...
        if self.strategy < 3:
            if self.dim_s > 2:
                order = self.dim_s - 3
                act_val = 0.
                eps_val = float('nan')
                for i in self.pp[order]:
                    self.set_pa(i)
                    arg_vector = self.calc_optimal_coefficients_a(i[1])
                    iv = self.integral_value(arg_vector, integrand_fcn)
                    if math.fabs(act_val - iv) <= self.req_eps:
                        eps_val = iv
                        break
                    act_val = iv
                if not math.isnan(eps_val):
                    integral = eps_val
                else:
                    print(f'\nResult: {act_val} has not achieved the required accuracy {self.req_eps}!')
                    print(f'Try to increase current periodization value sigma={self.sigma}.')
            else:
                integral = float('nan')
        else:
            integral = self.integral_value(self.optimal_coefficients(), integrand_fcn)
        """

        return integral
