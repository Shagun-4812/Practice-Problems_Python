from collections import deque

def shortest_path(building, start, target):
    rows, cols = len(building), len(building[0])
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions: Right, Down, Left, Up
    queue = deque([(start[0], start[1], 0, [])])  # (row, col, steps, path)
    visited = {start}

    while queue:
        x, y, steps, path = queue.popleft()

        if (x, y) == target:  # Target found
            path.append((x, y))
            display_path(building, path)
            return f"Path found in {steps} steps: {path}"

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and building[nx][ny] != 1 and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1, path + [(x, y)]))
                visited.add((nx, ny))

    return "No path to target!"

def display_path(building, path):
    grid = [row[:] for row in building]
    for x, y in path:
        grid[x][y] = '*'
    for row in grid:
        print(' '.join(str(cell) for cell in row))

# Example usage
building = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
    ['S', 0, 0, 'T', 1]
]

start, target = None, None
for i in range(len(building)):
    for j in range(len(building[0])):
        if building[i][j] == 'S':
            start = (i, j)
            building[i][j] = 0
        elif building[i][j] == 'T':
            target = (i, j)
            building[i][j] = 0

if start and target:
    print(shortest_path(building, start, target))
else:
    print("Start or target not found!")