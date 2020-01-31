from collections import Counter

input_file = 'day-01/input.txt'

def part1(input):
  counter = Counter(input)
  return counter['('] - counter[')']

def part2(input):
  floor = 0
  for i, c in enumerate(input, 1):
    floor += {"(": 1, ")": -1}[c]
    if floor == -1:
      return i

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))