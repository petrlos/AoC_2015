# Advent of Code 2015: Day 22
import re
from pprint import pprint

def define_spells(lines):
    reg_spell_name = re.compile(r"\w+")
    reg_num = re.compile(r"\d+")
    spells = {}
    parameters = "cost,dmg,heal,max_time,armor_bonus,mana_recharge".split(",")
    for line in lines:
        spell_name = reg_spell_name.search(line).group()
        numbers = list(map(int, reg_num.findall(line)))
        spells[spell_name] = dict(zip(parameters, numbers))
    return spells


# MAIN
with open("spells.txt") as file:
    lines = file.read().splitlines()

spells = define_spells(lines)

pprint(spells)