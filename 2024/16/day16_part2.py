from collections import deque

# Breadth-First Search (BFS)
def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # right, up, left, down

    best_rotations = float('inf')
    best_paths = []

    # Initialize queue: (current_position, path, current_direction_index, rotations)
    queue = deque([(start, [start], 0, 0)])

    # Keep track of visited cells with their rotations
    visited = {}

    while queue:
        (x, y), path, dir_index, rotations = queue.popleft()

        # Check if we've reached the end
        if (x, y) == end:
            if rotations < best_rotations:
                best_rotations = rotations
                best_paths = [path]

            elif rotations == best_rotations and len(path) <= min(len(i) for i in best_paths):
                best_paths.append(path)

            # Continue exploring other paths
            continue

        # Explore all possible moves
        for new_dir_index, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            # Ensure the move is within bounds and the cell is not a wall
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] in ['.', 'E']:
                # Calculate the number of rotations
                new_rotations = rotations + (1 if new_dir_index != dir_index else 0)

                # Only continue if this position is unvisited or has fewer rotations
                if (nx, ny, new_dir_index) not in visited or new_rotations <= visited[(nx, ny, new_dir_index)]:
                    visited[(nx, ny, new_dir_index)] = new_rotations
                    queue.append(((nx, ny), path + [(nx, ny)], new_dir_index, new_rotations))

    # No path found
    return set(item for sublist in best_paths for item in sublist)


# Import input.txt
with open("input.txt") as fopen:
    file = fopen.read().strip()

grid = [list(line) for line in file.split('\n')]

start = next(((x, y) for x, row in enumerate(grid) for y, char in enumerate(row) if char == 'S'), None)
end = next(((x, y) for x, row in enumerate(grid) for y, char in enumerate(row) if char == 'E'), None)

paths = shortest_path(grid, start, end)
if not paths:
    print("No path found")
else:
    for x, y in paths:
        grid[x][y] = 'O'

    print('\n'.join(''.join(row) for row in grid))
    print(len(paths))