__author__ = 'schillingt'
import time
import itertools


t0 = time.time()
print list(itertools.permutations(range(0, 10)))[999999]
t1 = time.time()
print t1-t0