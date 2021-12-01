#AoC 2015 - Day2
import math
def paperNeeded(size):
    size = [int(x) for x in size.split("x")]
    size.sort()
    return 3*size[0]*size[1] + 2*size[1]*size[2] + 2*size[2]*size[0]

def ribbonNeeded(size):
    size = [int(x) for x in size.split("x")]
    size.sort()
    return 2*size[0] + 2*size[1] + math.prod(size)

with open("data.txt", "r") as file:
    instructions = file.read().split("\n")

assert paperNeeded("2x3x4") == 58
assert paperNeeded("1x1x10") == 43
assert ribbonNeeded("2x3x4") == 34
assert ribbonNeeded("1x1x10") == 14

packpaper = []
ribbon = []
for present in instructions:
    packpaper.append(paperNeeded(present))
    ribbon.append(ribbonNeeded(present))

print("Task 1: {0}".format(sum(packpaper)))
print("Task 2: {0}".format(sum(ribbon)))
