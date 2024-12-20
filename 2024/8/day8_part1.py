from itertools import combinations

def is_valid(text, antena, position):
    x, y = position
    return 0 <= x < len(text) and 0 <= y < len(text[x]) and text[x][y] != antena

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read()

# Convert file into a grid
text = [list(line) for line in file.split('\n') if len(line) != 0]

# Find antenas
antenas = {}
for x in range(len(text)):
    for y in range(len(text[x])):
        if text[x][y] != '.':
            if text[x][y] not in antenas:
                antenas[text[x][y]] = []
            antenas[text[x][y]].append((x,y))

# Compute antinodes
antinodes = set()

for antena, positions in antenas.items():
    nodes = combinations(positions, 2)
    for node_a, node_b in nodes:
        # Extract points from node
        x1, y1 = node_a
        x2, y2 = node_b

        # Difference
        dx, dy = x2 - x1, y2 - y1

        # Calculate next points
        d1 = (x1 + dx, y1 + dy)
        d2 = (x1 - dx, y1 - dy)
        d3 = (x2 + dx, y2 + dy)
        d4 = (x2 - dx, y2 - dy)

        for position in [d1, d2, d3, d4]:
            if is_valid(text, antena, position):
                antinodes.add(position)
                if text[position[0]][position[1]] == '.':
                    text[position[0]][position[1]] = '#'

print('\n'.join(''.join(line) for line in text))
print(len(antinodes))