import re

input_file = 'day-06/input.txt'

def base(input, action):
  brightnesses = [[0]*1000 for x in range(1000)]
  for line in input.splitlines():
    instruction, *points = list(re.match(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", line).groups())
    start_x, start_y, stop_x, stop_y = [int(x) for x in points]
    for x in range(start_x, stop_x + 1):
      for y in range(start_y, stop_y + 1):
        brightnesses[y][x] = action(instruction, brightnesses[y][x])
  return sum(sum(b) for b in brightnesses)

def part1(input):
  action = lambda instruction, curr: {'toggle': 1 - curr, 'turn on': 1, 'turn off': 0}[instruction]
  return base(input, action)

def part2(input):
  action = lambda instruction, curr: {'toggle': curr + 2, 'turn on': curr + 1, 'turn off': max(0, curr -1)}[instruction]
  return base(input, action)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))