import rpg_simulator
import fileinput

BOSS_STATS = {'name': 'boss', 'hp': 109, 'damage': 8, 'armour': 2}
EXAMPLE_BOSS_STATS = {'name': 'boss', 'hp': 12, 'damage': 7, 'armour': 2}

def test_should_win_example_1():
  player_stats = {'name': 'player', 'hp': 8, 'damage': 5, 'armour': 5}
  assert rpg_simulator.is_win(player_stats, EXAMPLE_BOSS_STATS) == True

def test_should_win_example_2():
  player_stats = {'name': 'player', 'hp': 8, 'damage': 4, 'armour': 5}
  assert rpg_simulator.is_win(player_stats, EXAMPLE_BOSS_STATS) == False

def test_should_win_example_3():
  player_stats = {'name': 'player', 'hp': 100, 'damage': 7, 'armour': 4}
  assert rpg_simulator.is_win(player_stats, BOSS_STATS) == True

def test_should_win_example_4():
  player_stats = {'name': 'player', 'hp': 100, 'damage': 7, 'armour': 3}
  assert rpg_simulator.is_win(player_stats, BOSS_STATS) == False

def test_part1():
  with open(rpg_simulator.input_file) as f:
    data = f.read()
  expected = 111
  assert rpg_simulator.part1(data) == expected

def test_part2():
  with open(rpg_simulator.input_file) as f:
    data = f.read()
  expected = 188
  assert rpg_simulator.part2(data) == expected
