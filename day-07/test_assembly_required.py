import assembly_required
import fileinput

EXAMPLE = '''
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
123 -> x
456 -> y
NOT x -> h
NOT y -> i'''[1:]

def test_part1_example_d():
  check_part1_variables(EXAMPLE, 'd', 72)

def test_part1_example_e():
  check_part1_variables(EXAMPLE, 'e', 507)

def test_part1_example_f():
  check_part1_variables(EXAMPLE, 'f', 492)

def test_part1_example_g():
  check_part1_variables(EXAMPLE, 'g', 114)

def test_part1_example_h():
  check_part1_variables(EXAMPLE, 'h', 65412)

def test_part1_example_i():
  check_part1_variables(EXAMPLE, 'i', 65079)

def test_part1_example_x():
  check_part1_variables(EXAMPLE, 'x', 123)

def test_part1_example_y():
  check_part1_variables(EXAMPLE, 'y', 456)

def check_part1_variables(data, variable, expected):
  assert assembly_required.part1(data, variable) == expected

def test_part1():
  with open(assembly_required.input_file) as f:
    data = f.read()
  expected = 3176
  assert assembly_required.part1(data) == expected

def test_part2():
  with open(assembly_required.input_file) as f:
    data = f.read()
  expected = 14710
  assert assembly_required.part2(data) == expected
