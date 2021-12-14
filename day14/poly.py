#!/usr/bin/env python3

from collections import defaultdict, Counter

f = open('input.txt', 'r')

pairs = defaultdict(int)
poly_counter = defaultdict(int)
mapping = defaultdict()

initial = f.readline().strip()
f.readline()

for line in f:
    pair, add = line.strip().split(' -> ')
    mapping[pair] = add

for i in range(0, len(initial) - 1):
    pair = initial[i:i+2]
    pairs[pair] += 1
    poly_counter[initial[i]] += 1
poly_counter[initial[-1]] += 1

def iterate(NUM):
    global pairs, mapping, poly_counter

    for _ in range(NUM):
        new_pairs = defaultdict(int)

        for pair, num in pairs.items():
            addition = mapping[pair]
            new_pairs[pair[0] + addition] += num
            new_pairs[addition + pair[1]] += num
            poly_counter[addition] += num

        pairs = new_pairs

    c = Counter(poly_counter).most_common()
    max = c[0][1]
    min = c[-1][1]
    return max - min

print('Part 1:', iterate(10))
print('Part 2:', iterate(40 - 10))
