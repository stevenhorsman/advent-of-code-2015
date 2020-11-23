from itertools import combinations
input_file = 'day-17/input.txt'

def count_container_combos(input, target, break_on_min = False):
  containers = [int(x) for x in input.splitlines()]
  valid_combinations = 0
  for i in range(1, len(containers) + 1):
    valid_combinations += sum(1 for comb in combinations(containers, i) if sum(comb) == target)
    if break_on_min and valid_combinations > 0:
      return valid_combinations
  return valid_combinations

def part1(input, target = 150):
  return count_container_combos(input, target)

def part2(input, target = 150):
    return count_container_combos(input, target, True)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))