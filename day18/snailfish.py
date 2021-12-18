#!/usr/bin/env python3
from functools import reduce

f = open('input.txt', 'r').readlines()

edited = []
for line in f:
    edited_line = []
    depth = 0
    for c in line.strip():
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        elif c == ',':
            continue
        else:
            edited_line.append([int(c), depth])
    edited.append(edited_line)

def explode(line):
    length = len(line)
    for i, node in enumerate(line):
        num, dep = node
        if dep > 4:
            if i > 0:
                line[i - 1][0] += num
            if i + 2 < length:
                line[i + 2][0] += line[i + 1][0]
            line[i] = [0, dep - 1]
            del line[i + 1]
            return True
    return False

def split(line):
    for i, node in enumerate(line):
        num, dep = node
        if num > 9:
            floor = num // 2
            line[i] = [floor, dep + 1]
            line.insert(i + 1, [num - floor, dep + 1])
            return True
    return False

def change(line):
    edited = line.copy()
    while True:
        if explode(edited):
            continue
        if split(edited):
            continue
        break
    return edited

def add(line1, line2):
    new_line = [[c, d + 1] for c,d in line1 + line2]
    return change(new_line)

def get_magnitude(line):
    l = line.copy()
    while len(l) > 1:
        for i in range(len(l) - 1):
            num_left, depth_left = l[i]
            num_right, depth_right = l[i + 1]
            if depth_left == depth_right:
                l[i] = [num_left * 3 + num_right * 2, depth_right - 1]
                del l[i + 1]
                break
    return l[0][0]


part1 = get_magnitude(reduce(add, edited))
print('Part 1:', part1)

max = 0
for i in edited:
    for j in edited:
        if i == j:
            continue
        res = get_magnitude(add(i, j))
        if res > max:
            max = res

print('Part 2:', max)