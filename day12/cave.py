#!/usr/bin/env python3

f = open('input.txt', 'r')

adj_list = {}
visited = []
part1 = 0
part2 = 0
twiceUsed = False

# Create and set up adjacency list
for line in f:
    s, d = line.strip().split("-")
    if not s in adj_list:
        adj_list[s] = []
    if not d in adj_list:
        adj_list[d] = []
    adj_list[s].append(d)
    adj_list[d].append(s)

# Use DFS to traverse and check which ones end at "end"
def dfs(node):
    global part1, part2, twiceUsed
    if node == 'end':
        if twiceUsed:
            part2 += 1
        else:
            part1 += 1
        return

    visited.append(node)

    connected = adj_list[node]
    for u in connected:
        if u.isupper() or u not in visited:
            dfs(u)
        elif u != 'start' and u.islower() and not twiceUsed:
            twiceUsed = True
            dfs(u)
            twiceUsed = False
    visited.remove(node)

dfs("start")
print("Part 1:", part1)
print("Part 2:", part1 + part2)
