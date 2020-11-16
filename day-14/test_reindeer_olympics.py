import reindeer_olympics
import fileinput

def test_part1_example_1():
  data = '''
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
'''[1:]
  assert reindeer_olympics.part1(data, 1000) == 1120

def test_part1():
  with open(reindeer_olympics.input_file) as f:
    data = f.read()
  expected = 2640
  assert reindeer_olympics.part1(data) == expected

def test_part2_example_1():
  data = '''
Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
'''[1:]
  assert reindeer_olympics.part2(data, 1000) == 689

def test_part2():
  with open(reindeer_olympics.input_file) as f:
    data = f.read()
  expected = 1102
  assert reindeer_olympics.part2(data) == expected
