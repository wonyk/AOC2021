#!/usr/bin/env python3

import re
from functools import cache

ENTRANCE = {}
WIN_STR = ""
DEPTH = 2

ROOM_NO = 4
COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}
AMPHIS = ["A", "B", "C", "D"]
NO_STOP = {"A": 2, "B": 4, "C": 6, "D": 8}
HALL_VALID_SLOTS = (0, 1, 3, 5, 7, 9, 10)
PART2_EXTRA = "DDCBBAAC"

f = open("input.txt", "r").read()
inp = re.findall(r"[A-Z]+", f)


def main():
    solve_arr = [False, True]
    for i, solving_part_2 in enumerate(solve_arr):
        init_variables(solving_part_2)
        print(f"Part {i + 1}: {solve(solving_part_2)}")


def init_variables(part2=False):
    global WIN_STR, DEPTH

    if part2:
        DEPTH = 4

    start_idx = 11
    WIN_STR = "." * start_idx
    for amphi in AMPHIS:
        ENTRANCE[amphi] = start_idx
        start_idx += DEPTH
        WIN_STR += amphi * DEPTH


def get_start_map(part2=False):
    map_str = "." * 11
    for i in range(ROOM_NO):
        map_str += inp[i]
        if part2:
            map_str += PART2_EXTRA[i * 2]
            map_str += PART2_EXTRA[i * 2 + 1]
        map_str += inp[i + 4]
    return map_str


def swap(game_map, a, b):
    arr = list(game_map)
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
    return "".join(arr)


def solve(part2=False):
    start_map = get_start_map(part2)

    @cache
    def recursive_search(state):
        if state == WIN_STR:
            return 0

        best_cost = float("inf")
        # Start with halls
        for i in range(11):
            curr_type = state[i]
            if curr_type == ".":
                continue

            # get index for the room entrance
            target_dest = ENTRANCE[curr_type]
            valid_move = True

            # check if there are foreigners in room
            for room_idx in range(target_dest, target_dest + DEPTH):
                others = state[room_idx]
                if others != "." and others != curr_type:
                    valid_move = False
                    break

            if not valid_move:
                continue

            no_stop_node = NO_STOP[curr_type]
            # determine which side of the spot is in relative to hallway and do not block
            if i < no_stop_node:
                for j in range(i + 1, no_stop_node):
                    if state[j] != ".":
                        valid_move = False
                        break
            else:
                for j in range(no_stop_node + 1, i):
                    if state[j] != ".":
                        valid_move = False
                        break
            if not valid_move:
                continue

            # check empty slots in rooms and move it there
            empty = sum(
                state[slot] == "." for slot in range(target_dest, target_dest + DEPTH)
            )
            new_state = swap(state, i, target_dest + empty - 1)
            cost = (abs(i - no_stop_node) + empty) * COSTS[curr_type]

            extra_cost = recursive_search(new_state)
            new_cost = cost + extra_cost
            if new_cost < best_cost:
                best_cost = new_cost

        # continue with rooms
        for room_idx, target_type in enumerate(AMPHIS):
            should_move = False
            room_start = ENTRANCE[target_type]
            for i in range(room_start, room_start + DEPTH):
                # check for foreigners
                if state[i] != "." and state[i] != target_type:
                    should_move = True
            if not should_move:
                continue

            empty_slot = sum(
                state[i] == "." for i in range(room_start, room_start + DEPTH)
            )
            steps = empty_slot + 1

            curr_type = state[room_start + empty_slot]
            no_stop_node = NO_STOP[target_type]
            for h in HALL_VALID_SLOTS:
                is_blocked = False
                for i in range(min(h, no_stop_node), max(h, no_stop_node) + 1):
                    if state[i] != ".":
                        is_blocked = True
                        break
                if is_blocked:
                    continue

                new_state = swap(state, h, room_start + empty_slot)
                costs = (steps + abs(h - no_stop_node)) * COSTS[curr_type]
                extra_costs = recursive_search(new_state)
                total_costs = costs + extra_costs

                if total_costs < best_cost:
                    best_cost = total_costs

        return best_cost

    return recursive_search(start_map)


main()
