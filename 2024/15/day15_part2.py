def check(grid, position, movement):
    py, px = position

    if grid[py][px] == '#':
        return False
    
    if grid[py][px] == '.':
        return True

    if movement == '^':
        if grid[py][px] == '[':
            return check(grid, (py-1, px), movement) and check(grid, (py-1, px+1), movement)

        elif grid[py][px] == ']':
            return check(grid, (py-1, px), movement) and check(grid, (py-1, px-1), movement)

    elif movement == 'v':
        if grid[py][px] == '[':
            return check(grid, (py+1, px), movement) and check(grid, (py+1, px+1), movement)

        elif grid[py][px] == ']':
            return check(grid, (py+1, px), movement) and check(grid, (py+1, px-1), movement)


def move(grid, position, movement):
    py, px = position

    if movement == '<':
        for x in range(px-1, 0, -1):
            if grid[py][x] == '#':
                break

            elif grid[py][x] == '.':
                for x in range(x, px):
                    grid[py][x] = grid[py][x+1]
                grid[py][px] = '.'
                return (py, px-1)

    elif movement == '>':
        for x in range(px+1, len(grid[py])):
            if grid[py][x] == '#':
                break

            elif grid[py][x] == '.':
                for x in range(x, px, -1):
                    grid[py][x] = grid[py][x-1]
                grid[py][px] = '.'
                return (py, px+1)

    elif movement == '^':
        for y in range(py-1, 0, -1):
            if grid[y][px] == '#':
                break

            elif grid[y][px] == '[':
                if check(grid, (y, px), movement) and check(grid, (y, px+1), movement):
                    move(grid, (y, px+1), movement)
                else:
                    break

            elif grid[y][px] == ']':
                if check(grid, (y, px), movement) and check(grid, (y, px-1), movement):
                    move(grid, (y, px-1), movement)
                else:
                    break

            elif grid[y][px] == '.':
                for y in range(y, py):
                    grid[y][px] = grid[y+1][px]
                grid[py][px] = '.'
                return (py-1, px)

    elif movement == 'v':
        for y in range(py+1, len(grid)):
            if grid[y][px] == '#':
                break

            elif grid[y][px] == '[':
                if check(grid, (y, px), movement) and check(grid, (y, px+1), movement):
                    move(grid, (y, px+1), movement)
                else:
                    break

            elif grid[y][px] == ']':
                if check(grid, (y, px), movement) and check(grid, (y, px-1), movement):
                    move(grid, (y, px-1), movement)
                else:
                    break

            elif grid[y][px] == '.':
                for y in range(y, py, -1):
                    grid[y][px] = grid[y-1][px]
                grid[py][px] = '.'
                return (py+1, px)

    return (py, px)

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

# Enlarge map
file = file.replace('#', '##').replace('.','..').replace('@','@.').replace('O','[]')

# Initialize grid and movements vars
grid = [list(line) for line in file.split('\n\n')[0].split('\n')]
movements = file.split('\n\n')[1].replace('\n','')

# Find current position
position = next(((y, x) for y, row in enumerate(grid) for x, char in enumerate(row) if char == '@'), None)

# Apply movements
for m in movements:
    position = move(grid, position, m)
    
print('\n'.join(''.join(row) for row in grid))

# Compute distances
distances = sum([100 * y + x for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '['])
print(distances)