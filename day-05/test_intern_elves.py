import intern_elves
import fileinput

def test_part1_example_1():
  data = 'ugknbfddgicrmopn'
  assert intern_elves.part1(data) == 1

def test_part1_example_2():
  data = "aaa"
  assert intern_elves.part1(data) == 1

def test_part1_example_3():
  data = "jchzalrnumimnmhp"
  assert intern_elves.part1(data) == 0

def test_part1_example_4():
  data = "haegwjzuvuyypxyu"
  assert intern_elves.part1(data) == 0

def test_part1_example_5():
  data = "dvszwmarrgswjxmb"
  assert intern_elves.part1(data) == 0

def test_part1():
  with open(intern_elves.input_file) as f:
    data = f.read()
  expected = 255
  assert intern_elves.part1(data) == expected

def test_part2_example_1():
  data = 'qjhvhtzxzqqjkmpb'
  assert intern_elves.part2(data) == 1

def test_part2_example_2():
  data = "uurcxstgmygtbstg"
  assert intern_elves.part2(data) == 0

def test_part2_example_3():
  data = "ieodomkazucvgmuy"
  assert intern_elves.part2(data) == 0

def test_part2():
  with open(intern_elves.input_file) as f:
    data = f.read()
  expected = 55
  assert intern_elves.part2(data) == expected
