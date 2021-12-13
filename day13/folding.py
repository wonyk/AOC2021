#!/usr/bin/env python3

f = open('input.txt', 'r').read().splitlines()

points = set()
folding = False
part_1 = False
min_x = 0
min_y = 0
for line in f:
    if line == '':
        folding = True
        continue

    if not folding:
        x, y = (int(i) for i in line.split(','))
        points.add((x, y))

    else:
        instr = line.split()[-1]
        axis, num = instr.split("=")
        num = int(num)

        points_new = set()
        if axis == 'y':
            min_y = num
            for (x, y) in points:
                new_p = min(y, num * 2 - y)
                points_new.add((x, new_p))
        else:
            min_x = num
            for (x, y) in points:
                new_p = min(x, num * 2 - x)
                points_new.add((new_p, y))

        if not part_1:
            print('Part 1:', len(points_new))
            part_1 = True

        points = points_new

print('Part 2:')
for i in range(min_y + 1):
    for j in range(min_x + 1):
        print('#' if (j, i) in points else ' ', end='')
    print()
