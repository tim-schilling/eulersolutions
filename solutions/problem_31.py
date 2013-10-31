__author__ = 'schillingt'
import time

COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def get_coin_possibilities(value, coins, variants):
    if value <= 0:
        return
    index = 1
    for coin in coins:
        if value >= coin:
            if coin != 1:
                for number in range(1, int(value/coin)+1):
                    test_value = number*coin
                    if value == test_value:
                        # If the value of the number and coin together is the value, it'll just be itself.
                        variants.append([(coin, number)])
                    else:
                        new_variants = []
                        get_coin_possibilities(value - test_value, coins[index:], new_variants)
                        for l in new_variants:
                            l.append((coin, number))
                            variants.append(l)
            else:
                variants.append([(1, value)])
        index += 1


t0 = time.time()
v = []
get_coin_possibilities(200, COINS, v)
print len(v)
t1 = time.time()
print t1-t0