import re
from collections import defaultdict
from itertools import permutations, chain, cycle

input_file = 'day-13/input.txt'

def create_dict(input):
  happiness_dict = defaultdict(int)

  for line in input.splitlines():
    p1, gain_or_lose, happiness, p2 = list(re.match(r"(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+).", line).groups())
    happiness_dict[(p1,p2)] = int(happiness) if gain_or_lose == "gain" else -int(happiness)
  return happiness_dict

def calculate_max_happiness(input, include_me = False):
  happiness_dict = create_dict(input)
  people = set(chain.from_iterable(happiness_dict.keys()))
  if include_me:
    people.add('Me')
  # TODO - optimise so that all permutations that are equal (shifted by one, or reversed) are removed
  return max(sum(happiness_dict[(p1,p2)] + happiness_dict[(p2,p1)] for p1, p2 in zip(p, p[1:] + p[:1])) for p in permutations(people))

def part1(input):
  return calculate_max_happiness(input)

def part2(input):
  return calculate_max_happiness(input, True)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))