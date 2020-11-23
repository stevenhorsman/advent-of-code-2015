import aunt_sue
import fileinput

def test_part1():
  with open(aunt_sue.input_file) as f:
    data = f.read()
  expected = 40
  assert aunt_sue.part1(data) == expected

def test_part2():
  with open(aunt_sue.input_file) as f:
    data = f.read()
  expected = 241
  assert aunt_sue.part2(data) == expected
