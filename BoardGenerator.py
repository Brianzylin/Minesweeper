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

def printMatrix(matrix):
    for row in matrix:
        print(row)
    print("\n")
#print matrix
printMatrix(grid)

#print matrix
printMatrix(neighborMine)

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


def checkTile(tile):
    print("Checking ", tile.row, " ", tile.column)
    if grid[tile.row][tile.column] == 1:
        print("mine hit")
        return False
    else:
        userGrid[tile.row][tile.column] = neighborMine[tile.row][tile.column]
        if neighborMine[tile.row][tile.column] == 0:
            queue.append(Tile(row, column))
            exploreNeighbors()
        print("This round finishs.")
        return True

#print user input
printMatrix(userGrid)



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



def checkCoverAndFlag(covered, tile):
    if isOnBoard(tile) == True:
        if userGrid[tile.row][tile.column] == 9 and flagGrid[tile.row][tile.column] == 0:
            covered.append(tile)

def addToCount(tile):
    if isOnBoard(tile) == True:
        return flagGrid[tile.row][tile.column]
    else:
        return 0

def checkFlag(tile):
    count = 0
    covered = []
    tileUp = Tile(tile.row - 1, tile.column)
    checkCoverAndFlag(covered, tileUp)
    count += addToCount(tileUp)
    tileDown = Tile(tile.row + 1, tile.column)
    checkCoverAndFlag(covered, tileDown)
    count += addToCount(tileDown)
    tileLeft = Tile(tile.row, tile.column - 1)
    checkCoverAndFlag(covered, tileLeft)
    count += addToCount(tileLeft)
    tileRight = Tile(tile.row, tile.column + 1)
    checkCoverAndFlag(covered, tileRight)
    count += addToCount(tileRight)
    tileDiag1 = Tile(tile.row - 1, tile.column -1)
    checkCoverAndFlag(covered, tileDiag1)
    count += addToCount(tileDiag1)
    tileDiag2 = Tile(tile.row + 1, tile.column +1)
    checkCoverAndFlag(covered, tileDiag2)
    count += addToCount(tileDiag2)
    tileDiag3 = Tile(tile.row + 1, tile.column - 1)
    checkCoverAndFlag(covered, tileDiag3)
    count += addToCount(tileDiag3)
    tileDiag4 = Tile(tile.row - 1, tile.column + 1)
    checkCoverAndFlag(covered, tileDiag4)
    count += addToCount(tileDiag4)
    if count == userGrid[tile.row][tile.column]:
        return covered
    else:
        return []

# Progream starts
#First tile uncovered
row = int(input("Row:"))
column = int(input("Column:"))

nextTile = Tile(row,column)
while checkTile(nextTile) == True:
    #mark neighboring flags for every tile
    for x in range(height):
        for y in range(height):
            if userGrid[x][y] != 0 and userGrid[x][y] != 9:
                markFlag(Tile(x,y))
    allClickableTiles = []
    for x in range(height):
        for y in range(height):
            if userGrid[x][y] != 0 and userGrid[x][y] != 9:
                allClickableTiles.extend(checkFlag(Tile(x,y)))
    if len(allClickableTiles) > 0:
        nextTile = allClickableTiles.pop()
    else:
        print("No more tiles to uncover")
        break

printMatrix(userGrid)
#compare mines to flags
printMatrix(flagGrid)
printMatrix(grid)