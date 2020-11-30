import opening_the_turing_lock
import fileinput

def test_part1_example_1():
  data = '''
inc a
jio a, +2
tpl a
inc a'''[1:]
  assert opening_the_turing_lock.part1(data, 'a') == 2

def test_part1():
  with open(opening_the_turing_lock.input_file) as f:
    data = f.read()
  expected = 184
  assert opening_the_turing_lock.part1(data) == expected

def test_part2():
  with open(opening_the_turing_lock.input_file) as f:
    data = f.read()
  expected = 231
  assert opening_the_turing_lock.part2(data) == expected
