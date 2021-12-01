#AoC 2015 - Day 9
import re, itertools, datetime
def switchNodesInRoute(route):
    backup = route.split(":")
    return backup[1] + ":" + backup[0]

def checkDistance(order):
    sum = 0
    for i in range(0,len(order)-1):
        route = order[i] + ":" + order[i+1]
        if route not in dictDest.keys():
            route = switchNodesInRoute(route) #kazda cesta existuje
            # pokud ji nanajde, je definovana v jinem poradi
        sum += int(dictDest[route])
    return sum

#MAIN
start = datetime.datetime.now()
with open("data.txt", "r") as file:
    data = file.read().replace(" to ", ":").replace(" ", "")

#definice regexu
regexStars = re.compile(r"\w+")
regexDest = re.compile(r"(\w+:\w+)")
regexDist = re.compile(r"(\d+)")

#vytvori dict cilu - dict zajisti, ze kazdy cil bude prave 1x
dictStars, dictDest = {}, {}
mo = regexStars.findall(data)
for item in mo:
    if item.isalpha():
        if item not in dictStars.keys():
            dictStars.setdefault(item, None)

#generovani dict vzdalenosti mezi cili
for item in data.split("\n"):
    destination = regexDest.search(item).group() #regex najde dvojici uzlu
    distance = regexDist.search(item).group() #regex najde odpovidaji vzdalenost
    dictDest.setdefault(destination, distance) #vytvori zaznam v dict

#vygeneruje vsechny permutace a proveri jejich vzdalenosti
permutator = list(itertools.permutations(list(dictStars.keys())))
distance = []
for permutation in permutator:
    distance.append(checkDistance(permutation))

print("Task 1 - shortest distance: {0}".format(min(distance)))
print("Task 2 - longest distance: {0}".format(max(distance)))
print("Runtime: {0}".format(datetime.datetime.now() - start))