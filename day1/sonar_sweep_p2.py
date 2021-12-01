#!/usr/bin/env python3

f = open('input.txt', 'r')

result = 0
triNum = []

for i in range(3):
    triNum.append(int(f.readline()))

# Use modulo to check against 3 entries ago since the only difference between 
# 2 sets are spaced 4 positions apart
for counter, line in enumerate(f):
    depth = int(line)

    index = counter % 3
    if depth > triNum[index]:
        result += 1
    triNum[index] = depth

print(result)