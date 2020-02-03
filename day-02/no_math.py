import re, numpy, itertools

input_file = 'day-02/input.txt'

def get_dimensions(line):
  # m = re.match("^(\d+)x(\d+)x(\d+)$", line)
  # return sorted(map(int, m.group(1,2,3)))
  return sorted(map(int, line.split('x')))

def get_area(line):
  dimensions = get_dimensions(line)
  sides = [x*y for (x,y) in itertools.combinations(dimensions, 2)]
  return (2 * sum(sides)) + min(sides)

def get_ribbon(line):
  dimensions = get_dimensions(line)
  volume = numpy.prod(dimensions)
  perimeter = 2 * (dimensions[0] + dimensions[1])
  return volume + perimeter

def part1(input):
  return sum(get_area(line) for line in input.splitlines())

def part2(input):
  return sum(get_ribbon(line) for line in input.splitlines())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))