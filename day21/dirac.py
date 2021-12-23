#!/usr/bin/env python3

from itertools import product
from collections import Counter
from functools import cache

f = open('input.txt', 'r').read().splitlines()

def deterministic_die():
    rolls = 0
    curr_face = 0

    scores = [0, 0]
    # Force loc to count starting from 0
    loc = [int(f[0].split(': ')[1]) - 1, int(f[1].split(': ')[1]) - 1]

    player = 0
    while (max(scores) < 1000):
        sum = 0
        for _ in range(3):
            sum += (curr_face + 1) % 100
            curr_face += 1
        final_loc = (loc[player] + sum) % 10
        loc[player] = final_loc
        scores[player] += final_loc + 1
        rolls += 3
        player ^= 1

    return min(scores) * rolls

possible_rolls = Counter([sum(i) for i in product([1, 2, 3], repeat=3)])
WINNING_SCORE = 21

@cache
def quantum_die(player1_pos, player1_score, player2_pos, player2_score, turn):
    if player1_score >= WINNING_SCORE:
        return [1, 0]
    elif player2_score >= WINNING_SCORE:
        return [0, 1]

    wins = [0, 0]
    for sum_moves, freq in possible_rolls.items():
        new_p1_pos, new_p2_pos = player1_pos, player2_pos
        new_p1_score, new_p2_score = player1_score, player2_score

        if turn:
            new_p1_pos = ((player1_pos - 1 + sum_moves) % 10) + 1
            new_p1_score += new_p1_pos
        else:
            new_p2_pos = ((player2_pos - 1 + sum_moves) % 10) + 1
            new_p2_score += new_p2_pos

        p1_win, p2_win = quantum_die(new_p1_pos, new_p1_score, new_p2_pos, new_p2_score, not turn)

        wins[0] += p1_win * freq
        wins[1] += p2_win * freq

    return wins

print('Part 1:', deterministic_die())

INITIAL_SCORE = 0
P1_TURN = True
wins_tally = quantum_die(int(f[0].split(': ')[1]), INITIAL_SCORE, int(f[1].split(': ')[1]), INITIAL_SCORE, P1_TURN)

print('Part 2:', max(wins_tally))
