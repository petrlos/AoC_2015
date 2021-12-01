#AoC 2015 Day 3
import operator

def task1(input):
    houses = {}
    location = (0, 0)
    houses.setdefault(location)
    for char in input:
        location = tuple(map(operator.add, location, directions[char]))
        houses.setdefault(location)
    return len(houses.keys())

def task2(input):
    houses = {}
    locationSanta = (0,0)
    locationRobot = (0,0)
    santaDelivers = True
    houses.setdefault(locationSanta)
    for char in input:
        if santaDelivers:
            locationSanta = tuple(map(operator.add, locationSanta, directions[char]))
            houses.setdefault(locationSanta)
            santaDelivers = False
        else:
            locationRobot = tuple(map(operator.add, locationRobot, directions[char]))
            houses.setdefault(locationRobot)
            santaDelivers = True
    return len(houses.keys())

#MAIN:
directions = {"^": (0, 1), ">":(1,0), "v":(0,-1), "<":(-1, 0)}

with open("data.txt", "r") as file:
    input = file.readline()

print("Task 1: {0}".format(task1(input)))
print("Task 2: {0}".format(task2(input)))