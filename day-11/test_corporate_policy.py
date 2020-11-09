import corporate_policy
import fileinput

def test_is_valid_example_1():
  check_is_valid('hijklmmn', False)

def test_is_valid_example_2():
  check_is_valid('abbceffg', False)

def test_is_valid_example_3():
  check_is_valid('abbcegjk', False)

def test_is_valid_example_4():
  check_is_valid('abcdffaa', True)

def check_is_valid(password, expected):
  assert corporate_policy.is_valid(password) == expected

def test_part1_example_1():
  data = 'abcdefgh'
  assert corporate_policy.part1(data) == 'abcdffaa'

def test_part1_example_2():
  data = 'ghijklmn'
  assert corporate_policy.part1(data) == 'ghjaabcc'

def test_part1():
  with open(corporate_policy.input_file) as f:
    data = f.read()
  expected = 'hepxxyzz'
  assert corporate_policy.part1(data) == expected

def test_part2():
  with open(corporate_policy.input_file) as f:
    data = f.read()
  expected = 'heqaabcc'
  assert corporate_policy.part2(data) == expected
