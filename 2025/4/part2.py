grid = [list(line.strip()) for line in open(0)]
total = 0

while True:
    found = False
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != '@': continue
            region = [subarea[max(0, c-1):c+2] for subarea in grid[max(0, r-1):r+2]]
            if sum([i.count('@') for i in region]) <= 4:
                found = True
                total += 1
                grid[r][c] = '.'

    if not found:
        break

print(f"Total isolated @ removed: {total}")