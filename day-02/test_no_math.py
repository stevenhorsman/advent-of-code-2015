import no_math
import fileinput

def test_part1_example_1():
  data = '2x3x4'
  assert no_math.part1(data) == 58

def test_part1_example_2():
  data = "1x1x10"
  assert no_math.part1(data) == 43

def test_part1():
  with open(no_math.input_file) as f:
    data = f.read()
  expected = 1586300
  assert no_math.part1(data) == expected

def test_part2_example_1():
  data = '2x3x4'
  assert no_math.part2(data) == 34

def test_part2_example_2():
  data = "1x1x10"
  assert no_math.part2(data) == 14

def test_part2():
  with open(no_math.input_file) as f:
    data = f.read()
  expected = 3737498
  assert no_math.part2(data) == expected
