#AoC 2015 -  Day 5
import re

def task1(input):
    def checkTwoLetter(input):
        result = False
        for index in range(1, len(input)):
            if input[index] == input[index - 1]:
                result = True
        return result

    def checkVowels(input):
        counter = 0
        for char in "aeiou":
            counter += input.count(char)
        return counter >= 3

    def checkNaughtyGroup(input):
        result = True
        group = "ab,cd,pq,xy".split(",")
        for naughty in group:
            if naughty in input:
                result = False
        return result

    return checkTwoLetter(input) and checkVowels(input) and checkNaughtyGroup(input)

def task2(input):
    def twoPairs(input):
        result = True
        dup_pair_re = re.compile(r"(..).*\1")
        mo = dup_pair_re.search(input)
        if mo == None:
            result = False
        return result

    def oneLetterInBetween(input):
        result = False
        for index in range(2, len(input)):
            if input[index] == input[index-2]:
                result = True
        return result

    return twoPairs(input) and oneLetterInBetween(input)

#MAIN:
checkTask1 = ["ugknbfddgicrmopn", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
checkTask2 = "qjhvhtzxzqqjkmpb,xxyxx,uurcxstgmygtbstg,ieodomkazucvgmuy".split(",")

with open("data.txt", "r") as file:
    inputData = file.read().split("\n")

counter = [0, 0]
for line in inputData:
    if task1(line):
        counter[0] += 1
    if task2(line):
        counter[1] += 1

for task, count in enumerate(counter, start=1):
    print("Task {0}: {1}".format(task, count))

