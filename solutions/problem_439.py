__author__ = 'schillingt'
import time
import itertools


def get_divisors(number):
    return [value for value in range(1, number+1) if number % value == 0]


def get_s(n, upper_bound):
    s = 0
    for i, j in itertools.product(range(1, n+1), range(1, n+1)):
        s += sum(get_divisors(i*j))
        if s > upper_bound:
            s = s % upper_bound
    return s


t0 = time.time()
print get_s(10**11, 10**9)
t1 = time.time()
print t1-t0