from collections import defaultdict
import math

input_file = 'day-20/input.txt'

def get_divisors(n):
  small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
  large_divisors = [n / d for d in small_divisors if n != d * d]
  return small_divisors + large_divisors

def part1(input):
  target = int(input)

  house_no = 0
  while True:
    house_no +=1
    presents = sum(get_divisors(house_no)) * 10
    if presents >= target:
      return house_no

def part2(input):
  target = int(input)

  house_no = 0
  while True:
    house_no +=1
    presents = sum(d for d in get_divisors(house_no) if house_no / d <= 50) * 11
    if presents >= target:
      return house_no

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))