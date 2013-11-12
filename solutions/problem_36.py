import time


def get_digits(number):
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number /= 10
    return digits


def is_palindrome(elements):
    if elements[0] == 0 or elements[0] == "0":
        print elements
    elements_length = len(elements)
    halfway = elements_length/2
    for i in range(0, halfway):
        if elements[i] != elements[elements_length-i-1]:
            return False
    return True


def is_binary_palindrome(number):
    return is_palindrome(bin(number)[2:])


def is_decimal_palindrome(number):
    return is_palindrome(get_digits(number))


def get_all_palindromes(upper_bound):
    return sum(x for x in range(0, upper_bound) if is_decimal_palindrome(x) and is_binary_palindrome(x))


t0 = time.time()
print get_all_palindromes(1000000)
t1 = time.time()
print t1-t0
