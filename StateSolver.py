userGrid = [[0, 1, 1, 9, 9, 9, 9, 9, 9],
[0, 1, 9, 9, 9, 9, 9, 9, 9],
[1, 1, 9, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 9, 9, 9, 9, 9, 9],
[9, 9, 9, 9, 9, 9, 9, 9, 9]]

print(userGrid)

height = len(userGrid)
length = len(userGrid[0])


flagGrid = [[0 for i in range(length)] for j in range(height)]
allClickableTiles = []

class Tile:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    def __str__(self):
        return "({}, {})".format(self.row, self.column)
    def __repr__(self):
       return "({}, {})".format(self.row, self.column)
    



# check if a tile is on board
def isOnBoard(tile):
   return tile.row >= 0 and tile.row < height and tile.column >= 0 and tile.column < length

# check if a tile is covered and add them to a list
def checkCover(covered, tile):
    if isOnBoard(tile) == True:
        if userGrid[tile.row][tile.column] == 9:
            covered.append(tile)

# check how many 9's for a single tile
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


# check if a tile is covered and not flagged
def checkCoverAndFlag(covered, tile):
    if isOnBoard(tile) == True:
        if userGrid[tile.row][tile.column] == 9 and flagGrid[tile.row][tile.column] == 0:
            covered.append(tile)

# add to count if tile is inbound
def addToCount(tile):
    if isOnBoard(tile) == True:
        return flagGrid[tile.row][tile.column]
    else:
        return 0

# check surrounding flags for each tile
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




'''nextTile = Tile(row,column)'''
#Solving using basic logic

    #mark neighboring flags for every tile
def useBasicLogic():
    for x in range(height):
        for y in range(height):
            if userGrid[x][y] != 0 and userGrid[x][y] != 9:
                markFlag(Tile(x,y))

    for x in range(height):
        for y in range(height):
            if userGrid[x][y] != 0 and userGrid[x][y] != 9:
                allClickableTiles.extend(checkFlag(Tile(x,y)))


 


def solveState():
    useBasicLogic()
    if len()

