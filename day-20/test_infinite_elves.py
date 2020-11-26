import infinite_elves
import fileinput

def test_part1_example_1():
  data = '100'
  assert infinite_elves.part1(data) == 6

def test_part1_example_2():
  data = '150'
  assert infinite_elves.part1(data) == 8

def test_part1():
  with open(infinite_elves.input_file) as f:
    data = f.read()
  expected = 831600
  assert infinite_elves.part1(data) == expected

def test_part2_example_1():
  data = '100'
  assert infinite_elves.part2(data) == 6

def test_part2_example_2():
  data = '198'
  assert infinite_elves.part2(data) == 10

def test_part2():
  with open(infinite_elves.input_file) as f:
    data = f.read()
  expected = 884520
  assert infinite_elves.part2(data) == expected
