def compute(grid, position, destinations):
    x, y = position

    if grid[x][y] == 9:
        destinations.add(position)

    else:
        candidates = [(x-1,y),(x,y+1),(x+1,y),(x,y-1)] # up, right, down, left
        for candidate in candidates:
            nx, ny = candidate
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] == grid[x][y] + 1:
                compute(grid, candidate, destinations)


# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

# Convert file into grid
grid = [list(int(j) for j in i) for i in file.split('\n')]

# Find trailheads (values 0)
trailheads = {(x, y): set() for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] == 0}

# Compute trailheads
score = 0
for trailhead, destinations in trailheads.items():
    compute(grid, trailhead, destinations)
    score += len(destinations)

print(score)