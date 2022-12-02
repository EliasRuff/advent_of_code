import numpy as np

strat = np.genfromtxt('input.txt', dtype='str')

score = 0

# I know this is a pretty dumb solution

for opponent, player in strat:
    if player == 'X':
        score += 1
        if opponent == 'A':
            score += 3
        elif opponent == 'B':
            score += 0
        elif opponent == 'C':
            score += 6
    elif player == 'Y':
        score += 2
        if opponent == 'A':
            score += 6
        elif opponent == 'B':
            score += 3
        elif opponent == 'C':
            score += 0
    elif player == 'Z':
        score += 3
        if opponent == 'A':
            score += 0
        elif opponent == 'B':
            score += 6
        elif opponent == 'C':
            score += 3

print(f'Part 1 score = {score}')

score = 0

for opponent, play in strat:
    if play == 'X':
        score += 0
        if opponent == 'A':
            score += 3
        elif opponent == 'B':
            score += 1
        elif opponent == 'C':
            score += 2
    elif play == 'Y':
        score += 3
        if opponent == 'A':
            score += 1
        elif opponent == 'B':
            score += 2
        elif opponent == 'C':
            score += 3
    elif play == 'Z':
        score += 6
        if opponent == 'A':
            score += 2
        elif opponent == 'B':
            score += 3
        elif opponent == 'C':
            score += 1

print(f'Part 2 score = {score}')
