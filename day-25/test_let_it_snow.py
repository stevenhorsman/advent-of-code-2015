import let_it_snow
import fileinput

def test_part1_example_1():
  data = 'To continue, please consult the code grid in the manual.  Enter the code at row 1, column 1.'
  assert let_it_snow.part1(data) == 20151125

def test_part1_example_2():
  data = 'To continue, please consult the code grid in the manual.  Enter the code at row 2, column 6.'
  assert let_it_snow.part1(data) == 4041754

def test_part1_example_3():
  data = 'To continue, please consult the code grid in the manual.  Enter the code at row 6, column 6.'
  assert let_it_snow.part1(data) == 27995004

def test_part1():
  with open(let_it_snow.input_file) as f:
    data = f.read()
  expected = 8997277
  assert let_it_snow.part1(data) == expected

