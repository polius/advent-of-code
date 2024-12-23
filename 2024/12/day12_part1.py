# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

grid = [list(line) for line in file.split('\n')]

# Compute regions
regions = {}
visited = [[False for _ in range(len(grid[x]))] for x in range(len(grid))]

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if not visited[x][y]:
            group = []
            stack = [(x, y)]
            visited[x][y] = True

            while stack:
                cx, cy = stack.pop()
                group.append((cx, cy))

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[x]) and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

            if grid[x][y] not in regions:
                regions[grid[x][y]] = [group]
            else:
                regions[grid[x][y]].append(group)

# Compute perimeters
perimeters = {}

for p, r in regions.items():
    perimeters[p] = []
    for group in r:
        perimeter = 0
        for x, y in group:
            # Check each of the four sides of the cell (up, down, left, right)
            if not (x-1 >= 0 and grid[x-1][y] == grid[x][y]):
                perimeter += 1
            if not (x+1 < len(grid) and grid[x+1][y] == grid[x][y]):
                perimeter += 1
            if not (y-1 >= 0 and grid[x][y-1] == grid[x][y]):
                perimeter += 1
            if not (y+1 < len(grid[x]) and grid[x][y+1] == grid[x][y]):
                perimeter += 1

        perimeters[p].append(perimeter)

# Get computed data
total = 0
for plant in regions.keys():
    for region in range(len(regions[plant])):
        area = len(regions[plant][region])
        perimeter = perimeters[plant][region]
        print(f"- A region of {plant} plants with price {area} * {perimeter} = {area * perimeter}.")
        total += area * perimeter

print(f"Total: {total}")