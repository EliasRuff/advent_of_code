import numpy as np

rucksacks = np.genfromtxt('input.txt', dtype='str')

errors = []

for content in rucksacks:
    n = len(content)
    compartment_one = content[0:n//2]
    compartment_two = content[n//2:]
    for item in compartment_one:
        if item in compartment_two:
            errors.append(item)
            break

score = 0

for item in errors:
    if item >= 'a' and item <= 'z':
        score += ord(item) - 96
    else:
        score += ord(item) - 38

print(f'Part 1 score = {score}')

badges = []

for split in [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]:
    for item in split[0]:
        if item in split[1] and item in split[2]:
            badges.append(item)
            break

score = 0

for item in badges:
    if item >= 'a' and item <= 'z':
        score += ord(item) - 96
    else:
        score += ord(item) - 38

print(f'Part 2 score = {score}')

