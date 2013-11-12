__author__ = 'schillingt'
import time
from multiprocessing import Pool


def get_divisor_pairs(number):
    return [(value, int(number/value)) for value in range(1, number) if number % value == 0]


def get_digits(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number /= 10
    return digits


def is_pandigital(product):
    digits_used = get_digits(product)
    if 0 in digits_used or len(digits_used) != len(set(digits_used)):
        return False
    for m0, m1 in get_divisor_pairs(product):
        digits = get_digits(m0) + get_digits(m1)
        if 0 in digits:
            continue
        digits = digits_used+digits
        if len(digits) != 9 and len(set(digits)) != 9:
            return True
    return False


def get_all_pandigital_numbers(limits):
    lower_limit, upper_limit = limits
    return [number for number in range(lower_limit, upper_limit, 1) if is_pandigital(number)]


def test2():
    pan_digital_sum = 0
    for i in range(1, 123456790):
        i_digits = get_digits(i)
        if 0 in i_digits:
            continue
        for j in range(1, 123456790):
            product = i*j
            if product > 123456789:
                break
            j_digits = get_digits(j)
            if 0 in j_digits:
                continue
            all_digits = j_digits + i_digits
            if len(all_digits) != len(set(all_digits)):
                continue
            all_digits += get_digits(product)
            if len(all_digits) == 9 and len(set(all_digits)) == 9:
                pan_digital_sum += product


#34445489727
t0 = time.time()

#args = [(i, i+1050000) for i in range(1050000, 100000000, 1050000)]

#p = Pool(5)
#results = p.map(get_all_pandigital_numbers, args)
#s = 34445489727
#for r in results:
#    s += sum(r)
print test2() # s
t1 = time.time()
print t1-t0
