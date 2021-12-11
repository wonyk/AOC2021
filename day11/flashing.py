#!/usr/bin/env python3

from collections import deque

data = []
f = open('input.txt', 'r').read().splitlines()

sum_part1 = 0
part2 = 0
for line in f:
    octopus = []
    for o in line:
        octopus.append(int(o))
    data.append(octopus)

def get_neighbours(tup):
    row, col = tup
    ranges = [-1, 0, 1]
    neighbours = []
    for i in ranges:
        for j in ranges:
            if i == 0 and j == 0:
                continue
            candidate = (row + i, col + j)
            if candidate[0] in range(10) and candidate[1] in range(10):
                neighbours.append(candidate)
    return neighbours

for counter in range(10000):
    initial = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] += 1
            if data[i][j] > 9:
                initial.append((i, j))
                data[i][j] = 0
    
    stack = initial.copy()
    flashed = set(initial)

    while len(stack) != 0:
        neighbours = get_neighbours(stack.pop())
        for n in neighbours:
            if n in flashed:
                continue
            r, c = n
            data[r][c] += 1
            if data[r][c] > 9:
                stack.append(n)
                flashed.add(n)
                data[r][c] = 0

    if len(flashed) == len(data) * len(data[0]):
        part2 = counter + 1
        break
    
    if counter < 100:
        sum_part1 += len(flashed)


print('Part 1:', sum_part1)
print('Part 2:', part2)
