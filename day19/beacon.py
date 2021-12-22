#!/usr/bin/env python3

from collections import defaultdict

f = open('input.txt', 'r').read().splitlines()

scanners = []
tmp = []
for line in f[1:]:
    if line == "":
        continue
    if "---" in line:
        scanners.append(tmp)
        tmp = []
    else:
        x, y, z = map(int, line.split(","))
        tmp.append((x, y, z))
# Handle the last case
scanners.append(tmp)

aligned_beacons = set()
aligned_scanners = [scanners[0]]
other_scanners = scanners[1:]

def rotate(pt, num):
    a, b, c = pt
    if num == 0:
        return (a, b, c)
    elif num == 1:
        return (-b, a ,c)
    elif num == 2:
        return (-a, -b, c)
    elif num == 3:
        return (b, -a, c)

def orientate(pt, num):
    rotated_beacons = rotate(pt, num // 6)
    remainder = num % 6
    a, b, c = rotated_beacons
    if remainder == 0:
        return (a, b, c)
    if remainder == 1:
        return (c, b, -a)
    if remainder == 2:
        return (-a, b, -c) # check again (a, -b, -c)
    if remainder == 3:
        return (-c, b, a)
    if remainder == 4:
        return (a, -c, b)
    if remainder == 5:
        return (a, c, -b)

def get_orientation(beacon_arr, num):
    tmp = []
    for b in beacon_arr:
        tmp.append(orientate(b, num))
    return tmp

def get_diffs(aligned, others):
    x1,y1,z1 = aligned
    x0,y0,z0 = others
    return (x1 - x0, y1 - y0, z1 - z0)

def find_similar(trial, known):
    for i in range(24):
        matched_diff = defaultdict(int)

        for beacon_aligned in known:
            beacons_list_adjusted = get_orientation(trial, i)
            for rotations in beacons_list_adjusted:

                diff = get_diffs(beacon_aligned, rotations)
                matched_diff[diff] += 1 

        max_val = max(matched_diff.values())
        if max_val >= 12:
            dx, dy, dz = list(matched_diff.keys())[list(matched_diff.values()).index(max_val)]
            return [(x + dx, y + dy, z + dz) for (x, y, z) in beacons_list_adjusted], (dx, dy, dz)

    return False

aligned_beacons.update(aligned_scanners[0])
scanner_abs = [(0, 0, 0)]
while True:
    restart = False
    for target in aligned_scanners:
        if restart:
            break
        for trial in other_scanners:
            if result := find_similar(trial, target):
                aligned, diff = result
                scanner_abs.append(diff)
                aligned_scanners.append(aligned)
                other_scanners.remove(trial)
                restart = True
                aligned_beacons.update(aligned)
                break
    
    if len(other_scanners) == 0:
        break

print('Part 1:', len(aligned_beacons))

def get_dist(i, j):
    return sum(abs(a - b) for a, b in zip(i, j))

max_dist = 0
for i in scanner_abs:
    for j in scanner_abs:
        # prevent double counting
        if i >= j:
            continue
        max_dist = max(max_dist, get_dist(i, j))

print('Part 2:', max_dist)