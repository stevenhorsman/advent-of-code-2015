import re

input_file = 'day-10/input.txt'

def generate_sequence(input, iterations):
  for _ in range(iterations):
    groups = [m.group(0) for m in re.finditer(r"(\d)\1*", input)]
    result = ''
    for group in groups:
      result += str(len(group)) + group[0]
    # print(input + ' -> ' + result)
    input = result
  return result

def part1(input, iterations = 40):
  return len(generate_sequence(input, iterations))

def part2(input):
  return len(generate_sequence(input, 50))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))