__author__ = 'schillingt'
import time
import operator

LAST_CHECKED_VALUE = 0
KNOWN_PRIMES = []


def check_if_prime(value):
    if value % 2 == 0 or value % 5 == 0 or value < 3:
        return False
    if value in KNOWN_PRIMES:
        return True
    #if value > LAST_CHECKED_VALUE:
    for i in range(3, value, 2):
        if value % i == 0:
            return False
    KNOWN_PRIMES.append(value)
    return True


def get_consectutive_primes_of_quadratic_formula(a_limits, b_limits):
    results = []
    for a in range(a_limits[0], a_limits[1]):
        for b in range(b_limits[0], b_limits[1]):
            is_prime = True
            n = 0
            while is_prime:
                target = n**2 + a*n + b
                is_prime = check_if_prime(target)
                n += 1
            results.append((n, a, b))
    return results


def get_product_of_best_coefficients_of_quadratic_formula(a_limits, b_limits):
    values = get_consectutive_primes_of_quadratic_formula(a_limits, b_limits)
    best = sorted(values, key=operator.itemgetter(0), reverse=True)
    return best[0][1] * best[0][2]

t0 = time.time()
print get_product_of_best_coefficients_of_quadratic_formula((-999, 1000), (-999, 1000))
t1 = time.time()
print t1-t0