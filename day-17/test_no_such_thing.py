import no_such_thing
import fileinput

def test_part1_example_1():
  data = '''
20
15
10
5
5'''[1:]
  assert no_such_thing.part1(data, 25) == 4

def test_part1():
  with open(no_such_thing.input_file) as f:
    data = f.read()
  expected = 654
  assert no_such_thing.part1(data) == expected

def test_part2_example_1():
  data = '''
20
15
10
5
5'''[1:]
  assert no_such_thing.part2(data, 25) == 3

def test_part2():
  with open(no_such_thing.input_file) as f:
    data = f.read()
  expected = 57
  assert no_such_thing.part2(data) == expected
