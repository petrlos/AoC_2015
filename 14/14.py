#AoC 2015 - Day 14
import re

def getDistanceTask1(data, end):
    speed = data[0]
    remainFlying = data[1]
    remainRest = data[2]
    flying = True
    distance = 0
    for i in range(0,end+1):
        if flying and remainFlying > 0:
            distance += speed
            remainFlying -= 1
        elif not flying and remainRest > 0:
            remainRest -= 1
        if remainRest == 0:
            remainRest = data[2]
            flying = True
        if remainFlying == 0:
            flying = False
            remainFlying = data[1]
    return distance

#MAIN
end = 1000

with open("test.txt", "r") as file:
    data = file.read().split("\n")

regex = re.compile(r"\d+")
regName = re.compile(r"\w+")

reindeers = []
for line in data:
    name = regName.search(line).group()
    reindeer = [int(x) for x in regex.findall(line)]
    reindeers.append(reindeer)

#Task1: spocita vzdalenost vsech sobiku v casu END
distance = []
for reindeer in reindeers:
    distance.append(getDistanceTask1(reindeer, end))
print("Task 1:",max(distance))

