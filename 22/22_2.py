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
        return (self.mage_HP <= 0) or (self.mage_MP < 53)

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
        self.cast_effects()
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

def to_the_arms(game_start):
    game_queue = deque([game_start])
    result = 9999

    while game_queue:
        current_state = game_queue.popleft()
        possible_spells = set(spells.keys()) - set(current_state.active_effects)
        for spell_name in list(possible_spells):
            if spells[spell_name]["cost"] > current_state.mage_MP:
                possible_spells.discard(spell_name)
        if current_state.MP_consumed > result:
            possible_spells = []
        for spell_name in possible_spells:
            new_state = deepcopy(current_state)  # create new game state
            new_state.mage_turn(spell_name)  # mage turn inkl. casting effects
            if new_state.boss_dead:
                result = new_state.MP_consumed
                print(result, new_state.spells_casted)
                continue
            new_state.boss_turn()  # if boss survives, may turn, casting effects at first
            if new_state.boss_dead:
                result = new_state.MP_consumed
                print(result, new_state.spells_casted)
                continue
            elif not new_state.mage_dead:  # if mage survives, add state to queue
                game_queue.append(new_state)
    return result

# MAIN
with open("spells.txt") as file:
    lines = file.read().splitlines()

spells = define_spells(lines)

game_start = Game_state(50, 500, 51, 9) #mageHP, mageMP, bossHP, bossDMG

result = to_the_arms(game_start)
print(result)
print(datetime.now() - time_start)