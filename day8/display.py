#!/usr/bin/env python3

f = open('input.txt', 'r').read().splitlines()

# Part 1: Checking for unique numbers - 1, 4, 7, 8
CHECK_UNIQUE = [2, 4, 3, 7]
sum_p1 = 0

for line in f:
    output_vals = line.split(' | ')[1].split()

    for i in output_vals:
        if (len(i) in CHECK_UNIQUE):
            sum_p1 += 1

print('Part 1:', sum_p1)

# Part 2: Calculate the sum
sum_p2 = 0
for line in f:
    sample_val, output_val = line.split(' | ')
    five_arr = []
    six_arr = []
    for val in sample_val.split():
        if len(val) == 2:
            one_code = set(val)
        elif len(val) == 4:
            four_code = set(val)
        elif len(val) == 3:
            seven_code = set(val)
        elif len(val) == 7:
            eight_code = set(val)
        elif len(val) == 5:
            five_arr.append(val)
        else:
            six_arr.append(val)
    
    # Tackle the 6 lengths one first: 0, 6, 9
    for i in six_arr:
        temp = set(i)
        if one_code & temp != one_code:
            six_code = temp
        elif four_code & temp == four_code:
            nine_code = temp
        else:
            zero_code = temp
    
    # Next the arrays of 5s
    for i in five_arr:
        temp = set(i)
        if one_code & temp == one_code:
            three_code = temp
        elif six_code & temp == temp:
            five_code = temp
        else:
            two_code = temp
    
    DICT = {
        '0': zero_code,
        '1': one_code,
        '2': two_code,
        '3': three_code,
        '4': four_code,
        '5': five_code,
        '6': six_code,
        '7': seven_code,
        '8': eight_code,
        '9': nine_code
    }

    num = ''
    for out in output_val.split():
        num += [k for (k, v) in DICT.items() if v == set(out)][0]
    sum_p2 += int(num)

print('Part 2:', sum_p2)
