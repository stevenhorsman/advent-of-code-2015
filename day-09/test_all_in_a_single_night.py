import all_in_a_single_night
import fileinput

def test_part1_example_1():
  data = '''
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141'''[1:]
  assert all_in_a_single_night.part1(data) == 605

def test_part1():
  with open(all_in_a_single_night.input_file) as f:
    data = f.read()
  expected = 117
  assert all_in_a_single_night.part1(data) == expected

def test_part2_example_1():
  data = '''
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141'''[1:]
  assert all_in_a_single_night.part2(data) == 982

def test_part2():
  with open(all_in_a_single_night.input_file) as f:
    data = f.read()
  expected = 909
  assert all_in_a_single_night.part2(data) == expected
