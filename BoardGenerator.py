import random

length = 30
height = 16
mines = 99
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


#print matrix
for row in grid:
    print(row)

while True:
    row = int(input("Row:"))
    column = int(input("Column:"))
    if grid[row][column] == 1:
        print("mine hit")
        break
    else:
        userGrid[row][column] = grid[row][column + 1] + grid[row + 1][column + 1] + grid[row + 1][column] + grid[row + 1][column - 1] + grid[row][column - 1] + grid[row - 1][column -1] + grid[row - 1][column] + grid[row - 1][column + 1]
        print("mine not hit, try again:")
        for row in userGrid:
            print(row)
        print("Here are the mines")
        #print matrix
        for row in grid:
            print(row)
        print("This round finishs.")

#print user input
for row in userGrid:
    print(row)

#print mine count grid
    

