from collections import deque

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        for dx, dy in directions:
            nx, ny = current.x + dx, current.y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] is not None:
                next_pos = Position(nx, ny)
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, path + [next_pos]))

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
        else:
            row.append(Position(i, j))
    maze.append(row)

start = maze[0][0]
goal = maze[4][4]

path = bfs(maze, start, goal)
for p in path:
    print(f"({p.x}, {p.y})")
