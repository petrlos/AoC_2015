# Advent of Code 2015: Day 22
import re
from copy import deepcopy
from collections import deque
from datetime import datetime
time_start = datetime.now()

class Game_state:
    def __init__(self, mage_HP, mage_MP, boss_HP, boss_DMG):
        self.mage_HP = mage_HP
        self.mage_MP = mage_MP
        self.boss_HP = boss_HP
        self.boss_DMG = boss_DMG
        self.shield_on = False
        self.MP_consumed = 0
        self.active_effects = []
        self.spells_casted = []

    def __str__(self):
        return "Mage: {0} HP / {1} MP; Boss {2} HP / {3} DMG"\
            .format(self.mage_HP, self.mage_MP, self.boss_HP, self.boss_DMG) + "\n" + \
            "  {0}".format(", ".join(self.active_effects)) + "\n" + \
            "  Total MP Consumed: {0}".format(self.MP_consumed)

    @property
    def boss_dead(self):
        return self.boss_HP <= 0

    @property
    def mage_dead(self):
        if self.mage_HP <= 0:
            self.mage_HP = -100
            self.mage_MP = -100
        return self.mage_HP <= 0

    @property
    def shield_bonus(self): # if shield on
        return 7 if self.shield_on else 0

    def add_spell_to_effects(self, spell_name):
        self.active_effects += [spell_name]*spells[spell_name]["max_time"]

    def cast_effects(self): #cast current effects, after cast effect removed
        for effect in set(self.active_effects): #each effect only once
            self.boss_HP -= spells[effect]["dmg"]
            self.mage_MP += spells[effect]["mana_recharge"]
            self.active_effects.remove(effect)

    def mage_turn(self, spell_name):
        self.spells_casted.append("{0} {1}".format(spell_name,spells[spell_name]["cost"]))
        self.mage_MP -= spells[spell_name]["cost"]
        self.MP_consumed += spells[spell_name]["cost"]
        if spell_name in ["magic_misile", "drain"]:
            self.mage_HP += spells[spell_name]["heal"]
            self.boss_HP -= spells[spell_name]["dmg"]
        else:
            self.add_spell_to_effects(spell_name)

    def boss_turn(self):
        self.shield_on = "shield" in self.active_effects
        self.cast_effects()
        if not self.boss_dead:
            self.mage_HP -= (self.boss_DMG-self.shield_bonus)

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

def to_the_arms(game_start, hard_mode = False):
    game_queue = deque([game_start])
    result = [9999]

    while game_queue:
        current_state = game_queue.popleft()
        for spell_name in spells.keys():
            new_state = deepcopy(current_state)  # create new game state
            if hard_mode:
                new_state.mage_HP -= 1
            new_state.cast_effects()
            if spells[spell_name]["cost"] > new_state.mage_MP or \
                    spell_name in new_state.active_effects or \
                    new_state.mage_dead:
                continue #not enough MP, spell active or mage dead: not correct spell
            new_state.mage_turn(spell_name)
            if new_state.boss_dead:
                result.append(new_state.MP_consumed)
                continue
            new_state.boss_turn()  # if boss survives, may turn, casting effects at first
            if new_state.boss_dead and not new_state.mage_dead:
                result.append(new_state.MP_consumed)
                continue
            elif not new_state.mage_dead:  # if mage survives, add state to queue
                game_queue.append(new_state)
        if len(result) > 10: #tested empirically, enough results
            game_queue = []
    return min(result)

# MAIN
with open("spells.txt") as file:
    lines = file.read().splitlines()

spells = define_spells(lines)

game_start = Game_state(50, 500, 51, 9) #mageHP, mageMP, bossHP, bossDMG
#Task1
task1 = to_the_arms(game_start)
print("Task 1:", task1)

#Task2
task2 = to_the_arms(game_start, hard_mode=True)
print("Task 2:", task2)
print(datetime.now() - time_start)