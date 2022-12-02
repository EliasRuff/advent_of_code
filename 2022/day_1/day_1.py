li = [0]

with open('input.txt', 'r') as f:
    for line in f:
        num = line.strip()
        if num:
            li[-1] += int(num)
        else:
            li.append(0)

li.sort()

print(li[-1] + li[-2] + li[-3])