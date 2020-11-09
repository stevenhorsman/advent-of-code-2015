import matchsticks
import fileinput

def test_part1_example_1():
  data = '''
""
"abc"
"aaa\\"aaa"
"\\x27"'''[1:]
  assert matchsticks.part1(data) == 12

def test_part1():
  with open(matchsticks.input_file) as f:
    data = f.read()
  expected = 1333
  assert matchsticks.part1(data) == expected

def test_part2_example_1():
  data = '''
""'''[1:]
  assert matchsticks.part2(data) == 4

def test_part2_example_2():
  data = '''
""
"abc"
"aaa\\"aaa"
"\\x27"'''[1:]
  assert matchsticks.part2(data) == 19

def test_part2():
  with open(matchsticks.input_file) as f:
    data = f.read()
  expected = 2046
  assert matchsticks.part2(data) == expected
