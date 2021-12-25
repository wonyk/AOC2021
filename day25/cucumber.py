#!/usr/bin/env python3

f = open("input.txt", "r").read().splitlines()

width = len(f)
length = len(f[0])

east_set = set()
south_set = set()

for i, row in enumerate(f):
    for j, cucum in enumerate(row):
        if cucum == ">":
            east_set.add((i, j))
        elif cucum == "v":
            south_set.add((i, j))


def move_east():
    global east_set, south_set

    has_moved = False
    new_set = set()

    for i, j in east_set:
        # check if the next spot is occupied
        dest = (i, (j + 1) % length)
        if dest in east_set or dest in south_set:
            new_set.add((i, j))
            continue
        new_set.add(dest)
        has_moved = True

    east_set = new_set
    return has_moved


def move_south():
    global east_set, south_set

    has_moved = False
    new_set = set()

    for i, j in south_set:
        # check if the next spot is occupied
        dest = ((i + 1) % width, j)
        if dest in east_set or dest in south_set:
            new_set.add((i, j))
            continue
        new_set.add(dest)
        has_moved = True

    south_set = new_set
    return has_moved


def debug():
    for i in range(width):
        row = ""
        for j in range(length):
            if (i, j) in east_set:
                row += ">"
            elif (i, j) in south_set:
                row += "v"
            else:
                row += "."
        print(row)
    print()


has_moved = True
steps = 0
while has_moved:
    has_moved_east = move_east()
    has_moved = move_south() or has_moved_east
    steps += 1

print("Total steps:", steps)
