#AoC Day 11 - Game of Life
xdef extendGrid(grid):
    # rozsirit mrizku o 1 bunku kazdym smerem - muzu pak projit vsechny sousedy
    # podle listu delta, nemusim se starat o delku retezce
    emptyRow = "x"*len(grid[0])
    newGrid = []
    newGrid.append("x" + emptyRow + "x")
    for line in grid:
        newGrid.append("x" + line + "x")
    newGrid.append("x" + emptyRow + "x")
    return newGrid

def task1(grid):
    #pocita jenom prime sousedy
    rows, cols = len(grid), len(grid[0])
    delta = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    grid = extendGrid(grid)
    newGrid = []
    for row in range(1,rows+1):
        newRow = ""
        for col in range(1, cols+1):
            neighbours = ""
            for deltax, deltay in delta:
                rowx = row + deltax
                coly = col + deltay
                neighbours += grid[rowx][coly]
            neighboursOccupied = neighbours.count("#")
            if grid[row][col] == "#" and (neighboursOccupied == 2 or neighboursOccupied == 3):
                newRow += "#"
            if grid[row][col] == "#" and not (neighboursOccupied == 2 or neighboursOccupied == 3):
                newRow += "."
            if grid[row][col] == "." and neighboursOccupied == 3:
                newRow += "#"
            if grid[row][col] == "." and not neighboursOccupied == 3:
                newRow += "."
        newGrid.append(newRow)
    return newGrid

def task2(grid):
    sliceGrid0 = grid[0]
    sliceGrid1 = grid[-1]
    grid[0] = "#" + sliceGrid0[1:-1] + "#"
    grid[-1] = "#" + sliceGrid1[1:-1] + "#"
    return grid

#MAIN
from datetime import datetime
start = datetime.now()
print("AoC - Day 11")

with open ("data.txt" , 'r') as f:
    startGrid = [line.rstrip() for line in f.readlines()]

#Task 1
grid = startGrid * 1
for steps in range(0,100):
    grid = task1(grid) * 1
counter = 0
for line in grid:
    counter += line.count("#")
print("Runtime: ",datetime.now() - start)
print("Task 1:", counter)

#Task 2: four corners are always on
grid = startGrid * 1
for steps in range(0,100):
    grid = task2(grid) * 1
    grid = task1(grid) * 1
grid = task2(grid) * 1
counter = 0
for line in grid:
    counter += line.count("#")
print("Runtime: ",datetime.now() - start)
print("Task 2:", counter)
