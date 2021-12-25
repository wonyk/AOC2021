#!/usr/bin/env python3

f = open("input.txt", "r").read().splitlines()
REGISTERS_MAP = {"w": 0, "x": 1, "y": 2, "z": 3}


def checker(number):
    num_str = str(number)
    if "0" in num_str:
        return False
    if len(num_str) != 14:
        return False

    # Registers are in form [w,x,y,z]
    counter = 0
    registers = [0] * 4
    for line in f:
        instr_arr = line.split()
        instr = instr_arr[0]
        first = instr_arr[1]

        if "inp" in instr:
            registers[REGISTERS_MAP[first]] = int(num_str[counter])
            counter += 1
            continue

        second = instr_arr[2]
        if second in REGISTERS_MAP:
            second_val = registers[REGISTERS_MAP[second]]
        else:
            second_val = int(second)

        if "add" in instr:
            registers[REGISTERS_MAP[first]] += second_val
        elif "mul" in instr:
            registers[REGISTERS_MAP[first]] *= second_val
        elif "div" in instr:
            registers[REGISTERS_MAP[first]] //= second_val
        elif "mod" in instr:
            registers[REGISTERS_MAP[first]] %= second_val
        else:
            registers[REGISTERS_MAP[first]] = (
                1 if registers[REGISTERS_MAP[first]] == second_val else 0
            )
    # check valid of z == 0
    if registers[REGISTERS_MAP["z"]] == 0:
        return True
    return False
