import datetime, re, itertools

inputFile = "test.txt"

start = datetime.datetime.now()
def newCombination(combination, where):
    if combination[where] == max:
        combination[where] = 0
        combination = newCombination(combination, where-1)
    combination[where] += 1
    return combination

max = 100
regEx = re.compile(r"(-?\d+)")

#ziska hodnoty
with open(inputFile, "r") as file:
    data = file.read().split("\n")
ingredients = []
for line in data:
    ingredient = [int(x) for x in regEx.findall(line)]
    ingredients.append(ingredient)

#vygenerovani vsech moznych kombinaci, abych jejich soucet byl 100
combinations = []
combination = [0] * len(ingredients)
maxComb = [max] * len(ingredients)
while combination != maxComb:
    combination = newCombination(combination, -1)
    if sum(combination) == max:
        combinations.append(combination*1)

print("Preparation ready, counting results..")

task1, task2 = 0, 0
for combination in combinations:
    lines = []
    for i in range(0,len(ingredients)):
        line = []
        for parameter in ingredients[i]:
            line.append(combination[i]*parameter)
        lines.append(line)
    lines = list(zip(*lines[::-1]))
    result = 1
    for i in range(0,len(lines)-1):
        suma = sum(lines[i])
        if suma < 0:
            suma = 0
        result *= suma
    if result > task1:
        task1 = result
    if sum(lines[4]) == 500:
        if result > task2:
            task2 = result

print("Task1: ", task1)
print("Task2: ", task2)

print(datetime.datetime.now()-start)