#Advent of Code 2015 - Day 14
import re
from reindeer import Reindeer

regNum = re.compile(r"\d+")
regName = re.compile(r"\w+")

#end = race time
end = 2503
with open("data.txt", "r") as file:
    lines = file.read().splitlines()

reindeers = []
for line in lines:
    numbers = regNum.findall(line)
    reindeer = Reindeer(regName.search(line).group(), numbers[0], numbers[1], numbers[2])
    reindeers.append(reindeer)

#Task1
task1 = []
for reindeer in reindeers:
    task1.append(reindeer.getDistanceInTime(end))
print("Task 1:",max(task1))

#Task2

for racetime in range(1,end+1):
    #vypocitej urazenou vzdalenost u kazdeho jednotliveho soba
    for reindeer in reindeers:
        reindeer.distance = reindeer.getDistanceInTime(racetime)
    #pokud vzdalenost je rovna dosud maximalni urazene vzdalenosti, pripocitej 1b
    for reindeer in reindeers:
        if reindeer.distance == max([reindeer.distance for reindeer in reindeers]):
            reindeer.points += 1

print("Task 2:",max([reindeer.points for reindeer in reindeers]))
