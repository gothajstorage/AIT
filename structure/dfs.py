class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def dfs(maze, start, goal, path, visited):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    if start == goal:
        return path + [start]

    visited.add(start)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = start.x + dx, start.y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] is not None:
            next_pos = Position(nx, ny)
            if next_pos not in visited:
                result = dfs(maze, next_pos, goal, path + [start], visited)
                if result:
                    return result

    return []

rows, cols = 5, 5
maze = []

for i in range(rows):
    row = []
    for j in range(cols):
        if (i, j) == (0, 0):
            row.append(Position(i, j))
        elif (i, j) == (4, 4):
            row.append(Position(i, j))
        elif (i == 1 and j == 1) or (i == 1 and j == 3) or (i == 3 and j == 1) or (i == 3 and j == 2):
            row.append(None)
            row.append(Position(i, j))
    maze.append(row)

start = maze[0][0]
goal = maze[4][4]

path = dfs(maze, start, goal)
for p in path:
    print(f"({p.x}, {p.y})")
