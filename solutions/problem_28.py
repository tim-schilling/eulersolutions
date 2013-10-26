__author__ = 'schillingt'
__author__ = 'schillingt'
import time
from operator import itemgetter


def get_level_sum(level):
    if level == 1:
        return 1
    count_increase = (level * 2) - 1
    square = count_increase**2
    count_increase -= 1
    return sum([square - (count_increase * i) for i in range(1, 4)] + [square])


def get_spiral_diagonal_sum(rows):
    levels = (rows+1)/2 + 1
    return sum([get_level_sum(i) for i in range(1, levels)])


t0 = time.time()
print get_spiral_diagonal_sum(1001)
t1 = time.time()
print t1-t0