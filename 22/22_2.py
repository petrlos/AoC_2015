# Advent of Code 2015: Day 22
import re
from collections import deque
from copy import deepcopy

class Game_state:
    def __init__(self, mage_HP, mage_MP, boss_HP, boss_DMG):
        self.mage_HP = mage_HP
        self.mage_MP = mage_MP
        self.boss_HP = boss_HP
        self.boss_DMG = boss_DMG
        self.shield_on = False
        self.MP_consumed = 0
        self.active_effects = deque()

    def __str__(self):
        effects = ""
        for effect in self.active_effects:
            effects += str(effect)
        return "Mage: {0} HP / {1} MP; Boss {2} HP / {3} DMG"\
            .format(self.mage_HP, self.mage_MP, self.boss_HP, self.boss_DMG) + "\n" + \
            "  {0}".format(effects) + "\n" + \
            "  Total MP Consumed: {0}".format(self.MP_consumed)

    @property
    def boss_dead(self):
        return self.boss_HP <= 0

    @property
    def mage_dead(self):
        return self.mage_HP <= 0

    @property
    def shield_bonus(self):
        return 7 if self.shield_on else 0

    def add_spell_to_effects(self, spell_name):
        atributes = spells[spell_name]
        if atributes["cost"] < self.mage_MP:
            if spell_name in ["magic_misile", "drain"]: #instant cast, no effect
                self.mage_MP -= atributes["cost"]
                self.MP_consumed += atributes["cost"]
                self.boss_HP -= atributes["dmg"]
                self.mage_HP += atributes["heal"]
                # print("  Mage casts: {0}, deals {1} dmg to Boss".format(spell_name, atributes["dmg"]))
            else:
                active_spell_names = [spell[0] for spell in self.active_effects]
                if spell_name not in active_spell_names:
                    #print("  Player casts ", spell_name)
                    self.active_effects.append((spell_name,atributes["max_time"]))
                    self.mage_MP -= atributes["cost"]
                    self.MP_consumed += atributes["cost"]

    def cast_effects(self):
        self.shield_on = False
        new_active_effects = []
        for spell_name, timer in self.active_effects:
            timer -= 1
            if spell_name == "shield":
                self.shield_on = True
                #print("Shield activated, timer remaining:", timer)
            elif spell_name == "poison":
                self.boss_HP -= spells[spell_name]["dmg"]
                #print("Boss been hit for 3HP via poison, timer remaining:", timer)
            elif spell_name == "recharge":
                self.mage_MP += spells[spell_name]["mana_recharge"]
                #print("101MP recharged, timer remaining:", timer)
            if timer > 0:
                new_active_effects.append((spell_name, timer))
        self.active_effects = deepcopy(new_active_effects)

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

def mage_attacks_boss(game):
    queue = deque([game])

    lowest_mana_consumed = 9999
    while queue:
        start_state = queue.popleft()
        for spell_name, atributes in spells.items():
            current_state = deepcopy(start_state)
            #player turn - apply effects
            current_state.cast_effects()
            #player turn - cast spell
            current_state.add_spell_to_effects(spell_name)
            #boss turn - apply effect
            current_state.cast_effects()
            if current_state.boss_dead:  # boss dead
                print(current_state.MP_consumed)
                if current_state.MP_consumed < lowest_mana_consumed:
                    lowest_mana_consumed = current_state.MP_consumed
                continue
            # boss attack:
            boss_hit = current_state.boss_DMG - current_state.shield_bonus
            current_state.mage_HP -= boss_hit
            if current_state.mage_dead:  # mage dead
                continue
            else:  # both live
                queue.append(deepcopy(current_state))
    return lowest_mana_consumed

# MAIN
with open("spells.txt") as file:
    lines = file.read().splitlines()

spells = define_spells(lines)
game_start = Game_state(50, 500, 51, 9) #mageHP, mageMP, bossHP, bossDMG

print(mage_attacks_boss(game_start))