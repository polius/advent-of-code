from functools import lru_cache

grid = [list(line.strip()) for line in open(0)]
start = (0, grid[0].index('S'))

@lru_cache()
def compute(position):
    x, y = position

    if x == len(grid):
        return 0
    
    hits = 0

    if grid[x][y] == '^':
        hits += 1
        hits += compute((x, y-1))
        hits += compute((x, y+1))
    else:
        hits += compute((x+1, y))

    return hits

result = compute(start) + 1
print(result)