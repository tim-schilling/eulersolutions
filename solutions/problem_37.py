import time


def get_digits(number):
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number /= 10
    return digits


def condense_list_to_number(digits):
    value = 0
    for digit in digits:
        value = value*10 + digit
    return value


def check_if_prime(value):
    if value == 2 or value == 5:
        return True
    if value % 2 == 0 or value % 5 == 0 or value == 1:
        return False
    for i in range(3, value, 2):
        if value % i == 0:
            return False
    return True


def is_prime_truncating_front_digits(number):
    test_string = str(number)
    test_values = [test_string]
    test_string = test_string[1:]
    while len(test_string) > 0:
        if not check_if_prime(int(test_string)):
            return False
        test_values.append(test_string)
        test_string = test_string[1:]
    return True


def is_prime_truncating_end_digits(number):
    test_string = str(number)
    test_values = [test_string]
    test_string = test_string[:-1]
    while len(test_string) > 0:
        if not check_if_prime(int(test_string)):
            return False
        test_values.append(test_string)
        test_string = test_string[:-1]
    return True


def get_truncatable_primes():
    primes = [2, 3, 5, 7]
    new_primes = []
    truncatable_primes = []
    counter = 0
    while len(primes) > 0:
        print "%s - %s - %s" % (counter, primes, truncatable_primes)
        for prime in primes:
            for digit in range(3, 10, 2):
                test_value = prime*10 + digit
                if check_if_prime(test_value):
                    if is_prime_truncating_end_digits(test_value) and is_prime_truncating_front_digits(test_value):
                        truncatable_primes.append(test_value)
                    new_primes.append(test_value)
        if len(new_primes) == 0 or len(truncatable_primes) >= 11:
            return truncatable_primes
        primes = new_primes
        new_primes = []
        counter += 1

t0 = time.time()
print sum(get_truncatable_primes())
t1 = time.time()
print t1-t0
