import like_a_gif
import fileinput

def test_part1_example_1():
  data = '''
.#.#.#
...##.
#....#
..#...
#.#..#
####..'''[1:]
  assert like_a_gif.part1(data, 4) == 4

def test_part1():
  with open(like_a_gif.input_file) as f:
    data = f.read()
  expected = 814
  assert like_a_gif.part1(data) == expected

def test_part2_example_1():
  data = '''
##.#.#
...##.
#....#
..#...
#.#..#
####.#'''[1:]
  assert like_a_gif.part2(data, 5) == 17

def test_part2():
  with open(like_a_gif.input_file) as f:
    data = f.read()
  expected = 924
  assert like_a_gif.part2(data) == expected
