from collections import deque

# Breadth-First Search (BFS)
def shortest_path(grid, start, end):
    # Initialize queue: (current_position, path)
    queue = deque([(start, [start])])

    # Keep track of visited cells
    visited = {}

    while queue:
        (x, y), path = queue.popleft()

        # Check if we've reached the end
        if (x, y) == end:
            return visited

        # Explore all possible moves
        for (dx, dy) in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            nx, ny = x + dx, y + dy

            # Ensure the move is within bounds and the cell is not a wall
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] in 'SE.':
                # Only continue if this position is unvisited
                if (nx, ny) not in visited:
                    visited[(nx, ny)] = len(path)
                    queue.append(((nx, ny), path + [(nx, ny)]))

    # No path found
    return None

def get_neighbours(visited, position, unit_range):
    px, py = position
    neighbours = set()
    for dx in range(-unit_range, unit_range + 1):
        dy_max = unit_range - abs(dx)
        for dy in range(-dy_max, dy_max + 1):
            neighbour = (px + dx, py + dy)
            if neighbour in visited:
                neighbours.add(neighbour)
    return neighbours

def manhattan_distance(pos1, pos2):
    """Calculates the Manhattan distance between two coordinates."""
    return sum(abs(x - y) for x, y in zip(pos1, pos2))

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

grid = [list(line) for line in file.split('\n') if len(line) != 0]
start = next(((x, y) for x, row in enumerate(grid) for y, char in enumerate(row) if char == 'S'), None)
end = next(((x, y) for x, row in enumerate(grid) for y, char in enumerate(row) if char == 'E'), None)

visited = shortest_path(grid, start, end)
count = 0

for position in visited:
    neighbours = get_neighbours(visited, position, unit_range=20)
    for neighbour in neighbours:
        distance = manhattan_distance(position, neighbour)
        if visited[neighbour] - visited[position] - distance >= 100:
            count += 1

print(count)
