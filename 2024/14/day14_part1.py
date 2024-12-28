import re
import math

# Define constraints
SECONDS = 100
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

result = {}
for robot in data:
    px, py = robot['p']
    vx, vy = robot['v']

    nx = (px + vx * SECONDS) % WIDE
    ny = (py + vy * SECONDS) % TALL

    final_position = (nx, ny)
    result[final_position] = result.get(final_position, 0) + 1

# Compute quadrants
quadrants = {"q1": 0, "q2": 0, "q3": 0, "q4": 0}
q1 = {"x": (0, math.floor(WIDE / 2) - 1), "y": (0, math.floor(TALL / 2) - 1)}
q2 = {"x": (0, math.floor(WIDE / 2) - 1), "y": (math.ceil(TALL / 2), TALL - 1)}
q3 = {"x": (math.ceil(WIDE / 2), WIDE - 1), "y": (0, math.floor(TALL / 2) - 1)}
q4 = {"x": (math.ceil(WIDE / 2), WIDE - 1), "y": (math.ceil(TALL / 2), TALL - 1)}

for k, v in result.items(): 
    x, y = k
    if q1['x'][0] <= x <= q1['x'][1] and q1['y'][0] <= y <= q1['y'][1]:
        quadrants['q1'] += v
    elif q2['x'][0] <= x <= q2['x'][1] and q2['y'][0] <= y <= q2['y'][1]:
        quadrants['q2'] += v
    elif q3['x'][0] <= x <= q3['x'][1] and q3['y'][0] <= y <= q3['y'][1]:
        quadrants['q3'] += v
    elif q4['x'][0] <= x <= q4['x'][1] and q4['y'][0] <= y <= q4['y'][1]:
        quadrants['q4'] += v

# Compute total
total = quadrants["q1"] * quadrants["q2"] * quadrants["q3"] * quadrants["q4"]
print(total)