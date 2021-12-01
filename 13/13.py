#AoC 2015 - Day 13
import re, itertools, datetime
start = datetime.datetime.now()

def task1task2():
    permutator = list(itertools.permutations(list(nameDict.keys())))
    result = []
    for permutation in permutator:
        result.append(checkTableSetup(list(permutation)))
    return max(result)

def checkTableSetup(tableSetup):
    tableSetup.append(tableSetup[0])
    sum = 0
    for i in range(0,len(tableSetup)-1):
        checkRight = tableSetup[i] + ":" + tableSetup[i+1]
        checkLeft = tableSetup[i+1] + ":" + tableSetup[i]
        sum += happinessDict[checkLeft] + happinessDict[checkRight]
    return sum

with open("data.txt", "r") as file:
    data = file.read()
#cleanUP data: vymaze nepotrebne veci + nastavi format "JMENO cislo JMENO"
data = data.replace("would", "").replace(" gain ", "").replace(" lose ", "-")\
    .replace(".", "").replace("happiness units by sitting next to ","").upper()

#definice regexu
regexNames = re.compile(r"[A-Z]+")
regexHappiness = re.compile(r"-?\d+")

#vytvoreni dict - seznam jmen + seznam kombinaci s odpovidajici hapiness
nameDict, happinessDict = {}, {}
for line in data.split("\n"):
    name = regexNames.search(line).group()
    nameDict.setdefault(name, None)
    splitLine = line.split(" ")
    happinessDict.setdefault(splitLine[0] + ":" + splitLine[2], int(splitLine[1]))

task1 = task1task2()
print("Task 1:",task1)
print("Runtime:", datetime.datetime.now() - start)

#Task2 - do seznamu se prida self, ktery ma se vsemi interakci 0
self = "Self"
for name in nameDict.keys():
    newInputLeftRight = self + ":" + name
    newInputRightLeft = name + ":" + self
    happinessDict.setdefault(newInputLeftRight, 0)
    happinessDict.setdefault(newInputRightLeft, 0)
nameDict.setdefault("Self", None)

task2 = task1task2()
print("Task 2:",task2)
print("Runtime:", datetime.datetime.now() - start)