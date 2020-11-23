import re

input_file = 'day-16/input.txt'

correct_sue = {}
correct_sue['children'] = 3
correct_sue['cats'] = 7
correct_sue['samoyeds'] = 2
correct_sue['pomeranians'] = 3
correct_sue['akitas'] = 0
correct_sue['vizslas'] = 0
correct_sue['goldfish'] = 5
correct_sue['trees'] = 3
correct_sue['cars'] = 2
correct_sue['perfumes'] = 1

def is_attribute_valid(attribute_string, part_2 = False):
  name, value = list(re.match(r"(\w+): (\d+)", attribute_string).groups())
  if part_2:
    if name in ['trees', 'cats']:
      return correct_sue[name] < int(value)
    elif name in ['pomeranians', 'goldfish']:
      return correct_sue[name] > int(value)
  return correct_sue[name] == int(value)
  
def find_correct_aunt(input, part_2 = False):
  for line in input.splitlines():
    sue_no, attributes = list(re.match(r"Sue (\d+): (.*)", line).groups())
    is_valid = lambda attributes: all(is_attribute_valid(attribute_string, part_2) for attribute_string in attributes.split(", "))
    if is_valid(attributes):
      return int(sue_no)

def part1(input):
  return find_correct_aunt(input)
  
def part2(input):
  return find_correct_aunt(input, True)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))