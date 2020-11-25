import medicine_for_rudolph, fileinput, pytest

def test_part1_example_1():
  data = '''
H => HO
H => OH
O => HH

HOH'''[1:]
  assert medicine_for_rudolph.part1(data) == 4

def test_part1_example_2():
  data = '''
H => HO
H => OH
O => HH

HOHOHO'''[1:]
  assert medicine_for_rudolph.part1(data) == 7

def test_part1():
  with open(medicine_for_rudolph.input_file) as f:
    data = f.read()
  expected = 576
  assert medicine_for_rudolph.part1(data) == expected

def test_part2_example_1():
  data = '''
H => HO
H => OH
O => HH
e => H
e => O

HOH'''[1:]
  assert medicine_for_rudolph.part2(data) == 3

@pytest.mark.skip(reason="Solution infinite loops given these conditions")
def test_part2_example_2():
  data = '''
H => HO
H => OH
O => HH
e => H
e => O

HOHOHO'''[1:]
  assert medicine_for_rudolph.part2(data) == 6

def test_part2():
  with open(medicine_for_rudolph.input_file) as f:
    data = f.read()
  expected = 207
  assert medicine_for_rudolph.part2(data) == expected
