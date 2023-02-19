# Advent of Code 2015: Day 22
import re
from random import randint
from copy import deepcopy

#TODO: damaged, don't know why, not working, see version 22_2.py

# MAIN
regSpellName = re.compile(r"\w+")
regNum = re.compile(r"\d+")

with open("spells.txt", "r") as file:
    lines = file.read().splitlines()

spellsSetup = {}
parameters = "timer,cost,dmg,heal,maxTime,armorBonus,manaRecharge".split(",")
for line in lines:
    helpDict = {}
    spellName = regSpellName.search(line).group()
    numbers = [int(x) for x in regNum.findall(line)]
    for i, parameter in enumerate(parameters):
        helpDict.setdefault(parameter, numbers[i])
    helpDictDeepCopy = deepcopy(helpDict)
    spellsSetup.setdefault(spellName, helpDictDeepCopy)

spellNames = list(spellsSetup.keys())
manaConsumedList = []

for i in range(100):  # perform i games, find the one with least MP consumed
    playerHP = 50
    playerMP = 501
    bossHP = 51
    bossAttack = 9
    manaConsumed = 0
    playerWins = False
    spells = deepcopy(spellsSetup)
    task2dead = False

    while True:  # out if: player dead/boss dead
        playerHP = playerHP - 1
        if playerHP == 0:
            task2dead = True

        # find spell without effect
        if not task2dead:
            while True:  # out if: found spell with timer == 0
                spellName = spellNames[randint(0, len(spells.keys()) - 1)]
                if spells[spellName]["timer"] == 0 and playerMP > spells[spellName]["cost"]:
                    spells[spellName]["timer"] = spells[spellName]["maxTime"]
                    playerMP -= spells[spellName]["cost"]
                    manaConsumed += spells[spellName]["cost"]
                    break
                #with MP under 53 cant cast any spell
                elif playerMP < 53:
                    break

            # PLAYER TURN
            # go through all spells, active spells cast their effect - casted spells don't get effect
            for key in spellNames:
                activeSpell = spells[key]
                if activeSpell["timer"] > 0 and spellName not in ["poison", "recharge"]:
                    activeSpell["timer"] -= 1
                    bossHP -= activeSpell["dmg"]
                    playerHP += activeSpell["heal"]
                    playerMP += activeSpell["manaRecharge"]

            # BOSS TURN:
            # again go through all spells
            for key in spellNames:
                activeSpell = spells[key]
                if activeSpell["timer"] > 0:
                    activeSpell["timer"] -= 1
                    bossHP -= activeSpell["dmg"]
                    playerHP += activeSpell["heal"]
                    playerMP += activeSpell["manaRecharge"]
            if bossHP <= 0:
                playerWins = True
                break
            # BOSS attack
            if spells["shield"]["timer"] > 0:
                armorBonus = spells["shield"]["armorBonus"]
            else:
                armorBonus = 0
            playerHP = playerHP - (bossAttack - armorBonus)
        if playerHP <= 0:
            break
    if playerWins:
        manaConsumedList.append(manaConsumed)

print("Lowest MP Consum:", min(manaConsumedList))
