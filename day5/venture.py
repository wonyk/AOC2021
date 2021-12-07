#!/usr/bin/env python3

f = open('input.txt')
max_x = 0
max_y = 0
raw_data = f.readlines()

# Calculate the max
for data in raw_data:
    FROM, _, TO = data.strip().split()
    X,Y = FROM.split(",")
    X = int(X)
    Y = int(Y)
    max_x = X if max_x < X else max_x
    max_y  = Y if max_y < Y else max_y

    X,Y = TO.split(",")
    X = int(X)
    Y = int(Y)
    max_x = X if max_x < X else max_x
    max_y  = Y if max_y < Y else max_y

max_x += 1
max_y += 1

# Create the array / list
# First one for part 1, second for part 2
array = []
array.append([ [0] * max_x for _ in range(max_y) ])
array.append([ [0] * max_x for _ in range(max_y) ])

# Populate the data
for data in raw_data:
    FROM, _, TO = data.strip().split()
    X1,Y1 = FROM.split(",")
    X2,Y2 = TO.split(",")
    X1 = int(X1)
    X2 = int(X2)
    Y1 = int(Y1)
    Y2 = int(Y2)

    MINY = Y1 if Y1 < Y2 else Y2
    MAXY = Y1 if Y1 > Y2 else Y2
    MINX = X1 if X1 < X2 else X2
    MAXX = X1 if X1 > X2 else X2

    # Check horizontal
    if X1 == X2:
        for i in range(MINY, MAXY + 1):
            array[0][i][X1] += 1
            array[1][i][X1] += 1
    elif Y1 == Y2:
        for i in range(MINX, MAXX + 1):
            array[0][Y1][i] += 1
            array[1][Y1][i] += 1

    # Remains diagonal
    else:
        if X1 > X2:
            # Swap the pairs
            X1, X2 = X2, X1
            Y1, Y2 = Y2, Y1
        counter = 0
        for i in range(X1, X2 + 1):
            if Y1 > Y2:
                array[1][Y1 - counter][i] += 1
            else:
                array[1][Y1 + counter][i] += 1
            counter += 1

# Check for > 1 in array
answer_p1 = 0
answer_p2 = 0
for i in range(max_y):
    for j in range(max_x):
        if array[0][i][j] > 1:
            answer_p1 += 1
        if array[1][i][j] > 1:
            answer_p2 += 1

print('Part 1:', answer_p1)
print('Part 2:', answer_p2)

