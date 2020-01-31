import not_quite_lisp
import fileinput

def test_part1_example_1():
  data = "()()"
  assert not_quite_lisp.part1(data) == 0

def test_part1_example_2():
  data = "(())"
  assert not_quite_lisp.part1(data) == 0

def test_part1_example_3():
  data = '((('
  assert not_quite_lisp.part1(data) == 3

def test_part1_example_4():
  data = '(()(()('
  assert not_quite_lisp.part1(data) == 3

def test_part1_example_5():
  data = '))((((('
  assert not_quite_lisp.part1(data) == 3

def test_part1_example_6():
  data = ')))'
  assert not_quite_lisp.part1(data) == -3

def test_part1_example_7():
  data = ')())())'
  assert not_quite_lisp.part1(data) == -3

def test_part1():
  with open(not_quite_lisp.input_file) as f:
    data = f.read()
  expected = 138
  assert not_quite_lisp.part1(data) == expected

def test_part2_example_1():
  data = ')'
  assert not_quite_lisp.part2(data) == 1

def test_part2_example_2():
  data = "()())"
  assert not_quite_lisp.part2(data) == 5

def test_part2():
  with open(not_quite_lisp.input_file) as f:
    data = f.read()
  expected = 1771
  assert not_quite_lisp.part2(data) == expected
