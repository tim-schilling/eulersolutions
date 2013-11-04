__author__ = 'schillingt'
import time
from fractions import Fraction


def get_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number /= 10
    return digits


def find_all_fractions():
    return [(i, j) for i in range(10, 100) for j in range(10, 100) if i < j]


def is_curious(fraction):
    num_digits = get_digits(fraction[0])
    den_digits = get_digits(fraction[1])
    return (
        0 not in num_digits and 0 not in den_digits and (
            (num_digits[0] == den_digits[1] and float(num_digits[1])/den_digits[0] == float(fraction[0])/fraction[1])
            or (num_digits[1] == den_digits[0] and float(num_digits[0])/den_digits[1] == float(fraction[0])/fraction[1])
        )
    )


def get_curious_fractions():
    return [fraction for fraction in find_all_fractions() if is_curious(fraction)]


def get_product_of_fractions(fractions):
    numerator_product = 1
    denominator_product = 1
    for numerator, denominator in fractions:
        numerator_product *= numerator
        denominator_product *= denominator
    return Fraction(numerator_product, denominator_product).denominator

t0 = time.time()
print get_product_of_fractions(get_curious_fractions())
t1 = time.time()
print t1-t0
