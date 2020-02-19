import re

input_file = 'day-05/input.txt'

def vowel_count(string):
  return sum(1 for c in string if c in 'aeiou')

# lambda string: any(x[0] == x[1] for x in zip(string, string[1:])),
def contains_double(string):
  for i in range(1,len(string)):
    if string[i-1] == string [i]:
      return True
  return False

BLACK_LIST=['ab', 'cd', 'pq', 'xy']
def contains_black_list(string):
  return any(black in string for black in BLACK_LIST)

def is_nice_part_1(string):
  return vowel_count(string) >= 3 and contains_double(string) and not contains_black_list(string)

def part1(input):
  return sum(is_nice_part_1(line) for line in input.splitlines())

def contains_double_with_insert(string):
  for i in range(2,len(string)):
    if string[i-2] == string [i]:
      return True
  return False

# It contains a pair of any two letters that appears at least twice in the string
def contains_double_pair(string):
  return re.search(r'(.)(.).*\1\2', string) != None

def is_nice_part_2(string):
  return contains_double_pair(string) and contains_double_with_insert(string)

def part2(input):
   return sum(is_nice_part_2(line) for line in input.splitlines())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))