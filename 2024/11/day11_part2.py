memory = {}

def solve(stone, blink):
    if blink == 0:
        return 1
    elif (stone, blink) in memory:
        return memory[(stone, blink)]
    elif stone == 0:
        val = solve(1, blink - 1)
    elif len(stone_str := str(stone)) % 2 == 0:
        mid = len(stone_str) // 2
        val = solve(int(stone_str[:mid]), blink - 1) + solve(int(stone_str[mid:]), blink - 1)
    else:
        val = solve(stone * 2024, blink - 1)

    memory[(stone, blink)] = val
    return val

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

stones = list(map(int, file.split(' ')))

print(sum(solve(stone, 75) for stone in stones))
