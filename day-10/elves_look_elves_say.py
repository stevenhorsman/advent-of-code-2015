import re
from itertools import groupby

input_file = 'day-10/input.txt'

def generate_sequence(input, iterations):
  for _ in range(iterations):
    # input = ''.join([str(len(group)) + group[0] for group in [m.group(0) for m in re.finditer(r"(\d)\1*", input)]]) # 12s
    input = ''.join(str(len(list(g))) + k for k, g in groupby(input)) # 10s
  return input

def part1(input, iterations = 40):
  return len(generate_sequence(input, iterations))

def part2(input):
  return len(generate_sequence(input, 50))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))