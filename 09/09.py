#AoC 2015 - Day 9
import re, itertools, datetime
def switchNodesInRoute(route):
    backup = route.split(":")
    return backup[1] + ":" + backup[0]

def checkDistance(order):
    sum = 0
    for i in range(0,len(order)-1):
        route = dictStarTransfered[order[i]] + ":" + dictStarTransfered[order[i+1]]
        if route not in dictDest.keys():
            route = switchNodesInRoute(route)
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

#vytvori slovnik cilu, priradi jim index 1 az n
dictStars, dictDest = {}, {}
mo = regexStars.findall(data)
counter = 1
for item in mo:
    if item.isalpha():
        if item not in dictStars.keys():
            dictStars.setdefault(item, counter)
            counter += 1

#prohodi keys a values v seznamu uzlu, jednoduseji se potom hleda spravna cesta
dictStarTransfered = {}
for key in dictStars.keys():
    dictStarTransfered.setdefault(dictStars[key], key)

#generovani dict vzdalenosti mezi cili
for item in data.split("\n"):
    destination = regexDest.search(item).group() #regex najde dvojici uzlu
    distance = regexDist.search(item).group() #regex najde odpovidaji vzdalenost
    dictDest.setdefault(destination, distance) #vytvori zaznam v dict

#vygeneruje vsechny permutace a proveri jejich vzdalenosti
permutator = list(itertools.permutations(list(range(1,len(dictStars.keys())+1))))
distance = []
for permutation in permutator:
    distance.append(checkDistance(permutation))

print("Task 1 - shortest distance: {0}".format(min(distance)))
print("Task 2 - longest distance: {0}".format(max(distance)))
print("Runtime: {0}".format(datetime.datetime.now() - start))