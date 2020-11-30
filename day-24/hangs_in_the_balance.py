import itertools, operator
from functools import reduce

input_file = 'day-24/input.txt'

def does_remainder_split(weights, split_groups):
  target_weight = sum(weights) // split_groups
  for group_size in range(1, len(weights)):
    for group in [comb for comb in itertools.combinations(weights, group_size) if sum(comb) == target_weight]:
      if split_groups == 2:
        return True #we've found a valid split, return up the stack to calculate the best approach
      else:
        return does_remainder_split(list(set(weights) - set(group)), split_groups - 1)

def get_best_entanglement(weights, split_groups):
  target_weight = sum(weights) // split_groups
  for group_size in range(1, len(weights)): # automatically finishes once we find the smallest group one
    candidate_groups = [comb for comb in itertools.combinations(weights, group_size) if sum(comb) == target_weight]
    valid_groups = [group for group in candidate_groups if does_remainder_split(list(set(weights) - set(group)), split_groups - 1)]
    if len(valid_groups) > 0:
      products = list(map(lambda group: reduce(operator.mul, group, 1), valid_groups))
      return sorted(products)[0]

def part1(input):
  packages = list(map(int, input.splitlines()))
  return get_best_entanglement(packages, 3)

def part2(input):
  packages = list(map(int, input.splitlines()))
  return get_best_entanglement(packages, 4)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))