import itertools, math

input_file = 'day-21/input.txt'

WEAPON_LIST = [
  {'name': 'Dagger', 'cost': 8, 'damage': 4, 'armour': 0},
  {'name': 'Shortsword', 'cost': 10, 'damage': 5, 'armour': 0},
  {'name': 'Warhammer', 'cost': 25, 'damage': 6, 'armour': 0},
  {'name': 'Longsword', 'cost': 40, 'damage': 7, 'armour': 0},
  {'name': 'Greataxe', 'cost': 74, 'damage': 8, 'armour': 0}
]

ARMOUR_LIST = [
  {'name': 'None', 'cost': 0, 'damage': 0, 'armour': 0},
  {'name': 'Leather', 'cost': 13, 'damage': 0, 'armour': 1},
  {'name': 'Chainmail', 'cost': 31, 'damage': 0, 'armour': 2},
  {'name': 'Splintmail', 'cost': 53, 'damage': 0, 'armour': 3},
  {'name': 'Bandedmail', 'cost': 75, 'damage': 0, 'armour': 4},
  {'name': 'Platemail', 'cost': 102, 'damage': 0, 'armour': 5}
]

RING_LIST = [
  {'name': 'None1', 'cost': 0, 'damage': 0, 'armour': 0},
  {'name': 'None2', 'cost': 0, 'damage': 0, 'armour': 0},
  {'name': 'Damage +1', 'cost': 25, 'damage': 1, 'armour': 0},
  {'name': 'Damage +2', 'cost': 50, 'damage': 2, 'armour': 0},
  {'name': 'Damage +3', 'cost': 100, 'damage': 3, 'armour': 0},
  {'name': 'Defence +1', 'cost': 20, 'damage': 0, 'armour': 1},
  {'name': 'Defence +2', 'cost': 40, 'damage': 0, 'armour': 2},
  {'name': 'Defence +3', 'cost': 80, 'damage': 0, 'armour': 3}
]

def get_sorted_upgrade_combos():
  # ring_combos = list(itertools.combinations(RING_LIST, 2))
  valid_upgrade_perms = [ perm for perm in itertools.product(WEAPON_LIST, ARMOUR_LIST, RING_LIST, RING_LIST) if perm[2]['name'] < perm[3]['name']]
  return sorted(valid_upgrade_perms, key=lambda perm: sum(item['cost'] for item in perm))

def is_win(player, boss):
  player_damage = max(1, player['damage'] - boss['armour'])
  boss_damage = max(1, boss['damage'] - player['armour'])

  player_hits_required = math.ceil(boss['hp'] / player_damage)
  boss_hits_required = math.ceil(player['hp'] / boss_damage)
  return player_hits_required <= boss_hits_required

BOSS_STATS = {'hp': 109, 'damage': 8, 'armour': 2}
PLAYER_BASE_STATS = {'name': 'player', 'hp': 100, 'damage': 0, 'armour': 0}
def do_upgrades_win(items):
  current_stats = dict(PLAYER_BASE_STATS)
  current_stats['damage'] = sum(item['damage'] for item in items)
  current_stats['armour'] = sum(item['armour'] for item in items)
  return is_win(current_stats, BOSS_STATS)

def part1(input):
    for items in get_sorted_upgrade_combos():
      if do_upgrades_win(items):
        return sum(item['cost'] for item in items)

def part2(input):
  for items in get_sorted_upgrade_combos()[::-1]:
    if not do_upgrades_win(items):
      return sum(item['cost'] for item in items)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))