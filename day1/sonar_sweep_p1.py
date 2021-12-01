#!/usr/bin/env python3

f = open('input.txt', 'r')

result = 0
prev = int(f.readline())

for line in f:
    depth = int(line)
    if depth > prev:
        result += 1
    prev = depth

print(result)