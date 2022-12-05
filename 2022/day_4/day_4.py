import numpy as np

assignments = np.genfromtxt('example.txt', dtype='str', delimiter=',')

score = 0

for pair in assignments:
    newpairs = np.array([x.split('-') for x in pair], dtype=int)
    if newpairs[0][0] <= newpairs[1][0] and newpairs[0][1] >= newpairs[1][1]:
        score += 1
    elif newpairs[0][0] >= newpairs[1][0] and newpairs[0][1] <= newpairs[1][1]:
        score += 1

print(f'Part 1 score = {score}')

score = 0

for pair in assignments:
    newpairs = np.array([x.split('-') for x in pair], dtype=int)
    if newpairs[0][0] <= newpairs[1][0] and newpairs[0][1] >= newpairs[1][1]:
        score += 1
    elif newpairs[0][0] >= newpairs[1][0] and newpairs[0][1] <= newpairs[1][1]:
        score += 1
    elif newpairs[0][0] >= newpairs[1][0] and newpairs[0][0] <= newpairs[1][1]:
        score += 1
    elif newpairs[0][1] >= newpairs[1][0] and newpairs[0][1] <= newpairs[1][1]:
        score += 1 

print(f'Part 2 score = {score}')
