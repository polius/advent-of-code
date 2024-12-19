def find_start_position(text):
    for x in range(len(text)):
        for y in range(len(text[x])):
            if text[x][y] == '^':
                return (x, y, 'up')

def next_position(text, x, y, direction):
    if direction == 'up':
        if x - 1 >= 0 and text[x - 1][y] in ['#','O']:
            direction = 'right'
            text[x][y] = '+'
        else:
            text[x][y] = '+' if text[x][y] in ['+','-'] else '|'
            x -= 1

    if direction == 'down':
        if x + 1 < len(text) and text[x + 1][y] in ['#','O']:
            direction = 'left'
            text[x][y] = '+'
        else:
            text[x][y] = '+' if text[x][y] in ['+','-'] else '|'
            x += 1

    if direction == 'left':
        if y - 1 >= 0 and text[x][y - 1] in ['#','O']:
            direction = 'up'
            text[x][y] = '+'
        else:
            text[x][y] = '+' if text[x][y] in ['+','|'] else '-'
            y -= 1

    if direction == 'right':
        if y + 1 < len(text[x]) and text[x][y + 1] in ['#','O']:
            direction = 'down'
            text[x][y] = '+'
        else:
            text[x][y] = '+' if text[x][y] in ['+','|'] else '-'
            y += 1

    return (x, y, direction)

def simulate(text, start):
    x, y, direction = start
    visited = set()
    while True:
        # Outside the grid
        if not (0 <= x < len(text)) or not (0 <= y < len(text[x])):
            return False

        # Loop detected
        if (x, y, direction) in visited:
            return True

        visited.add((x, y, direction))
        x, y, direction = next_position(text, x, y, direction)

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Convert file into a grid
text = [list(line) for line in file.split('\n') if len(line) != 0]

# Find starting position
start = find_start_position(text)
x, y, direction = start

# Start computing
obstructions = set()
while True:
    x, y, direction = next_position(text, x, y, direction)

    # Check if position is out of the grid
    if not (0 <= x < len(text)) or not (0 <= y < len(text[x])):
        break

    # Place obstruction
    text[x][y] = 'O'

    # Simulate new grid
    if simulate(text, start):
        if (x, y) not in obstructions:
            obstructions.add((x, y))
            # print(f"OBSTRUCTION: {len(obstructions)}")
            # print('\n'.join(''.join(line) for line in text))

    # Reset the grid
    text = [list(line) for line in file.split('\n') if len(line) != 0]

print(len(obstructions))
