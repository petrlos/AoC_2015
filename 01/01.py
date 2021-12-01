#Aoc 2015 - Day1
def getFloorNumber(instructions):
    return instructions.count("(") - instructions.count(")")

def getToBasement(instructions):
    level, result = 0, 0
    for position, char in enumerate(instructions):
        if char == "(":
            level += 1
        else:
            level -= 1
        if level == -1:
            result = position + 1
            break
    return result

with open("data.txt", "r") as file:
    data = file.readline()

print("Task 1: {0}".format(getFloorNumber(data)))
print("Task 2: {0}".format(getToBasement(data)))

assert getFloorNumber("(())") == 0
assert getFloorNumber("))(((((") == 3
assert getFloorNumber(")))") == -3
assert getToBasement("()())") == 5