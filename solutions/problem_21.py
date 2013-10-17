__author__ = 'schillingt'
import time
AMICABLE_NUMBERS = []
SUMMED_DIVISORS = {}


def get_divisors(number):
    return [value for value in range(1, number) if number % value == 0]


def get_potential_amicable_number(number):
    try:
        return SUMMED_DIVISORS[number]
    except KeyError:
        value = sum(get_divisors(number))
        SUMMED_DIVISORS[number] = value
        return value


def check_if_amicable_number(number):
    if number in AMICABLE_NUMBERS:
        return True
    amicable_number = get_potential_amicable_number(number)
    if amicable_number != number and get_potential_amicable_number(amicable_number) == number:
        AMICABLE_NUMBERS.append(number)
        return True
    return False


def get_all_amicable_numbers(upper_bound):
    amicable_numbers = [
        value for value in range(1, upper_bound) if check_if_amicable_number(value)
    ]
    return amicable_numbers


t0 = time.time()
print sum(get_all_amicable_numbers(10000))
t1 = time.time()
print t1-t0