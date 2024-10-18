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

def isOnBoard(tile):
    return tile.row >= 0 and tile.row < height and tile.column >= 0 and tile.column < length

def inspect(tile):
    # check if the tile is on the board
    if isOnBoard(tile) == True:
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

#removed while True and break for testing
#while True:
row = int(input("Row:"))
column = int(input("Column:"))
if grid[row][column] == 1:
    print("mine hit")
    #break
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

# Return a Tile to click next




flagGrid = [[0 for i in range(length)] for j in range(height)]

# check if a tile is covered and add them to a list
def checkCover(covered, tile):
    if isOnBoard(tile) == True:
        if userGrid[tile.row][tile.column] == 9:
            covered.append(tile)

def markFlag(tile):
    covered = []
    tileUp = Tile(tile.row - 1, tile.column)
    checkCover(covered, tileUp)
    tileDown = Tile(tile.row + 1, tile.column)
    checkCover(covered, tileDown)
    tileLeft = Tile(tile.row, tile.column - 1)
    checkCover(covered, tileLeft)
    tileRight = Tile(tile.row, tile.column + 1)
    checkCover(covered, tileRight)
    tileDiag1 = Tile(tile.row - 1, tile.column -1)
    checkCover(covered, tileDiag1)
    tileDiag2 = Tile(tile.row + 1, tile.column +1)
    checkCover(covered, tileDiag2)
    tileDiag3 = Tile(tile.row + 1, tile.column - 1)
    checkCover(covered, tileDiag3)
    tileDiag4 = Tile(tile.row - 1, tile.column + 1)
    checkCover(covered, tileDiag4)
    #if the amount covered neighboring mines is equal to the displayed number on the tile,
    #all covered tiles are mines, so we flag them on a separate register.
    if userGrid[tile.row][tile.column] == len(covered):
        for t in covered:
            flagGrid[t.row][t.column] = 1

for x in range(height):
    for y in range(length):
        if userGrid[x][y] != 0 and userGrid[x][y] != 9:
            markFlag(Tile(x,y))

print("\n")
for row in flagGrid:
    print(row)    

def checkCoverAndFlag(covered, tile):
    if isOnBoard(tile) == True:
        if userGrid[tile.row][tile.column] == 9 and flagGrid[tile.row][tile.column] == 0:
            covered.append(tile)
    
def checkFlag(tile):
    covered = []
    tileUp = Tile(tile.row - 1, tile.column)
    checkCoverAndFlag(covered, tileUp)
    tileDown = Tile(tile.row + 1, tile.column)
    checkCoverAndFlag(covered, tileDown)
    tileLeft = Tile(tile.row, tile.column - 1)
    checkCoverAndFlag(covered, tileLeft)
    tileRight = Tile(tile.row, tile.column + 1)
    checkCoverAndFlag(covered, tileRight)
    tileDiag1 = Tile(tile.row - 1, tile.column -1)
    checkCoverAndFlag(covered, tileDiag1)
    tileDiag2 = Tile(tile.row + 1, tile.column +1)
    checkCoverAndFlag(covered, tileDiag2)
    tileDiag3 = Tile(tile.row + 1, tile.column - 1)
    checkCoverAndFlag(covered, tileDiag3)
    tileDiag4 = Tile(tile.row - 1, tile.column + 1)
    checkCoverAndFlag(covered, tileDiag4)
    flagCount = flagGrid[tileUp.row][tileUp.column] + flagGrid[tileDown.row][tileDown.column] + flagGrid[tileLeft.row][tileLeft.column] + flagGrid[tileRight.row][tileRight.column] + flagGrid[tileDiag1.row][tileDiag1.column] + flagGrid[tileDiag2.row][tileDiag2.column] + flagGrid[tileDiag3.row][tileDiag3.column] + flagGrid[tileDiag4.row][tileDiag4.column]
    if flagCount == userGrid[tile.row][tile.column]:
        print(covered)
    else:
        print("No clickable tiles.")

row2 = int(input("Row:"))
column2 = int(input("Column:"))
checkFlag(Tile(row2, column2))
        
