import re, json
input_file = 'day-12/input.txt'

def sum_digits(string):
  return sum([int(s) for s in re.findall(r'[-\d]+', string)])

def part1(input):
  return sum_digits(input)

def part2(input):
  return count_non_red_json(json.loads(input))

def count_non_red_json(input):
  if type(input) == int:
    return input
  elif type(input) == list:
    return sum(count_non_red_json(item) for item in input)
  elif type(input) == dict and not 'red' in input.values():
    return sum(count_non_red_json(value) for value in input.values())
  return 0

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))