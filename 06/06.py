import re, datetime
start = datetime.datetime.now()

def task1():
    lights = {}
    for counter, line in enumerate(data, start=1):
        if counter % 60 == 0:
            print("Task 1 done: {0}%".format(counter / 3))
        coords = [int(x) for x in regex.findall(line)]
        for i in range(coords[0], coords[2] + 1):
            for j in range(coords[1], coords[3] + 1):
                lights.setdefault((i, j), 0)
                if line[0] == "N":
                    lights[(i, j)] = True
                elif line[0] == "F":
                    lights[(i, j)] = False
                elif line[0] == "T":
                    if lights[(i, j)] == True:
                        lights[(i, j)] = False
                    else:
                        lights[(i, j)] = True
    return len(list(filter(lambda x: x, lights.values())))

def task2():
    lights = {}
    for counter, line in enumerate(data, start=1):
        if counter % 60 == 0:
            print("Task 2 done: {0}%".format(counter / 3))
        coords = [int(x) for x in regex.findall(line)]
        for i in range(coords[0], coords[2] + 1):
            for j in range(coords[1], coords[3] + 1):
                lights.setdefault((i, j), 0)
                if line[0] == "N":
                    lights[(i, j)] += 1
                elif line[0] == "F":
                    lights[(i, j)] -= 1
                    if lights[(i,j)] < 0:
                        lights[(i,j)] = 0
                elif line[0] == "T":
                    lights[(i, j)] += 2
    return sum(lights.values())

#MAIN:
with open("data.txt", "r") as file:
    # TOOGLE = T: prepni - to co sviti se zhasne a obracene
    # TURN ON = N: rozsviti vsechno
    # TURN OFF = F: zhasne vsechno
    data = file.read().replace(" through ", ":").replace("turn off ","F").\
        replace("turn on ","N").replace("toggle ", "T").split("\n")

#najde vsechny skupiny znaku obsahujici aspon jedno cislo a pouze cisla
regex = re.compile(r"\d+")

task1 = task1()
task2 = task2()

print("Task 1: {0}".format(task1))
print("Task 2: {0}".format(task2))
print("Runtime:", datetime.datetime.now()-start)