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
            [[23, 3], [53, 25], [101, 40], [151, 20], [307, 75], [523, 78],
             [829, 116], [1259, 535], [2129, 937], [3001, 772], [4001, 722],
             [5003, 1476], [6007, 592], [8191, 739], [10007, 544], [13001, 2135],
             [20011, 6880], [30011, 10180], [40009, 16592], [50021, 12962], [75011, 26279],
             [100003, 13758], [200003, 79253], [500009, 33606], [1000003, 342972]],
            #  4
            [[23, 5], [53, 12], [101, 15], [151, 22], [307, 95], [523, 238],
             [829, 45], [1259, 483], [2129, 766], [3001, 1466], [4001, 956],
             [5003, 2053], [6007, 1351], [8191, 3842], [10007, 1206], [13001, 778],
             [20011, 2891], [30011, 12084], [40009, 9023], [50021, 23277],
             [75011, 13715], [100003, 12475]],
            #  5
            [[101, 21], [151, 58], [307, 29], [523, 64], [829, 146], [1259, 321],
             [2129, 618], [3001, 890], [4001, 1534], [5003, 840], [6007, 509],
             [8191, 2228], [10007, 1870], [13001, 1864], [20011, 9432], [30011, 13604],
             [40009, 13130], [50021, 7255], [75011, 16449], [100003, 48778]],
            #  6
            [[151, 18], [307, 122], [523, 118], [829, 109], [1259, 200], [2129, 727],
             [3001, 233], [4001, 1780], [5003, 2208], [6007, 1521], [8191, 3699],
             [10007, 2240], [13001, 1940], [20011, 6387], [30011, 6645], [40009, 19727],
             [50021, 15683], [75011, 2127], [100003, 6798]],
            #  7
            [[523, 27], [829, 175], [1259, 227], [2129, 718], [3001, 170], [4001, 115],
             [5003, 1573], [6007, 1508], [8191, 2107], [10007, 2304], [13001, 4797],
             [20011, 4791], [30011, 8784], [40009, 12506], [50021, 23981], [75011, 30059],
             [100003, 30925]],
            #  8
            [[829, 32], [1259, 392], [2129, 86], [3001, 955], [4001, 1728], [5003, 2362],
             [6007, 1253], [8191, 2602], [10007, 1905], [13001, 1352], [20011, 7191],
             [30011, 7011], [40009, 9946], [50021, 10899], [75011, 17605], [100003, 15120]],
            #  9
            [[2129, 636], [3001, 108], [4001, 1234], [5003, 526], [6007, 2633],
             [8191, 3052], [10007, 4748], [13001, 3391], [20011, 6181], [30011, 2348],
             [40009, 10979], [50021, 5358], [75011, 10460], [100003, 48635]],
            # 10
            [[5003, 592], [6007, 1262], [8191, 1751], [10007, 1554], [13001, 3466],
             [20011, 6951], [30011, 8883], [40009, 15619], [50021, 9224], [75011, 31958],
             [100003, 833]],
            # 11
            [[8191, 349], [10007, 480], [13001, 5116], [20011, 8978], [30011, 12217],
             [40009, 9873], [50021, 5346], [75011, 11723], [100003, 45273]],
            # 12
            [[20011, 9832], [30011, 10777], [40009, 15380], [50021, 5963], [75011, 14706],
             [100003, 1]],
            # 13
            [[50021, 22854], [75011, 1], [100003, 1]],
            # 14
            [[50021, 2711], [75011, 1], [100003, 1]],
            # 15
            [[50021, 14360], [75011, 1], [100003, 1]],
            # 16
            [[1000003, 106257]],
            # 17
            [[1000003, 106245]],
            # 18
            [[1000003, 106257]],
            # 19
            [[1000003, 106245]],
            # 20
            [[1000003, 106233]]
            #  x
            # [[151, 1], [307, 1], [523, 1], [829, 1], [1259, 1], [2129, 1], [3001, 1],
            # [4001, 1], [5003, 1], [6007, 1], [8191, 1], [10007, 1], [13001, 1], [20011, 1],
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
            #  x
            # [6007, 79] [8191, 89] [10007, 101]
        ])

    def __del__(self):
        # print(f'Object {self.__class__.__name__} deleted')
        print('\n')

    def empty_arrays(self, dims):
        self.dim_s = dims
        self.a_arr = np.empty(self.dim_s)
        self.b_arr = np.empty(self.dim_s)
        self.c_arr = np.empty(self.dim_s)

    def check_numbers(self):
        if self.n_nodes <= self.dim_s:
            raise ValueError('Integral dimension s must be < N nodes!')

    def set_values(self, strategy, dims, nodes=1009, sec_nodes=1, **kwargs):
        """
        :param strategy: Set variant of integration
                          1 - automatic predefined p
                          2 - automatic predefined p, q
                          3 - N = p
                          4 - N = p.q
        :param dims: Dimension of integral
        :param nodes: Number of nodes N1
        :param sec_nodes: Number of nodes N2
        :return:
        """
        self.empty_arrays(dims)
        self.p_prime = n_prime(nodes)
        self.strategy = strategy

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

        # TODO: choose p,q for strategy==1 & 2
        if self.strategy == 1:
            self.choose_p(0)
        if self.strategy == 2:
            self.choose_pq()
        if self.strategy == 3 and sec_nodes > 1:
            self.q_prime = 1
        if self.strategy == 4 and sec_nodes == 1:
            self.p_prime = n_prime(int(pow(nodes, 2/3)))
            self.q_prime = n_prime(int(pow(nodes, 1/3)))
        if self.strategy == 4 and sec_nodes > 1:
            self.q_prime = n_prime(sec_nodes)

        self.n_nodes = self.p_prime*self.q_prime

        assert (self.dim_s < self.n_nodes), 'Integral dimension s must be < N nodes!'
        if strategy == 2 and nodes >= 10000:
            warnings.warn('Slow computation, number of nodes too large.')

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
        self.p_prime = self.pp[0][i][0]
        self.a_opt = self.pp[0][i][1]
        self.q_prime = 1
        self.n_nodes = self.p_prime

    def choose_pq(self):
        qq = np.array([23, 53, 101, 151, 307, 523, 829, 1259, 2129, 3001, 4001, 5003,
                       6007, 8191, 10007, 13001, 20011, 30011, 40009, 50021, 75011,
                       100003, 200003, 500009, 1000003, 2000003, 5000011])
        self.p_prime = 13
        self.q_prime = 1
        self.n_nodes = self.p_prime*self.q_prime

    def set_dpq(self, dims, p, q):
        self.empty_arrays(dims)
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
            for l in range(s):
                ent = fraction(k*aopt[l] / p)
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

    def h_tilde_sum(self, upperb, z):
        """
        Summation in h(z) function without coefficient
        Must calculate array a_arr before!
        :param upperb: upper bound of summation
        :param z: polynomial parameter
        :return: sum in h(z) function
        """
        s = self.dim_s
        p = self.p_prime
        q = self.q_prime
        b = np.ones(s)
        sm_k = 0
        zs = 1
        for j in range(s):
            b[j] = zs / q + self.a_arr[j] / p
            zs = (zs*z) % q
        for k in range(1, upperb + 1):
            k_term = 1.
            for l in range(s):
                ent = fraction(k*b[l])
                k_term = k_term*(1. - ent - ent)
            sm_k = sm_k + k_term*k_term
        return sm_k

    def h_tilde_poly(self, z):
        """
        Equation (207) in Korobov's book
        :param z: polynomial parameter
        :return: sum k = 1,2,...,N=p.q
        """
        nn = self.p_prime*self.q_prime
        return pow(3, self.dim_s) / nn * self.h_tilde_sum(nn, z)

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
        Provides optimal coefficients based on strategy and defined eps
        :return: array of [1,c,c^2,...,c^{s-1}]
        """
        res_arr = self.a_arr
        if self.dim_s == 2:
            res_arr = self.calc_fibonacci()
        else:
            # TODO: check all conditions again
            if self.strategy == 2:
                print('\nUnknown optimal...')
                print(self.a_opt)
                self.calc_optimal_coefficients_a(self.a_opt)
                res_arr = self.a_arr
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

        # absolute error
        integ = float('nan')
        if self.strategy == 1 or self.strategy == 2:
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
                    integ = eps_val
                else:
                    print(f'\nResult: {act_val} has not achieved the required accuracy {self.req_eps}!')
                    print(f'Try to increase current periodization value sigma={self.sigma}.')
            else:
                print('Ooops!')
        else:
            integ = self.integral_value(self.optimal_coefficients(), integrand_fcn)

        return integ
