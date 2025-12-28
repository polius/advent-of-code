total = 0

grid = [line.strip() for line in open(0)]

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell != '@': continue
        area = [region[max(c-1,0):c+2] for region in grid[max(r-1,0):r+2]]
        if sum([i.count('@') for i in area]) <= 4:
            total += 1

print(f"Total isolated @: {total}")