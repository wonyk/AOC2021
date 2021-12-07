#!/usr/bin/env python3

f = open('input.txt').read()
fishes = [int(i) for i in f.split(',')]
FIRST_CYCLE = 8
NORMAL_CYCLE = 6
days = [0] * ( FIRST_CYCLE + 1 )

for fish in fishes:
    days[fish] += 1

def get_ans(ROUNDS):
    daysCount = days.copy()
    for i in range(ROUNDS):
        numBirth = daysCount.pop(0)
        daysCount.append(numBirth)
        daysCount[NORMAL_CYCLE] += numBirth

    return sum(daysCount)

print('Part 1:', get_ans(80))
print('Part 2:', get_ans(256))
