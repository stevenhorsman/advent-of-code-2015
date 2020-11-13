import knights_of_the_dinner_table
import fileinput

def test_part1_example_1():
  data = '''
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.'''[1:]
  assert knights_of_the_dinner_table.part1(data) == 330

def test_part1():
  with open(knights_of_the_dinner_table.input_file) as f:
    data = f.read()
  expected = 618
  assert knights_of_the_dinner_table.part1(data) == expected

def test_part2_example_1():
  data = '''
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.'''[1:]
  assert knights_of_the_dinner_table.part2(data) == 286

def test_part2():
  with open(knights_of_the_dinner_table.input_file) as f:
    data = f.read()
  expected = 601
  assert knights_of_the_dinner_table.part2(data) == expected
