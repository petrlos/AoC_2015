#Advent of Code 2015: Day 7
from pprint import pprint as pp

def getTwoNumbers(what):
    numbers = [0, 0]
    for i in range(0, 2):
        if what[i].isdigit():
            numbers[i] = int(what[i])
        else:
            if what[i] not in wires.keys():
                runThrougInstructions(what[i])
            numbers[i] = int(wires[what[i]])
    return numbers

def runThrougInstructions(key):
    for line in lines:
        instructions = line.split(":")
        if instructions[1] == key:
            if "AND" in instructions[0]:
                numbers = getTwoNumbers(instructions[0].split(" AND "))
                result = numbers[0] & numbers[1]
                wires.setdefault(key, result)
            elif "OR" in instructions[0]:
                numbers = getTwoNumbers(instructions[0].split(" OR "))
                result = numbers[0] | numbers[1]
                wires.setdefault(key, result)
            elif "LSHIFT" in instructions[0]:
                numbers = getTwoNumbers(instructions[0].split(" LSHIFT "))
                result = numbers[0] << numbers[1]
                wires.setdefault(key, result)
            elif "RSHIFT" in instructions[0]:
                numbers = getTwoNumbers(instructions[0].split(" RSHIFT "))
                result = numbers[0] >> numbers[1]
                wires.setdefault(key, result)
            elif "NOT" in instructions[0]:
                input = "1 " + instructions[0]
                numbers = getTwoNumbers(input.split(" NOT "))
                result = 65535 - numbers[1]
                wires.setdefault(key, result)
            elif instructions[0].isdigit():
                wires.setdefault(instructions[1], int(instructions[0]))
            else:
                runThrougInstructions(instructions[0])
                wires.setdefault(instructions[1], int(wires[instructions[0]]))

#MAIN
with open("data.txt", "r") as file:
    lines = file.read().replace(" -> ", ":").splitlines()

wires = {}
runThrougInstructions("a")
print("Task1:",wires["a"])

#Task 2 - take signal "a" from task1 and run program again for wire "a"
wires = {"b": wires["a"]}
runThrougInstructions("a")
print("Task2:",wires["a"])