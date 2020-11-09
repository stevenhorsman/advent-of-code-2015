input_file = 'day-08/input.txt'

def part1(input):
  #Shorter version
  #return sum(len(line) - len(eval(line)) for line in input.splitlines())
  
  literal_count = 0
  memory_count = 0

  for line in input.splitlines():
    literal_count += len(line)
    memory_count += len(eval(line))
  
  return literal_count - memory_count

# Difference is:
  # Add 2 extra for start and end quotes
  # Add 1 for each " and \
def part2(input):
  return sum(2 + line.count('"') + line.count('\\') for line in input.splitlines())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))