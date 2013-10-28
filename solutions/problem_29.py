__author__ = 'schillingt'
import time


def get_all_powers(base, lower_bound, max_power, target):
    target.append(base ** max_power)
    if max_power > lower_bound:
        get_all_powers(base, lower_bound, max_power-1, target)


def get_all_integer_combinations(upper_bound):
    target = []
    lower_bound = 2
    for a in range(lower_bound, upper_bound):
        get_all_powers(a, lower_bound, upper_bound-1, target)
    target = list(set(target))
    return target

t0 = time.time()
print len(get_all_integer_combinations(101))
t1 = time.time()
print t1-t0