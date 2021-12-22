#!/usr/bin/env python3

f = open('input.txt', 'r').read().splitlines()

image = f[2:]

algorithm = []
for c in f[0]:
    if c == '#':
        algorithm.append(1)
    else:
        algorithm.append(0)

# If first is unlit, infinity will always be unlit
# If both are lit, infinity will be lit after the first iteration, leading to infinity as solution
# If first lit and last unlit, infinity will change every iteration
INFINITY = '0'
first, last = algorithm[0], algorithm[-1]
infinity_changes = False
if first != last and first == 1:
    infinity_changes = True

lit_pixels = set()
for i, row in enumerate(image):
    for j, light in enumerate(row):
        if light == '#':
            lit_pixels.add((i, j))

def iterate(lit_pixels):
    global INFINITY
    NEIGHBOUR = [-1, 0, 1]
    
    min_x = min(a[0] for a in lit_pixels)
    max_x = max(a[0] for a in lit_pixels)
    min_y = min(a[1] for a in lit_pixels)
    max_y = max(a[1] for a in lit_pixels)

    new_image = set()
    for i in range(min_x - 1, max_x + 2):
        for j in range(min_y - 1, max_y + 2):
            bin_str = ''
            for x in NEIGHBOUR:
                for y in NEIGHBOUR:
                    x_off = i + x
                    y_off = j + y
                    if min_x <= x_off <= max_x and min_y <= y_off <= max_y:
                        if (x_off, y_off) in lit_pixels:
                            bin_str += '1'
                        else:
                            bin_str += '0'
                    else:
                        bin_str += INFINITY
            result = algorithm[int(bin_str, 2)]
            if result == 1:
                new_image.add((i, j))

    if infinity_changes:
        INFINITY = '1' if INFINITY == '0' else '0'

    return new_image

for i in range(2):
    lit_pixels = iterate(lit_pixels)

print('Part 1:', len(lit_pixels))

for i in range(50 - 2):
    lit_pixels = iterate(lit_pixels)

print('Part 2:', len(lit_pixels))
