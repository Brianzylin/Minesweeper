import random
from collections import deque

length = 9
height = 9
mines = 10
#generate an empty board
grid = [[0 for i in range(length)] for j in range(height)]
userGrid = [[9 for i in range(length)] for j in range(height)]
#create all positions
positions = [(i,j) for i in range(height) for j in range(length)]
#determine mine locations
for i in range(mines):
    j = random.randint(i ,len(positions) - 1)
    positions[i], positions[j] = positions[j], positions[i]
    x,y = positions[i]
    grid[x][y] = 1

mineCountGrid = [[0 for i in range(length + 2)] for j in range(height + 2)]
for i in range(height):
    for j in range(length):
        mineCountGrid[i+1][j+1] = grid[i][j]

neighborMine = [[0 for i in range(length)] for j in range(height)]
for i in range(height):
    for j in range(length):
        neighborMine[i][j] = mineCountGrid[i + 1][j + 2] + mineCountGrid[i + 2][j + 2] + mineCountGrid[i + 2][j + 1] + mineCountGrid[i + 2][j] + mineCountGrid[i + 1][j] + mineCountGrid[i][j] + mineCountGrid[i][j + 1] + mineCountGrid[i][j + 2]

#print matrix
for row in grid:
    print(row)
print("\n")

#print matrix
for row in neighborMine:
    print(row)
print("\n")

class Tile:
  def __init__(self, row, column):
    self.row = row
    self.column = column

queue = deque()

def inspect(tile):
    # check if the tile is on the board
    isOnBoard = tile.row >= 0 and tile.row < height and tile.column >= 0 and tile.column < length
    if isOnBoard == True:
        hasNotBeenInspected = userGrid[tile.row][tile.column] == 9
        if hasNotBeenInspected:
            userGrid[tile.row][tile.column] = neighborMine[tile.row][tile.column]
            if userGrid[tile.row][tile.column] == 0:
                queue.append(tile)

def exploreNeighbors():
    tile = queue.pop()
    tileUp = Tile(tile.row - 1, tile.column)
    inspect(tileUp)
    tileDown = Tile(tile.row + 1, tile.column)
    inspect(tileDown)
    tileLeft = Tile(tile.row, tile.column - 1)
    inspect(tileLeft)
    tileRight = Tile(tile.row, tile.column + 1)
    inspect(tileRight)
    tileDiag1 = Tile(tile.row - 1, tile.column -1)
    inspect(tileDiag1)
    tileDiag2 = Tile(tile.row + 1, tile.column +1)
    inspect(tileDiag2)
    tileDiag3 = Tile(tile.row + 1, tile.column - 1)
    inspect(tileDiag3)
    tileDiag4 = Tile(tile.row - 1, tile.column + 1)
    inspect(tileDiag4)
    if len(queue) != 0:
        exploreNeighbors()

while True:
    row = int(input("Row:"))
    column = int(input("Column:"))
    if grid[row][column] == 1:
        print("mine hit")
        break
    else:
        userGrid[row][column] = neighborMine[row][column]
        if neighborMine[row][column] == 0:
            queue.append(Tile(row, column))
            exploreNeighbors()
    for row in userGrid:
        print(row)
    print("This round finishs.")





#print user input
for row in userGrid:
    print(row)



#print mine count grid
    
#Logic
#if neighboring mines amount = neighboring covered tiles all coivered tiles are mines
# if neighboring mines =  neighboring mines amount uncover rest of mines
#pattern recognition?


