__author__ = 'schillingt'
import time
from operator import itemgetter


def get_all_decimal_digits(denominator):
    numerator = 1
    remainders = []
    remainder = 1
    while len(remainders) < 50 and remainder > 0:
        remainder = numerator % denominator
        if remainder > 0:
            remainders.append(remainder)
        numerator = remainder * 10
    return remainders


def get_reoccuring_cycle_for_fraction(denominator):
    # Ended up getting some help on the algorithm for this answer.
    for t in range(1, denominator):
        if 1 == 10**t % denominator:
            return t
    return 0


def get_largest_reoccuring_cycle(lower_limit, upper_limit, step):
    cycles = []
    for value in range(lower_limit, upper_limit, step):
        if value % 5 == 0:
            continue
        cycle = get_reoccuring_cycle_for_fraction(value)
        if cycle:
            cycles.append((cycle, value))
    return sorted(cycles, key=itemgetter(0), reverse=True)

t0 = time.time()
print get_largest_reoccuring_cycle(3, 1000, 2)
t1 = time.time()
print t1-t0