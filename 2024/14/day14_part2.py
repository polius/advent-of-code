import re
import math

# Define constraints
WIDE = 101
TALL = 103

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

# Pattern to match 'p=' or 'v=' followed by numbers with commas
pattern = r'(-?\d+(?:,-?\d+)*)'

# Find all matches
matches = re.findall(pattern, file)

# Build data
data = [
    {'p': tuple(map(int, matches[i].split(','))), 'v': tuple(map(int, matches[i+1].split(',')))}
    for i in range(0, len(matches), 2)
]

seconds = 0
while True:
    # Compute
    result = {}
    for robot in data:
        px, py = robot['p']
        vx, vy = robot['v']

        nx = (px + vx * seconds) % WIDE
        ny = (py + vy * seconds) % TALL

        final_position = (nx, ny)
        result[final_position] = result.get(final_position, 0) + 1

    # Compute adjacent positions
    scores = []
    for k in result.keys():
        x, y = k
        score = 0
        if (x, y-1) in result:
            score += 1
        if (x+1, y-1) in result:
            score += 1
        if (x+1, y) in result:
            score += 1
        if (x+1, y+1) in result:
            score += 1
        if (x, y+1) in result:
            score += 1
        if (x-1, y+1) in result:
            score += 1
        if (x-1, y) in result:
            score += 1
        if (x-1, y-1) in result:
            score += 1
        scores.append(score)

    avg = sum(scores) / len(scores)
    print(f"Seconds {seconds}: {avg}")
    if avg >= 1:
        break
    seconds += 1

# Display image
image = ''
for y in range(0, TALL):
    for x in range(0, WIDE):
        image += '1' if (x,y) in result else '.'
    image += '\n'
print(image)
print(f"Christmas tree found! Seconds: {seconds}.")