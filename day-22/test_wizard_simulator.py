import wizard_simulator
import fileinput

def test_simulate_fight():
  assert wizard_simulator.simulate_fight(13, 8, 10, 250, ['Poison', 'Missile']) == True

def test_simulate_fight_example_2():
  assert wizard_simulator.simulate_fight(14, 8, 10, 250, ['Recharge', 'Shield', 'Drain', 'Poison', 'Missile']) == True

def test_part1_example_1():
  data = '''
Hit Points: 13
Damage: 8'''[1:]
  assert wizard_simulator.part1(data, 10, 250) == 173 + 53

def test_part1_example_2():
  data = '''
Hit Points: 14
Damage: 8'''[1:]
  assert wizard_simulator.part1(data, 10, 250) == 229 + 73 + 173 + 113 + 53

def test_part1():
  with open(wizard_simulator.input_file) as f:
    data = f.read()
  expected = 1269
  assert wizard_simulator.part1(data) == expected

def test_part2_example_1():
  data = '''
Hit Points: 13
Damage: 8'''[1:]
  assert wizard_simulator.part2(data, 12, 250) == 226

def test_part2_example_2():
  data = '''
Hit Points: 14
Damage: 8'''[1:]
  assert wizard_simulator.part2(data, 15, 250) == 588

def test_part2():
  with open(wizard_simulator.input_file) as f:
    data = f.read()
  expected = 1309
  assert wizard_simulator.part2(data) == expected
