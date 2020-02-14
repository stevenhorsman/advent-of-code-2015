import stocking_stuffer
import fileinput

def test_part1_example_1():
  data = 'abcdef'
  assert stocking_stuffer.part1(data) == 609043

def test_part1_example_2():
  data = "pqrstuv"
  assert stocking_stuffer.part1(data) == 1048970

def test_part1():
  with open(stocking_stuffer.input_file) as f:
    data = f.read()
  expected = 282749
  assert stocking_stuffer.part1(data) == expected

def test_part2():
  with open(stocking_stuffer.input_file) as f:
    data = f.read()
  expected = 9962624
  assert stocking_stuffer.part2(data) == expected
