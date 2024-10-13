import random

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

#for row in mineCountGrid:
#    print(row)
#print("\n")

for row in neighborMine:
    print(row)
print("\n")

while True:
    row = int(input("Row:"))
    column = int(input("Column:"))
    if grid[row][column] == 1:
        print("mine hit")
        break
    else:
        userGrid[row][column] = neighborMine[row][column]
    for row in userGrid:
        print(row)
    print("This round finishs.")

#print user input
for row in userGrid:
    print(row)

#print mine count grid
    

