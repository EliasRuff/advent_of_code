from typing import List

class Dir:
    def __init__(self, name):
        self.name = name
        self.size = -1
        self.children = []
    def __str__(self) -> str:
        return f'Dir({self.name},{self.size}) START {self.children} END'
    def __repr__(self) -> str:
        return self.__str__()

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
    def __str__(self) -> str:
        return f'File({self.name},{self.size})'
    def __repr__(self) -> str:
        return self.__str__()

lines = []

with open('input.txt', mode='r') as f:
    lines = f.readlines()

def fs_build_recursion(node, i: int) -> int:
    current_line = lines[i].split()
    if current_line[0] == '$':
        if current_line[1] == 'cd':
            if current_line[2] == '..':
                return i + 1
            else:
                while current_line[0] == '$' and current_line[1] == 'cd':
                    if current_line[2] == '..':
                        return i + 1
                    next_node = [x for x in node.children if isinstance(x, Dir) and x.name == current_line[2]]
                    i = fs_build_recursion(next_node[0], i + 1)
                    if i == len(lines):
                        return i
                    current_line = lines[i].split()
        if current_line[1] == 'ls' and current_line[0] == '$':
            i += 1
            current_line = lines[i].split()
    
    while current_line[0] != '$':
        if current_line[0] == 'dir':
            node.children.append(Dir(current_line[1]))
        else:
            node.children.append(File(current_line[1], int(current_line[0])))
        i += 1
        if i == len(lines):
            return i
        else:
            current_line = lines[i].split()

    return fs_build_recursion(node, i)

def fs_size_recursion(node) -> int:
    node_size = 0
    for n in node.children:
        if isinstance(n, Dir):
            node_size += fs_size_recursion(n)
        else:
            node_size += n.size
    node.size = node_size
    return node_size

def fs_part_one_recursion(node) -> int:
    p1 = 0
    for n in node.children:
        if isinstance(n, Dir):
            p1 += fs_part_one_recursion(n)
    if node.size <= 100_000:
        p1 += node.size
    return p1

def fs_part_two_recursion(node, min_size: int):
    candidates = []
    if node.size > min_size:
        candidates.append(node)
    for n in node.children:
        if isinstance(n, Dir):
            candidates.append(fs_part_two_recursion(n, min_size))
    if not candidates:
        return None
    else:
        best = candidates[0]
        for n in candidates:
            if n != None:
                if n.size < best.size:
                    best = n
        return best    

filesystem = Dir('/')

fs_build_recursion(filesystem, 1)

fs_size_recursion(filesystem)

print(f'Part 1 score = {fs_part_one_recursion(filesystem)}')

free_space = 70_000_000 - filesystem.size

min_freed = 30_000_000 - free_space

part_two = fs_part_two_recursion(filesystem, min_freed)

if part_two != None:
    part_two = part_two.size
else:
    part_two = 0

print(f'Part 2 score = {part_two}')