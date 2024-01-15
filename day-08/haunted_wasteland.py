import math
import re

# Code by u/4HbQ
dirs, _, *graph = open("day08.in").read().split('\n')
graph = {n: d for n, *d in [re.findall(r'\w+', s) for s in graph]}
start = [n for n in graph if n.endswith('A')]

# Part One
def part_one():
    steps = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        for direction in dirs:
            if current_node == 'ZZZ':
                break
            if direction == 'L':
                current_node =  graph[current_node][False]
            if direction == 'R':
                current_node =  graph[current_node][True]
            steps += 1
    return steps

print(part_one())


# Part Two
# Solution by u/4HbQ
def solve(pos, steps=0):
    while not pos.endswith('Z'):
        dir = dirs[steps % len(dirs)]
        pos = graph[pos][dir=='R']
        steps += 1
    return steps

print(math.lcm(*map(solve, start)))