from math import sqrt

def is_prime(n):
    if n in (2, 3, 5, 7, 11):  # special case small primes
        return True
    if n % 2 == 0 or n == 1:  # special case even numbers and 1
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
	

from itertools import count

if __name__ == "__main__":
    num = int(input())
    next_prime = next(filter(is_prime, count(num)))
    print(next_prime)	