import re

input_file = 'day-25/input.txt'

def get_code_number(row, column):
    side_length = row + column
    triangle = (side_length - 1) * (side_length) // 2
    return triangle - row + 1

def part1(input):
  row, column = list(map(int, list(re.match(r"To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).", input).groups())))
  code_no = get_code_number(row, column)
  print(row, column, code_no)

  answer = 20151125
  for _ in range(code_no - 1):
    answer = (answer * 252533) % 33554393
  return answer

def part2(input):
  return 0

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))