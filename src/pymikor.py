import math
import numpy as np
from itertools import count
import warnings


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
        self.a_opt = 0
        self.a_opt_value = 0
        self.b_opt = 0
        self.b_opt_value = 0
        self.a_arr = np.empty(self.dim_s)
        self.b_arr = np.empty(self.dim_s)
        self.c_arr = np.empty(self.dim_s)

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

    def set_values(self, dims, nodes, strategy=1, sec_nodes=1):
        """
        :param dims: Dimension of integral
        :param nodes: Number of nodes N1
        :param strategy: Set variant of integration
                          1 - predefined coefficients
                          2 - N = p
                          3 - N = p.q
        :param sec_nodes: Number of nodes N2
        :return:
        """
        self.empty_arrays(dims)
        self.p_prime = n_prime(nodes)
        self.strategy = strategy

        if self.strategy == 1:
            self.choose_pq()
        if self.strategy == 2 and sec_nodes > 1:
            self.q_prime = 1
        if self.strategy == 3 and sec_nodes == 1:
            self.p_prime = n_prime(int(pow(nodes, 2/3)))
            self.q_prime = n_prime(int(pow(nodes, 1/3)))
        if self.strategy == 3 and sec_nodes > 1:
            self.q_prime = n_prime(sec_nodes)

        self.n_nodes = self.p_prime*self.q_prime

        assert (self.dim_s < self.n_nodes), 'Integral dimension s must be < N nodes!'
        if strategy == 2 and nodes >= 10000:
            warnings.warn('Slow computation, number of nodes too large.')

    def choose_pq(self):
        self.p_prime = 13
        self.q_prime = 11
        self.n_nodes = self.p_prime*self.q_prime

    def set_dpq(self, dims, p, q):
        self.empty_arrays(dims)
        self.p_prime = n_prime(p)
        if q == 1:
            self.strategy = 2
        else:
            self.strategy = 3
            self.q_prime = n_prime(q)
        self.n_nodes = p*q

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

    def first_optimal_a(self):
        """
        Find first optimal value z = a
        :return: tuple of (a value, H(a) value)
        """
        upran = int((self.p_prime - 1)/2)
        optimal_a = 0
        optimal_val = 1e+18

        for i in range(1, upran + 1):
            h_sum = self.h_poly_chet(i)
            if h_sum < optimal_val:
                optimal_a = i
                optimal_val = h_sum
            # if i % 1000 == 0:
            #    print(f'{i}. iteration')
        return optimal_a, optimal_val

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

    def first_optimal_b(self):
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
            # if i % 1000 == 0:
            #    print(f'{i}. iteration')
        return optimal_b, optimal_val

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
        # res_arr = self.a_arr
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
        return self.a_arr.astype(int)

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
        return self.b_arr.astype(int)

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
        Provides optimal coefficients based on strategy
        :return: array of [1,c,c^2,...,c^{s-1}]
        """
        res_arr = self.a_arr
        if self.strategy == 1:
            for i in range(len(self.a_arr)):
                res_arr[i] = 11
        else:
            self.a_opt, self.a_opt_value = self.first_optimal_a()
            self.calc_optimal_coefficients_a(self.a_opt)
            if self.strategy == 2:
                res_arr = self.a_arr
            if self.strategy == 3:
                self.b_opt, self.b_opt_value = self.first_optimal_b()
                self.calc_optimal_coefficients_b(self.b_opt)
                self.calc_optimal_coefficients_c()
                res_arr = self.c_arr
        return res_arr.astype(int)

    def show_parameters(self):
        print('Object class            :', self.__class__.__name__)
        print('dimension of integration:', self.dim_s)
        print('dimension of result     :', self.dim_r)
        print('p - prime               :', self.p_prime)
        print('q - prime               :', self.q_prime)
        print('number of nodes         :', self.n_nodes)
        print('strategy                :', self.strategy)

    def __call__(self, m_fnc, **kwargs):
        for k in kwargs:
            if k == 'strategy':
                print(f'strategy = {kwargs[k]}')
            elif k == 'name':
                print(' '*2 + f'{kwargs[k]}')
            else:
                raise AttributeError(f'no attribute named {k}')

        if self.dim_s == 2:
            m_a_arr = self.calc_fibonacci()
        else:
            m_a_arr = self.optimal_coefficients()
            print(len(m_a_arr))
        fpa = np.empty(self.dim_s)
        sm_f = 0
        for i in range(1, self.n_nodes + 1):
            for j in range(self.dim_s):
                fpa[j] = fraction(m_a_arr[j]*i/self.n_nodes)
            sm_f += m_fnc(fpa)
        return sm_f/self.n_nodes
