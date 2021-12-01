#AoC 2015 - Day 20
from datetime import datetime
from functools import reduce

start = datetime.now()

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def task2vs2(house):
    return sum((filter(lambda x: house / x < 50, factors(house))))*11

minPresents = 36000000
houseNumber = 800000
presents = 0

print("The house with more than {0} presents: ".format(minPresents))

#Task1
while presents < minPresents / 10:
    houseNumber += 1
    presents = sum(factors(houseNumber))
print("Task 1:", houseNumber)
print(datetime.now()-start)

#Task2
houseNumber = 800000
presents = 0
while presents < minPresents:
    houseNumber += 1
    presents = task2vs2(houseNumber)

print("Task 2:", houseNumber)
print(datetime.now()-start)