#!/usr/bin/env python3

from heapq import heappop, heappush

f = open('input.txt', 'r')

data = []
for line in f:
    data.append([int(i) for i in line.strip()])

def dijkstra(part2 = False):
    global data

    pq = [(0, 0, 0)]
    seen = set()

    ORIGINAL_LENGTH = len(data)
    ORIGINAL_WIDTH = len(data[0])
    MAX_X = ORIGINAL_LENGTH if not part2 else ORIGINAL_LENGTH * 5
    MAX_Y = ORIGINAL_WIDTH if not part2 else ORIGINAL_WIDTH * 5

    while pq:
        total_weight, x, y = heappop(pq)
        if x == MAX_X - 1 and y == MAX_Y - 1:
            return total_weight

        for a, b in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x = x + a
            new_y = y + b
            if new_x < 0 or new_y < 0 or new_x >= MAX_X or new_y >= MAX_Y:
                continue

            if (new_x, new_y) in seen:
                continue

            seen.add((new_x, new_y))

            additional = new_x // ORIGINAL_LENGTH + new_y // ORIGINAL_WIDTH
            calc = data[new_x % ORIGINAL_LENGTH][new_y % ORIGINAL_WIDTH] + additional
            calc = (calc - 1) % 9 + 1

            heappush(pq, (calc + total_weight, new_x, new_y))
    return 0

print('Part 1:', dijkstra())
print('Part 2:', dijkstra(True))
