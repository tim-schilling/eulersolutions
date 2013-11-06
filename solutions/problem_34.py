__author__ = 'schillingt'
import time
from itertools import product


def get_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number /= 10
    return digits


def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)


def find_curious_digit_factorial_sums():
    # the zero digit was giving me wrong answers for the factorials. Had to insert a hack
    factorials = [(0, 0)] + [(i, factorial(i)) for i in range(1, 10)]
    curious_numbers = []
    attempted_combinations = factorials[:]
    for j in range(0, 6):
        attempted_combinations = [
            (tup1[0]*10+tup2[0], tup1[1]+tup2[1]) for tup1, tup2 in product(attempted_combinations, factorials)]
    # Handle the hack for the 0's
    for number, value in attempted_combinations:
        for digit in get_digits(number):
            if digit == 0:
                value += 1
        attempted_combinations[number] = (number, value)
        # Check if the number is equal to its digits factorials summation
        if number == value and number > 2:
            curious_numbers.append(number)
    return curious_numbers


def get_digits_factorials(number):
    return sum(factorial(x) for x in get_digits(number))


t0 = time.time()
print sum(find_curious_digit_factorial_sums())
t1 = time.time()
print t1-t0
