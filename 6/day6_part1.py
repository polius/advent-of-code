def find_start_position(text):
    for x in range(len(text)):
        for y in range(len(text[x])):
            if text[x][y] == '^':
                return (x, y)

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Convert file into a grid
text = [list(line) for line in file.split('\n') if len(line) != 0]

# Find starting position
x, y = find_start_position(text)
direction = 'up'
steps = 0

while True:
    if text[x][y] != 'X':
        steps += 1
        text[x][y] = 'X'

    if direction == 'up':
        if x - 1 < 0:
            break
        if text[x - 1][y] == '#':
            direction = 'right'
        else:
            x -= 1

    elif direction == 'down':
        if x + 1 >= len(text):
            break
        if text[x + 1][y] == '#':
            direction = 'left'
        else:
            x += 1

    elif direction == 'left':
        if y - 1 < 0:
            break
        if text[x][y - 1] == '#':
            direction = 'up'
        else:
            y -= 1

    elif direction == 'right':
        if y + 1 >= len(text[y]):
            break
        if text[x][y + 1] == '#':
            direction = 'down'
        else:
            y += 1

print(steps)