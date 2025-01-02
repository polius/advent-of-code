from collections import deque

# Breadth-First Search (BFS)
def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # right, up, left, down

    # Initialize queue: (current_position, path)
    queue = deque([(start, [start])])

    # Keep track of visited cells with their rotations
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        # Check if we've reached the end
        if (x, y) == end:
            return path

        # Explore all possible moves
        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy

            # Ensure the move is within bounds and the cell is not a wall
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.':

                # Only continue if this position is unvisited
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))

    # No path found
    return None

# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

grid = [['.'] * 71 for _ in range(71)]

for i, line in enumerate(file.split('\n')):
    if i == 1024:
        break
    x, y = map(int,line.split(','))
    grid[y][x] = '#'

start = (0, 0)
end = (70, 70)

path = shortest_path(grid, start, end)

if not path:
    print("No path found")
else:
    print("Path length:", len(path) - 1)
