import math


class PathFinder():
    def __init__(self, grid, startPos, endPos):
        self.grid = grid
        self.endPos = endPos

        self.position = startPos
    def move(self):
        closestPos = opened[0]
        closest = 99999999
        for i in range(0, 3):
            new = distance(opened[i], endPos)
            if new < closest:
                closest = new
                closestPos = opened[i]

        if set(grid[self.position.up()]) & set(visited[self.position.up()]) == False:
            opened.append(self.position.up())
        if set(grid[self.position.down()]) & set(visited[self.position.down()]) == False:
            opened.append(self.position.down())
        if set(grid[self.position.left()]) & set(visited[self.position.left()]) == False:
            opened.append(self.position.left())
        if set(grid[self.position.right()]) & set(visited[self.position.right()]) == False:
            opened.append(self.position.right())

        visited.append(self.position)

        print(self.position.getX() + " " + self.position.getY())

class Location:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
    def getX(self):
        return self.posX
    def getY(self):
        return self.posY
    def up(self):
        return [self.posX, self.posY - 1]
    def down(self):
        return [self.posX, self.posY + 1]
    def left(self):
        return [self.posX - 1, self.posY]
    def right(self):
        return [self.posX + 1, self.posY]

def distance(pos1, pos2):
    return math.hypot(pos1.getX() + pos2.getX(), pos1.getY() + pos2.getY())


visited = []
opened = []

grid = []

for x in range(0, 10):
    for y in range(0, 10):
        grid.append(Location(x, y))

startPos = Location(0, 0)
endPos = Location(10, 10)

pathFinder = PathFinder(grid, startPos, endPos)

while(pathFinder.position != endPos):
    pathFinder.move()

print("done" + pathFinder.position + " " + endPos.getX() + " " + endPos.getY())



