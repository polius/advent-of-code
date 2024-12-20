from itertools import combinations

def traverse(text, node, difference, movement, antinodes):
    x, y = node
    dx, dy = difference

    if 0 <= x < len(text) and 0 <= y < len(text[x]):
        antinodes.add(node)
        text[x][y] = '#' if text[x][y] == '.' else text[x][y]
        if movement == 'up':
            new_node = (x - dx, y - dy)
        elif movement == 'down':
            new_node = (x + dx, y + dy)
        traverse(text, new_node, difference, movement, antinodes)

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
        difference = (x2 - x1, y2 - y1)

        # Traverse
        traverse(text, node_a, difference, 'up', antinodes)
        traverse(text, node_a, difference, 'down', antinodes)

# print('\n'.join(''.join(line) for line in text))
print(len(antinodes))