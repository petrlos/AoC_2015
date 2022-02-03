#Advent of Code 2015: Day 5
def task1(word):
    if len(regForbiddenPair.findall(word)) > 0:
        return False
    if len(regMustHavePair.findall(word)) == 0:
        return False
    if len(regVowel.findall(word)) < 3:
        return False
    return True

import re

regForbiddenPair = re.compile(r"(xy|ab|cd|pq)")
regMustHavePair = re.compile(r"([a-z])\1")
regVowel = re.compile(r"[aeiou]")

with open("data.txt") as file:
    lines = file.read().splitlines()

counterTask1 = 0
for word in lines:
    if task1(word):
        counterTask1 += 1

print(counterTask1)
