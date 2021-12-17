#!/usr/bin/env python3

f = open('input.txt', 'r').readline().strip()

inpArr = f.split("=")
x1 = int(inpArr[1][:inpArr[1].index("..")])
x2 = int(inpArr[1][inpArr[1].index("..") + 2: inpArr[1].index(",")])
y1 = int(inpArr[2][:inpArr[2].index("..")])
y2 = int(inpArr[2][inpArr[2].index("..")+ 2:])

# Part 1: Because of physics, the object will always reach back to y = 0 regardless of the initial upward velocity,
# assuming we are aiming for the highest height. This means that the highest would be achieved when the next following step
# would plunge it into the area directly with the maximum gravity. Thus, the max upward force is abs(y - 1). Using
# arithmetic progression, the result would be abs(y + 1) / 2 * abs(y - 1 + 1)
def arithmetic_math():
    return abs(y1) * abs(y1 + 1) // 2

print('Part 1:', arithmetic_math())

def check(x_trial, y_trial):
    x = 0
    y = 0
    x_curr = x_trial
    y_curr = y_trial

    while y >= y1 and x <= x2:
        x += x_curr
        y += y_curr

        x_curr = x_curr - 1 if x_curr > 0 else 0
        y_curr -= 1

        if y1 <= y <= y2 and x1 <= x <= x2:
            return True
    return False



# For part 2, the x is bounded to the furthest x position, else will definitely exceed
# The y is bounded by the furthest y position and with part 1 logic, the maximum y will be abs(y1 - 1)
total = 0
for x_trial in range(x2 + 1):
    for y_trial in range(y1, abs(y1)):
        if check(x_trial, y_trial):
            total += 1

print('Part 2:', total)
