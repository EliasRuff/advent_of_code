def part_one(stream: str, win_len: int) -> int:
        window = stream[:win_len]
        num = 0
    
        for char in window:
            num += window.count(char)

        if num == win_len:
            return 0

        for i in range(win_len, len(stream)):
            window = window[1:] + stream[i]
            num = 0
            for char in window:
                num += window.count(char)
            if num == win_len:
                return i + 1
        return len(stream)

with open('input.txt', mode='r') as f:
    stream = f.read()
    print(f'Part 1 solution = {part_one(stream, 4)}')
    print(f'Part 2 solution = {part_one(stream, 14)}')