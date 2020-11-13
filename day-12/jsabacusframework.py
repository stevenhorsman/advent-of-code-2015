import re, json
input_file = 'day-12/input.txt'

def sum_digits(string):
  return sum([int(s) for s in re.findall(r'[-\d]+', string)])

def part1(input):
  return sum_digits(input)

def part2(input):
  json_input = json.loads(input)
  return count_non_red_json(json_input)

def count_non_red_json(json_input):
  total = 0
  if type(json_input) == dict:
    if not 'red' in json_input.values():
      for value in json_input.values():
        total += count_non_red_json(value)
  elif type(json_input) == list:
    for segment in json_input:
      total += count_non_red_json(segment)
  else:
    total += sum_digits(json.dumps(json_input))
  return total

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))