__author__ = 'schillingt'
import time


def get_divisors(number):
    return [value for value in range(1, number) if number % value == 0]


def categorize_number(deficient, perfect, abundant, number):
    sum_of_proper_divisors = sum(get_divisors(number))
    if sum_of_proper_divisors == number:
        perfect.append(number)
    elif sum_of_proper_divisors > number:
        abundant.append(number)
    elif sum_of_proper_divisors < number:
        deficient.append(number)


def find_positive_integers_that_cant_be_written_as_sum_of_two_abundant_numbers(upper_limit):
    deficient, perfect, abundant = [], [], []
    for number in range(1, upper_limit):
        categorize_number(deficient, perfect, abundant, number)
    print "categorized"
    sums_of_two_abundant_numbers = [
        number+other_number for number in abundant for other_number in abundant
    ]
    print "summed"
    return [number for number in range(1, upper_limit) if number not in sums_of_two_abundant_numbers]

t0 = time.time()
print sum(find_positive_integers_that_cant_be_written_as_sum_of_two_abundant_numbers(28124))
t1 = time.time()
print t1-t0