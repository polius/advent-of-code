def compute(grid, position, hits, visited):
    x, y = position

    if x == len(grid) or position in visited:
        return 0
    
    visited.add(position)

    if grid[x][y] == '^':
        hits.add(position)
        compute(grid, (x+1, y-1), hits, visited)
        compute(grid, (x+1, y+1), hits, visited)
    else:
        compute(grid, (x+1, y), hits, visited)

grid = [list(line.strip()) for line in open(0)]
hits = set()
visited = set()

start = (0, grid[0].index('S'))
result = compute(grid, start, hits, visited)

print(len(hits))