#Aoc 2015 - Day 8

with open("data.txt", "r") as file:
    lines = file.read().splitlines()

literals = 0
memory = 0
for lineIndex, line in enumerate(lines):
    index = 0
    memory += len(line)
    while index < len(line):
        if line[index] == "\"":
            index += 1
        elif line[index].isalpha():
            literals += 1
            index += 1
        elif line[index] =="\\":
            if line[index+1] == "x":
                index += 4
                literals += 1
            elif line[index+1]== "\"" or line[index+1] == "\\":
                index += 2
                literals += 1
print("Task 1:",memory - literals)

result = 0
for line in lines:
    newLine = "\"" + line.replace("\\", "\\\\").replace("\"", "\\\"") + "\""
    result += (len(newLine) - len(line))

print("Task 2:",result)