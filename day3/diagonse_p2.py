#!/usr/bin/env python3

SIZE = 12
f = open("input.txt", "r")

result = 0
dataArr = []

def check_result_and_filter(listOfStr, isSeekMost, index):
    count = 0
    ones_arr = []
    zeros_arr = []

    for s in listOfStr:
        if s[index] == '1':
            count += 1
            ones_arr.append(s)
        else:
            count -= 1
            zeros_arr.append(s)
    
    if isSeekMost:
        return ones_arr if count >= 0 else zeros_arr
    else:
        return zeros_arr if count >= 0 else ones_arr

for i in f:
    input = i.strip()
    dataArr.append(input)

newArrOxy = dataArr
newArrCo2 = dataArr
for i in range(SIZE):
    newArrOxy = check_result_and_filter(newArrOxy, True, i)

    if len(newArrOxy) == 1:
        oxystr = newArrOxy[0]
        break

for i in range(0, SIZE):
    newArrCo2 = check_result_and_filter(newArrCo2, False, i)

    if len(newArrCo2) == 1:
        co2str = newArrCo2[0]
        break

oxygen_levels = int(oxystr, 2)
co2_levels = int(co2str, 2)

print('oxygen:', oxygen_levels)
print('co2:', co2_levels)

print("Life support rating:", oxygen_levels * co2_levels)
