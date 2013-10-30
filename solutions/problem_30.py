__author__ = 'schillingt'
import time


def get_fifth_power_sums(power, max_value):
    number = 2
    sums_of_their_digits = []
    power_sums = [i**power for i in range(0, 10)]
    while number < max_value:
        original_number = number
        digits_sum = 0
        while number > 0:
            digit = number % 10
            digits_sum += power_sums[digit]
            if digits_sum > original_number:
                break
            number /= 10
        if digits_sum == original_number:
            sums_of_their_digits.append(original_number)
        number = original_number + 1
    return sums_of_their_digits

t0 = time.time()
print sum(get_fifth_power_sums(5, 1000000))
t1 = time.time()
print t1-t0