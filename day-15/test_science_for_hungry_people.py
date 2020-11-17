import science_for_hungry_people
import fileinput

def test_part1_example_1():
  data = '''
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''[1:]
  assert science_for_hungry_people.part1(data) == 62842880

def test_part1():
  with open(science_for_hungry_people.input_file) as f:
    data = f.read()
  expected = 21367368
  assert science_for_hungry_people.part1(data) == expected

def test_part2_example_1():
  data = '''
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''[1:]
  assert science_for_hungry_people.part2(data) == 57600000

def test_part2():
  with open(science_for_hungry_people.input_file) as f:
    data = f.read()
  expected = 1766400
  assert science_for_hungry_people.part2(data) == expected
