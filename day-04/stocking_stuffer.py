import hashlib, itertools, concurrent

input_file = 'day-04/input.txt'

def get_md5_hex(input, number):
  return hashlib.md5((input + str(number)).encode('utf-8')).hexdigest()

def find_leading_zeros(input, zeroes):
  for i in itertools.count():
    if get_md5_hex(input, i).startswith('0' * zeroes):
      return i

def part1(input):
  return find_leading_zeros(input, 5)

def part2(input):
  return find_leading_zeros(input, 6)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))