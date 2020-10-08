from math import sqrt
from itertools import count


ULIMIT = 10**5


def is_prime(n):
    # if n in (2, 3, 5, 7, 11):  # special case small primes
    #    return True
    if n % 2 == 0 or n == 1:  # special case even numbers and 1
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    num = ULIMIT
    plist = []
    next_prime = 0
    while next_prime < num:
        if is_prime(next_prime):
            plist.append(next_prime)
        next_prime += 1


def get_primes():
    # num = int(input())
    num = ULIMIT
    plist = []
    next_prime = 0
    while next_prime < num:
        next_prime = next(filter(is_prime, count(next_prime)))
        if next_prime > num:
            break
        plist.append(next_prime)
        next_prime += 1
    return plist


if __name__ == "__main__":
    main()
    primes = get_primes()
    print(primes)
