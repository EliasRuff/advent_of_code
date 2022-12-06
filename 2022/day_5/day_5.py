import numpy as np
import copy

crates = [[] for y in range(9)]
#crates = [[] for y in range(3)]


instructions = []

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    for i in range(0, 8):
    #for i in range(0, 3):
        for j in range(1, 34, 4):
        #for j in range(1, 10, 4):
            if lines[i][j] != ' ':
                crates[int((j - 1) / 4)].append(lines[i][j])
    
    for i in range(10, len(lines)):
    #for i in range(5, len(lines)):
        words = lines[i].split()
        instructions.append([int(words[1]), int(words[3]), int(words[5])])

crates_one = copy.deepcopy(crates)

for ins in instructions:
    for i in range(0, ins[0]):
        crate = crates_one[ins[1] - 1].pop(0)
        crates_one[ins[2] - 1].insert(0, crate)

solution = ''

for stack in crates_one:
    if stack:
        solution += stack[0]

print(f'Part 1 solution = {solution}')

for ins in instructions:
    stack = crates[ins[1] - 1][:ins[0]]
    crates[ins[1] - 1] = crates[ins[1] - 1][ins[0]:]
    crates[ins[2] - 1] = stack + crates[ins[2] - 1]

solution = ''

for stack in crates:
    if stack:
        solution += stack[0]

print(f'Part 2 solution = {solution}')