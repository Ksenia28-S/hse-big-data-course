#!/usr/bin/env python

import sys

n = 0
prices_sum = 0
prices_sum_square = 0

for line in sys.stdin:
    if not line.startswith('id'):
        fields = line.strip().split(',')
        if len(fields) >= 6:
            price = float(fields[-7])
            n += 1
            prices_sum += price
            prices_sum_square += price**2
mean = prices_sum / n
var = (prices_sum_square - 2 * mean * prices_sum + n * mean**2) / n
print(n, mean, var)	
