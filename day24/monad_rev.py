#!/usr/bin/env python3

from monad import checker

"""
The input can be split into 14 parts with very similar content and some changing variables
The python psuedo code is as follows:

for _ in range(14):
    w = input()
    if (z % 26 + {b}) != w: # condition 1
        z //= {a}
        z *= 26
        z += (w + {c})
    else:                   # condition 2
        z //= {a}

From the input, we can see that condition 1 will never be reached in certain cases when b >= 10 since
z >= 0. For all of those cases, a = 1, forcing condition 1 to occur. This means that we can see z as base 26,
essentially thinking like alphabetical letters where a == 1 will add a new "letter" and a == 26 can remove a "letter".

"""

f = open("input.txt", "r").read().splitlines()
numbers = []
for i in range(14):
    offset = i * 18
    a = int(f[offset + 4].split()[2])
    b = int(f[offset + 5].split()[2])
    c = int(f[offset + 15].split()[2])
    numbers.append((a, b, c))


def convert_to_int_and_check(num_string):
    number = "".join([str(i) for i in num_string])
    assert checker(number)
    return number


smallest_sol = [0] * 14
largest_sol = [9] * 14
valid_nums = range(1, 10)
rev_nums = valid_nums[::-1]

stack = []
for i, num in enumerate(numbers):
    _, b, c = num
    # Handle forced condition 1
    if b >= 10:
        stack.append((i, c))
    else:
        prev_idx, added = stack.pop()

        # find largest
        for j in rev_nums:
            if j + added + b in valid_nums:
                largest_sol[prev_idx] = j
                largest_sol[i] = j + added + b
                break

        # find smallest
        for j in valid_nums:
            if j + added + b in valid_nums:
                smallest_sol[prev_idx] = j
                smallest_sol[i] = j + added + b
                break

print("Largest:", convert_to_int_and_check(largest_sol))
print("Smallest:", convert_to_int_and_check(smallest_sol))
