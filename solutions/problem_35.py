__author__ = 'schillingt'
import time


def get_digits(number):
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number /= 10
    return digits


def is_prime(number):
    for value in range(3, number, 2):
        if number % value == 0:
            return False
    return True


def condense_list_to_number(digits):
    value = 0
    for digit in digits:
        value = value*10 + digit
    return value


def is_circular_prime(number):
    digits = get_digits(number)
    if any([x in digits for x in [0, 2, 4, 5, 6, 8]]):
        return False
    for i in range(0, len(digits)):
        digits.insert(0, digits.pop())
        if not is_prime(condense_list_to_number(digits)):
            return False
    return True

t0 = time.time()
primes = [2, 5] + [x for x in range(3, 10**6, 2) if is_circular_prime(x)]
print len(primes)
print primes
t1 = time.time()
print t1-t0
