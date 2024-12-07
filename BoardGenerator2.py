import random
width = 9
height = 9
mines = 10

class Tile:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_mine = False  # Initially not a mine
        self.is_revealed = False
        #self.is_flagged = False
        self.neighboring_mines = 0  # Number of neighboring mines
    
    def __repr__(self):
        m = str(int(self.is_mine)) 
        n = str(self.neighboring_mines)
        r = str(int(self.is_revealed)) 
        return "({}, {}, {})".format(m, n, r)


grid = [[Tile(row, col) for col in range(width)] for row in range(height)]

#distribute mines on board
positions = [(i,j) for i in range(height) for j in range(width)]

for i in range(mines):
    j = random.randint(i ,len(positions) - 1)
    positions[i], positions[j] = positions[j], positions[i]
    x,y = positions[i]
    grid[x][y].is_mine = True

#check if on board
outofGridTile = Tile(-1, -1)
def getTile(row, col):
    if row >= 0 and row < height and col >= 0 and col < width:
        return grid[row][col]
    else:
        return outofGridTile

def checkMine(row, col):
    currentTile = getTile(row, col)
    if (currentTile != outofGridTile and currentTile.is_mine == True):
        return 1
    else:
        return 0

#Neighboring mine count

def neighbors(tile):
    count = 0
    count += checkMine(tile.row + 1, tile.col + 1)
    count += checkMine(tile.row + 1, tile.col)
    count += checkMine(tile.row + 1, tile.col - 1)
    count += checkMine(tile.row, tile.col + 1)
    count += checkMine(tile.row, tile.col - 1)
    count += checkMine(tile.row - 1, tile.col + 1)
    count += checkMine(tile.row - 1, tile.col)
    count += checkMine(tile.row - 1, tile.col - 1)
    tile.neighboring_mines = count

for i in range (0,height):
    for j in range(0,width):
        neighbors(grid[i][j])

def printMatrix(matrix):
    for row in matrix:
        print(row)
    print("\n")


printMatrix(grid)






