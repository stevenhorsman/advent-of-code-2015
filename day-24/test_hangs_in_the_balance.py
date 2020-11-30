import hangs_in_the_balance
import fileinput

def test_part1_example_1():
  data = '''
1
2
3
4
5
7
8
9
10
11'''[1:]
  assert hangs_in_the_balance.part1(data) == 99

def test_part1():
  with open(hangs_in_the_balance.input_file) as f:
    data = f.read()
  expected = 11266889531
  assert hangs_in_the_balance.part1(data) == expected

def test_part2_example_1():
  data = '''
1
2
3
4
5
7
8
9
10
11'''[1:]
  assert hangs_in_the_balance.part2(data) == 44

def test_part2():
  with open(hangs_in_the_balance.input_file) as f:
    data = f.read()
  expected = 77387711
  assert hangs_in_the_balance.part2(data) == expected
