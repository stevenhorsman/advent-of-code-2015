import itertools, re

input_file = 'day-11/input.txt'

def is_valid(password):
  return not contains_black_list(password) and contains_three_consecutive(password) and contains_double_pair(password)

def contains_three_consecutive(string):
  return any(ord(x)+2 == ord(y)+1 == ord(z) for x, y, z in zip(string, string[1:], string[2:]))

def contains_black_list(string):
  return any(c in ['i','o','l'] for c in string)

def contains_double_pair(string):
  double_list = re.findall(r'([a-z])\1', string)
  return len(double_list) >= 2

def part1(input):
  input = increment_string(input)
  max = 10000000000000
  while not is_valid(input) and max > 0:
    input = increment_string(input)
    max -= 1
  return input

def increment_string(input):
  for index in range(len(input)-1, 0, -1):
    if ord(input[index]) == 122:
      input = input[:index] + 'a' + input[index + 1:]
    elif ord(input[index]) < 122:
      input = input[:index] + chr(ord(input[index]) + 1) + input[index + 1:]
      break
  return input

def part2(input):
  first_password = part1(input)
  return part1(first_password)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))