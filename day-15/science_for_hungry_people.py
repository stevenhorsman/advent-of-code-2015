import re, itertools, sys
from collections import defaultdict
input_file = 'day-15/input.txt'

MAX_VOL = 100

def generate_combinations(ingredients_list, max_vol):
  return itertools.combinations_with_replacement(ingredients_list, max_vol)

def generate_ingredients_map(input):
  ingredients_map = defaultdict(list)
  for line in input.splitlines():
    name, capacity, durability, flavour, texture, calories = list(re.match(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", line).groups())
    ingredients_map[name] = [int(v) for v in [capacity, durability, flavour, texture, calories]]
  return ingredients_map

def calculate_best_score(ingredients_map, calorie_limt = sys.maxsize):
  best_score = 0
  for combination in generate_combinations(list(ingredients_map.keys()), MAX_VOL):
    capacity = durability = flavour = texture = calories = 0
    for ingredient in combination:
      capacity += ingredients_map[ingredient][0]
      durability += ingredients_map[ingredient][1]
      flavour += ingredients_map[ingredient][2]
      texture += ingredients_map[ingredient][3]
      calories += ingredients_map[ingredient][4]
    if calories > calorie_limt:
      continue
    best_score = max(best_score, max(capacity, 0) * max(durability, 0) * max(flavour, 0) * max(texture, 0))
  return best_score

def part1(input):
  ingredients_map = generate_ingredients_map(input)
  return calculate_best_score(ingredients_map)

def part2(input):
  ingredients_map = generate_ingredients_map(input)
  return calculate_best_score(ingredients_map, 500)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))