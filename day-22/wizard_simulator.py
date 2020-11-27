from dataclasses import dataclass, field
from copy import deepcopy
from typing import List
import re, sys

input_file = 'day-22/input.txt'

@dataclass
class Spell:
  name: str
  cost: int
  damage: int
  armour: int
  hp: int
  mana: int
  ticks: int
  immediate: bool = True
@dataclass
class GameState:
  boss_hp: int
  boss_damage: int
  player_hp: int
  player_mana: int
  hard_mode: bool = False
  player_turn: bool = True
  mana_used: int = 0
  effects_list: List[Spell] = field(default_factory=list)


SPELLS = {
  'Missile': Spell('Magic Missile', 53, 4, 0, 0, 0, 0),
  'Drain': Spell('Drain', 73, 2, 0, 2, 0, 0, False),
  'Shield': Spell('Shield', 113, 0, 7, 0, 0, 6),
  'Poison': Spell('Poison', 173, 3, 0, 0, 0, 6, False),
  'Recharge': Spell('Recharge', 229, 0, 0, 0, 101, 5)
}

least_mana_used = sys.maxsize

def simulate(game_state, spell_history):
  global least_mana_used
  player_armour = 0

  new_gs = deepcopy(game_state)

  if new_gs.player_turn and new_gs.hard_mode:
    new_gs.player_hp -= 1
    if new_gs.player_hp <= 0:
      return False

  for effect in list(new_gs.effects_list):
      new_gs.boss_hp -= effect.damage
      player_armour += effect.armour
      new_gs.player_mana += effect.mana
      new_gs.player_hp += effect.hp
      effect.ticks -= 1
      if effect.ticks <= 0:
        new_gs.effects_list.remove(effect)

  if new_gs.boss_hp <= 0:
    least_mana_used = min(new_gs.mana_used, least_mana_used)
    print(str(least_mana_used) + ':' + ','.join(spell_history))
    return True

  if new_gs.mana_used >= least_mana_used:
    return False

  if new_gs.player_turn:
    new_gs.player_turn = False
    is_not_active = lambda spell: not any(spell.name == active.name for active in new_gs.effects_list)
    is_cheap = lambda spell: spell.cost <= new_gs.player_mana
    for spell in deepcopy([spell for spell in SPELLS.values() if is_not_active(spell) and is_cheap(spell)]):
      spell_gs = deepcopy(new_gs)
      spell_gs.player_mana -= spell.cost
      spell_gs.mana_used += spell.cost
      spell_gs.effects_list.append(spell)
      new_spell_history = list(spell_history)
      new_spell_history.append(spell.name)
      simulate(spell_gs, new_spell_history)
  else:
    new_gs.player_hp -= max(1, new_gs.boss_damage - player_armour)
    if new_gs.player_hp > 0:
      new_gs.player_turn = True
      simulate(new_gs, spell_history)

def simulate_fight(boss_hp, boss_damage, player_hp, player_mana, spell_list):
  # print(boss_hp, boss_damage, player_hp, player_mana, spell_list)
  effects_list = []
  player_armour = 0

  while len(spell_list) > 0:
    print(f'\n-- Player turn --')
    print(f'- Player has {player_hp} hit points, {player_armour} armour, {player_mana} mana --')
    print(f'- Boss has {boss_hp} hit points')
    # Process effects
    player_armour = 0
    for effect in list(effects_list):
      effect.ticks -= 1
      if effect.damage > 0:
        damage = effect.damage
        print(f"{effect.name} deals {damage} damage; its timer is now {effect.ticks}.")
        boss_hp -= damage
      if effect.armour > 0:
        armour = effect.armour
        print(f"{effect.name}'s timer is now {effect.ticks}.")
        player_armour += armour
      if effect.mana > 0:
        mana = effect.mana
        print(f"{effect.name} provides {mana} mana; its timer is now {effect.ticks}.")
        player_mana += mana
      if effect.ticks == 0:
        effects_list.remove(effect)

    if player_hp <=0:
      print(f"Player dies.")
      return False
    if boss_hp <= 0:
      print(f"Boss dies.")
      return True

    spell = SPELLS[spell_list.pop(0)]
    if spell.ticks > 0:
      if spell.name == 'Shield':
        print(f"Player casts Shield, increasing armour by 7.")
        player_armour += spell.armour
      else:
        print(f"Player casts {spell.name}.")
      effects_list.append(spell)
    else:
      if spell.name == 'Magic Missile':
        print(f"Player casts Magic Missile, dealing 4 damage.")
      elif spell.name == 'Drain':
        print(f"Player casts Drain, dealing 2 damage, and healing 2 hit points.")
      boss_hp -= spell.damage
      player_hp += spell.hp
    player_mana -= spell.cost

    if player_mana < 0:
      print(f"Player out of mana.")
      return False

    print(f'\n-- Boss turn --')
    print(f'- Player has {player_hp} hit points, {player_armour} armour, {player_mana} mana --')
    print(f'- Boss has {boss_hp} hit points')
    # Process effects
    player_armour = 0

    for effect in list(effects_list):
      effect.ticks -= 1
      if effect.damage > 0:
        damage = effect.damage
        print(f"{effect.name} deals {damage} damage; its timer is now {effect.ticks}.")
        boss_hp -= damage
      if effect.armour > 0:
        armour = effect.armour
        print(f"{effect.name}'s timer is now {effect.ticks}.")
        player_armour += armour
      if effect.mana > 0:
        mana = effect.mana
        print(f"{effect.name} provides {mana} mana; its timer is now {effect.ticks}.")
        player_mana += mana
      if effect.ticks == 0:
        print(f"{effect.name} wears off.")
        effects_list.remove(effect)

    if player_hp <=0:
      print(f"Player dies.")
      return False
    if boss_hp <= 0:
      print(f"Boss dies.")
      return True

    boss_damage = max(1, boss_damage - player_armour)
    player_hp -= boss_damage
    print(f'- Boss attacks for {boss_damage} damage')

    if player_hp <=0:
      print(f"Player dies.")
      return False
    if boss_hp <= 0:
      print(f"Boss dies.")
      return True

  print(f'\n-- Fight ends --')
  print(f'- Player has {player_hp} hit points, {player_armour} armour, {player_mana} mana --')
  print(f'- Boss has {boss_hp} hit points')
  return None

def part1(input, player_hp = 50, player_mana = 500):
  boss_hp, boss_damage = map(int, list(re.match(r"Hit Points: (\d+)\nDamage: (\d+)", input).groups()))
  simulate(GameState(boss_hp, boss_damage, player_hp, player_mana), [])
  return least_mana_used

def part2(input, player_hp = 50, player_mana = 500):
  boss_hp, boss_damage = map(int, list(re.match(r"Hit Points: (\d+)\nDamage: (\d+)", input).groups()))
  simulate(GameState(boss_hp, boss_damage, player_hp, player_mana, True), [])
  return least_mana_used

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))