import spherical_houses
import fileinput

def test_part1_example_1():
  data = '>'
  assert spherical_houses.part1(data) == 2

def test_part1_example_2():
  data = "^>v<"
  assert spherical_houses.part1(data) == 4

def test_part1_example_3():
  data = "^v^v^v^v^v"
  assert spherical_houses.part1(data) == 2

def test_part1():
  with open(spherical_houses.input_file) as f:
    data = f.read()
  expected = 2592
  assert spherical_houses.part1(data) == expected

def test_part2_example_1():
  data = '^v'
  assert spherical_houses.part2(data) == 3

def test_part2_example_2():
  data = '^>v<'
  assert spherical_houses.part2(data) == 3

def test_part2_example_3():
  data = '^v^v^v^v^v'
  assert spherical_houses.part2(data) == 11

def test_part2():
  with open(spherical_houses.input_file) as f:
    data = f.read()
  expected = 2360
  assert spherical_houses.part2(data) == expected
