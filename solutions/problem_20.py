def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x-1)


def sum_digits(value):
    summed_value = 0
    while value > 10:
        summed_value += value % 10
        value = long(value / 10)
    summed_value += value
    return summed_value

digits = factorial(100)
print sum_digits(digits)