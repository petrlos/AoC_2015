#AoC 2015 - Day 24
from itertools import permutations
import math, datetime

def findOptimalConfiguration(data, groupCount):
    groupWeight = sum(data) / groupCount
    luggageCount = 0
    while True:
        luggageCount += 1
        perm = list(filter(lambda x: sum(x) == groupWeight, permutations(data, luggageCount)))
        if len(perm) > 0:
            break

    products = []
    for combination in perm:
        products.append(math.prod(combination))
    return min(products)

#MAIN:
start = datetime.datetime.now()
with open("data.txt", "r") as file:
    data = [int(x) for x in file.read().split("\n")]

#Task 1: 3 Groups with same weight
print("Task 1:", findOptimalConfiguration(data, 3))
print("Runtime:", datetime.datetime.now() - start)
#Task 2: 4 Groups with same weight
print("Task 2:", findOptimalConfiguration(data, 4))
print("Runtime:", datetime.datetime.now() - start)
