#AoC 2015 Day 16
import re

def checkAuntSueTask1(auntSue):
    for parameter in mfcsamDict.keys():
        if parameter in auntSue.keys():
            if mfcsamDict[parameter] != auntSue[parameter]:
                return False
    return True

def checkAuntSueTask2(auntSue):
    for parameter in mfcsamDict.keys():
        if parameter in auntSue.keys():
            if parameter == "trees" or parameter == "cats":
                if mfcsamDict[parameter] >= auntSue[parameter]:
                    return False
            elif parameter == "pomeranians" or parameter == "goldfish":
                if mfcsamDict[parameter] <= auntSue[parameter]:
                    return False
            else:
                if mfcsamDict[parameter] != auntSue[parameter]:
                    return False
    return True

with open("data.txt", "r") as file:
    auntsSue = file.read().split("\n")
with open("mfcsam.txt", "r") as file:
    mfcsam = file.read().split("\n")

#vytvori dict z mfcsam
mfcsamDict = {}
for line in mfcsam:
    parameter = re.compile(r"\w+").search(line).group()
    value = re.compile(r"\d+").search(line).group()
    mfcsamDict.setdefault(parameter, int(value))

line = "1: goldfish: 9, cars: 0, samoyeds: 9"
regexSue = re.compile(r"(\d*): (\w+): (\d*), (\w+): (\d+), (\w+): (\d+)")

for line in auntsSue:
#    line = "Sue 357: trees: 7, goldfish: 10, akitas: 0"
    littleDict = {}
    mo = regexSue.findall(line)
    for i in range(1,6,2):
        littleDict.setdefault(mo[0][i], int(mo[0][i+1]))
    if checkAuntSueTask1(littleDict):
        print("Task 1:",line)
    if checkAuntSueTask2(littleDict):
        print("Task 2:",line)
