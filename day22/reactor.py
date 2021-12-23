#!/usr/bin/env python3

from collections import defaultdict

f = open('input.txt', 'r').read().splitlines()

instructions = []
for line in f:
    instr, coord = line.split() 
    is_on = instr == 'on'
    
    parsed = [is_on]
    for c in coord.split(','):
        parsed.extend(list(map(int, c[2:].split('..'))))
    instructions.append(parsed)

cubes_on = set()

def check_range(inst):
    return all([inst[i] >= -50 and inst[i + 1] <= 50 for i in range(0, len(inst), 2)])

def parse_cubes(ins):
    turn_on, x0, x1, y0, y1, z0, z1 = ins
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            for z in range(z0, z1 + 1):
                if turn_on:
                    cubes_on.add((x, y, z))
                else:
                    try:
                        cubes_on.remove((x, y, z))
                    except:
                        pass

def part_1():
    for ins in instructions:
        if check_range(ins[1:]):
            parse_cubes(ins)
    return len(cubes_on)

def intersection(first, second):
    x1, x2, y1, y2, z1, z2 = first
    a1, a2, b1, b2, c1, c2 = second

    max_x1 = max(x1, a1)
    min_x2 = min(x2, a2)
    max_y1 = max(y1, b1)
    min_y2 = min(y2, b2)
    max_z1 = max(z1, c1)
    min_z2 = min(z2, c2)

    if max_x1 <= min_x2 and max_y1 <= min_y2 and max_z1 <= min_z2:
        return max_x1, min_x2, max_y1, min_y2, max_z1, min_z2

def volume(x,X,y,Y,z,Z):
    return (X - x + 1) * (Y - y +1 ) * (Z - z + 1)

print('Part 1:', part_1())

cube_dict = defaultdict(int)
for instr in instructions:
    turn_on, coords = instr[0], instr[1:]

    for current in cube_dict.copy():
        if intersections := intersection(current, coords):
            cube_dict[intersections] -= cube_dict[current]

    if turn_on:
        cube_dict[tuple(coords)] += 1

print('Part 2:', sum(volume(*dimensions) * magnitude for dimensions, magnitude in cube_dict.items()))
