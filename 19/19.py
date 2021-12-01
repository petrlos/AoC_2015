#Advent of Code 2015 Day 19
import re

def replaceNth(string, old, new, position):
    where = [m.start() for m in re.finditer(old, string)][position - 1]
    before = string[:where]
    after = string[where:]
    after = after.replace(old, new, 1)
    newString = before + after
    return newString

#MAIN:
with open("data.txt") as file:
    lines = file.read().splitlines()
startMolecule = lines[-1]

molecules = set()

#postupne prochazi instrukce a kdyz najde moznou zamenu, provede ji a novou molekulu prida
#do setu. nahrazuje se vzdy jenom 1x, podle indexu podle poctu vyskytu podretezce
for line in lines[:-2]:
    instruction = line.split(" => ")
    count = startMolecule.count(instruction[0])
    for i in range(count):
        newMolecule = replaceNth(startMolecule, instruction[0], instruction[1], i+1)
        molecules.add(newMolecule)
print("Task 1:", len(molecules))

#prochazi instrukce a v pripade ze muze nahradit, nahradi. opakuje dokud nezustane pouze "e"
counter = 0
while startMolecule != "e":
    for line in lines[:-2]:
        instruction = line.split(" => ")
        if instruction[1] in startMolecule:
            startMolecule = startMolecule.replace(instruction[1], instruction[0], 1)
            counter += 1
print("Task 2:", counter)