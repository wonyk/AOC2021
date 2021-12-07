#!/usr/bin/env python3

from os import stat
import statistics

f = open('input.txt').read().strip()

positions = [int(i) for i in f.split(',')]

median_value = statistics.median(positions)
mean_value = statistics.mean(positions)

print('Part 1:', int(sum([ abs(i - median_value) for i in positions ])))

# The math shows that the answer is mean +- 2. We will brute force these values.

minimum = sum([ abs(n - int(mean_value)) * (abs(n - int(mean_value)) + 1)  // 2 for n in positions])
for i in range(-2, 3):
    testedMean = int(mean_value) + i 
    calc = sum([ abs(n - testedMean) * (abs(n - testedMean) + 1) // 2 for n in positions])
    if calc <= minimum:
        minimum = calc

print('Part 2:', minimum)
