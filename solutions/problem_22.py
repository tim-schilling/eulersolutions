__author__ = 'schillingt'
import time
import os

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SCORING_DICTIONARY = {}
index = 0
while index < len(ALPHABET):
    # Add one to the index because the scoring starts at 1.
    SCORING_DICTIONARY[ALPHABET[index]] = index + 1
    index += 1


def get_names():
    f = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/problem_22/names.txt"))
    raw_string = "".join(f.readlines())
    f.close()
    return raw_string.replace('"', '').split(',')


def score_name(name, rank):
    return sum([SCORING_DICTIONARY[char] for char in name]) * rank


def sum_scores_of_all_names():
    names = get_names()
    names.sort()
    summation = 0
    i = 0
    while i < len(names):
        # Add one to the index because the scoring starts at 1.
        summation += score_name(names[i], i+1)
        i += 1
    return summation

t0 = time.time()
print sum_scores_of_all_names()
t1 = time.time()
print t1-t0