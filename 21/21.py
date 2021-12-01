#Advent of Code 2015 - Day 21
from itertools import combinations
from datetime import datetime
start = datetime.now()

class Fighter:
    def __init__(self, name, hp, stats):
        self.name = name
        self.hp = hp
        self.stats = stats
        self.price = stats[0]
        self.dmg = stats[1]
        self.armor = stats[2]
        self.win = False

    def __str__(self):
        return "{0}, {1}hp, {2}".format(self.name, self.hp, self.stats)

def fight(player, boss):
    while True:
        #player hits boss:
        boss.hp = boss.hp - (player.dmg - boss.armor)
        if boss.hp <= 0:
            player.win = True
            break
        #boss hits player:
        player.hp = player.hp - (boss.dmg - player.armor)
        if player.hp <= 0:
            break
    return player.win

#MAIN:
with open("data.txt", "r") as file:
    items = [line.split(" ") for line in file.read().splitlines()]

weapons, armors, rings = [], [], []
for item in items:
    if item[0] == "W":
        weapons.append(item)
    elif item[0] == "A":
        armors.append(item)
    elif item[0] == "R":
        rings.append(item)

#get all combinations for rings - one ring and two rings
ringComb = [com for sub in range(2) for com in combinations(rings, sub + 1)]

players = []
#no rings
for weapon in weapons:
    for armor in armors:
        equip = [0, 0, 0]
        for i in range(1, 4):
            equip[i - 1] += int(weapon[i]) + int(armor[i])
        newPlayer = Fighter("Player", 100, equip)
        players.append(newPlayer)
# 1-2 rings
for weapon in weapons:
    for armor in armors:
        for ring in ringComb:
            equip = [0, 0, 0]
            for i in range(1, 4):
                if len(ring) == 1:
                    equip[i-1] += int(weapon[i]) + int(armor[i]) + int(ring[0][i])
                if len(ring) == 2:
                    equip[i-1] += int(weapon[i]) + int(armor[i]) + int(ring[0][i]) + int(ring[1][i])
            #print(weapon, armor, ring, ": ", equip)
            newPlayer = Fighter("Player", 100, equip)
            players.append(newPlayer)

#Task1: min outcome to win
winners = []
#Task2: max outcome and still lose
loosers = []

#run all fights with all possible equipments
for player in players:
    boss = Fighter("Boss", 100, [0, 8, 2])
    player.win = fight(player, boss)
    if player.win:
        winners.append(player.price)
    if not player.win:
        loosers.append(player.price)

print("Task 1 - minimal outcome to win:", min(winners))
print("Task 2 - maximal outcome and still lose:",max(loosers))
print("Runtime:", datetime.now() - start)