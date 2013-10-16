def factorial(x):
     if x == 0:
         return 1
     return x * factorial(x-1)

def sum_digits(value):
    sum = 0
    while value > 10:
        sum += value % 10
        value = long(value / 10)
    sum += value
    return sum

digits = factorial(100)
print sum_digits(digits)