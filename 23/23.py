#AoC 2015 - Day 23
import datetime
start = datetime.datetime.now()

def runInstructions(dictValues):
    currentLine = 0
    while True:
        instructions = data[currentLine].replace(",", "").split(" ")
        if instructions[0] == "hlf":
            # half current value
            dictValues[instructions[1]] = dictValues[instructions[1]] / 2
            currentLine += 1
        elif instructions[0] == "tpl":
            # tripple
            dictValues[instructions[1]] = dictValues[instructions[1]] * 3
            currentLine += 1
        elif instructions[0] == "inc":
            # +1
            dictValues[instructions[1]] = dictValues[instructions[1]] + 1
            currentLine += 1
        elif instructions[0] == "jmp":
            # jump by offset
            offset = int(instructions[1])
            currentLine += offset
        elif instructions[0] == "jie":
            # jump if even by offset
            currentRegister = instructions[1]
            if dictValues[currentRegister] % 2 == 0:
                currentLine += int(instructions[2])
            else:
                currentLine += 1
        elif instructions[0] == "jio":
            # jump if one by offset
            currentRegister = instructions[1]
            if dictValues[currentRegister] == 1:
                currentLine += int(instructions[2])
            else:
                currentLine += 1
        else:
            print("Instruction not found")
        if currentLine > len(data) - 1:
            break
    return dictValues["b"]

with open("data.txt", "r") as file:
    data = file.read().split("\n")

dictValues = {"a" : 0, "b": 0}
print("Task 1:", runInstructions(dictValues))
dictValues = {"a" : 1, "b": 0}
print("Task 2:", runInstructions(dictValues))
print("Runtime: ", datetime.datetime.now() - start)