import elves_look_elves_say
import fileinput

def test_generate_sequence_example_1():
  data = "1"
  assert elves_look_elves_say.generate_sequence(data, 1) == "11"

def test_generate_sequence_example_2():
  data = "21"
  assert elves_look_elves_say.generate_sequence(data, 1) == "1211"

def test_generate_sequence_example_3():
  data = "1"
  assert elves_look_elves_say.generate_sequence(data, 5) == "312211"

def test_part1_example_1():
  data = "1"
  assert elves_look_elves_say.part1(data, 5) == 6

def test_part1():
  with open(elves_look_elves_say.input_file) as f:
    data = f.read()
  expected = 492982
  assert elves_look_elves_say.part1(data) == expected

def test_part2():
  with open(elves_look_elves_say.input_file) as f:
    data = f.read()
  expected = 6989950
  assert elves_look_elves_say.part2(data) == expected
