#Advent of Code 2017: Day 7 - Vs. 2
from datetime import datetime
timeStart = datetime.now()

def decodeNumber(number):
    if number.isalpha():
        if number not in wires.keys():
            performInstruction(number) #key not yet found
        return wires[number]
    else:
        return int(number)

def performInstruction(key):
    for line in lines:
        left, right = line.split(" -> ")
        if right == key:
            if left.isnumeric(): #parametr left is number
                wires[key] = decodeNumber(left)
            elif "AND" in left:
                first, second = left.split(" AND ")
                wires[key] = decodeNumber(first) & decodeNumber(second)
            elif "OR" in left:
                first, second = left.split(" OR ")
                wires[key] = decodeNumber(first) | decodeNumber(second)
            elif "LSHIFT" in left:
                first, second = left.split(" LSHIFT ")
                wires[key] = decodeNumber(first) << decodeNumber(second)
            elif "RSHIFT" in left:
                first, second = left.split(" RSHIFT ")
                wires[key] = decodeNumber(first) >> decodeNumber(second)
            elif "NOT" in left:
                first = left[4:]
                wires[key] = 65535 - decodeNumber(first)
            else: #parameter left NOT number and NOT bitwise
                wires[key] = decodeNumber(left)

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

wires = dict()

#Task1:
performInstruction("a")
print("Task 1:", wires["a"])

#Task2:
wires = {"b": wires["a"]}
performInstruction("a")
print("Task 2:", wires["a"])
print("Total runtime:", datetime.now() - timeStart)