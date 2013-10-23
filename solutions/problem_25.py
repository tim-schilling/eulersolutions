__author__ = 'schillingt'
import time
import itertools


def get_next_fibonacci(n_term, n_minus_1_term):
    return n_term + n_minus_1_term


def get_index_of_first_term_to_contain_digits(number_of_digits=1):
    index = 1
    n_term = 1
    n_minus_1_term = 0
    if number_of_digits == 1:
        return index
    limit = 10**(number_of_digits-1)
    next_term = get_next_fibonacci(n_term, n_minus_1_term)
    while next_term < limit:
        n_minus_1_term = n_term
        n_term = next_term
        next_term = get_next_fibonacci(n_term, n_minus_1_term)
        index += 1
    return index+1


t0 = time.time()
print get_index_of_first_term_to_contain_digits(1000)
t1 = time.time()
print t1-t0