import fire_hazard
import fileinput

def test_part1_example_1():
  data = 'turn on 0,0 through 999,999'
  assert fire_hazard.part1(data) == 1000000

def test_part1_example_2():
  data = "toggle 0,0 through 999,0"
  assert fire_hazard.part1(data) == 1000

def test_part1_example_3():
  data = '''
turn on 0,0 through 999,999
toggle 0,0 through 999,0'''[1:]
  assert fire_hazard.part1(data) == 999000

def test_part1_example_4():
  data = '''
turn on 0,0 through 999,999
turn off 499,499 through 500,500'''[1:]
  assert fire_hazard.part1(data) == 999996

def test_part1():
  with open(fire_hazard.input_file) as f:
    data = f.read()
  expected = 400410
  assert fire_hazard.part1(data) == expected

def test_part2_example_1():
  data = 'turn on 0,0 through 0,0'
  assert fire_hazard.part2(data) == 1

def test_part2_example_2():
  data = "toggle 0,0 through 999,999"
  assert fire_hazard.part2(data) == 2000000

def test_part2_example_3():
  data = '''
turn on 0,0 through 999,999
toggle 499,499 through 500,500'''[1:]
  assert fire_hazard.part2(data) == 1000008

def test_part2_example_4():
  data = 'turn off 0,0 through 0,0'
  assert fire_hazard.part2(data) == 0

def test_part2():
  with open(fire_hazard.input_file) as f:
    data = f.read()
  expected = 15343601
  assert fire_hazard.part2(data) == expected
