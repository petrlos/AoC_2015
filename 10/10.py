#AoC 2015 - Day 10:
import datetime
start = datetime.datetime.now()
def lookAndSay(input, counter):
    input = input + "#"
    output = ""
    for _ in range(0, counter):
        tryOut = ""
        for i in range(len(input)):
            if tryOut != "":
                if input[i] in tryOut:
                    tryOut += input[i]
                else:
                    output += str(len(tryOut)) + input[i - 1]
                    tryOut = "" + input[i]
            else:
                tryOut += input[i]
        input = output + "#"
        output = ""
    return len(input[:-1])

#MAIN
input = "3113322113"

task1 = lookAndSay(input, 40)
print("Task 1 lenght: {0}".format(task1))
task2 = lookAndSay(input, 50)
print("Task 2 lenght: {0}".format(task2))
print("Runtime: {0}".format(datetime.datetime.now() - start))