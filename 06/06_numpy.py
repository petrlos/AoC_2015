#Advent of Code 2015: Day 6 - using numpy
import numpy
import re
from datetime import datetime
timeStart = datetime.now()

regCoords = re.compile(r"\d+,\d+")
with open("data.txt") as file:
    lines = file.read().splitlines()

gridTask1 = numpy.zeros((1000,1000))
gridTask2 = numpy.zeros((1000,1000))

for line in lines:
    numbers = regCoords.findall(line)
    topLeft = list(map(int, numbers[0].split(",")))
    bottomRight = list(map(int, numbers[1].split(",")))
    for row in range(topLeft[0], bottomRight[0]+1):
        for column in range(topLeft[1], bottomRight[1]+1):
            if "on" in line:
                gridTask1[row, column] = True
                gridTask2[row, column] += 1
            elif "off" in line:
                gridTask1[row, column] = False
                gridTask2[row, column] -= 1
                if gridTask2[row, column] < 0:
                    gridTask2[row, column] = 0
            elif "toggle" in line:
                gridTask1[row, column] = not gridTask1[row, column]
                gridTask2[row, column] += 2
print("Task 1:",gridTask1.sum())
print("Task 2:",gridTask2.sum())
print("Total runtime:", datetime.now() - timeStart)