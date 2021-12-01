#AoC 2015 - Day 25
from datetime import datetime as d
start = d.now()
firstNumber = 20151125

row = 2981
col = 3075

def nextNumber(number):
    number = number * 252533
    return number % 33554393

target = (sum(range(1,row+col-1)) + col)
print("Target iteration:",target)

number = firstNumber
for i in range(0,target-1):
    number = nextNumber(number)

print("Result:",number)
print("Runtime:", d.now() - start)