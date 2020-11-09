import re
from collections import defaultdict
from itertools import permutations, chain

input_file = 'day-09/input.txt'

def produce_trip_lengths(input):
  graph = defaultdict(int)

  for line in input.splitlines():
    start, end, length = list(re.match(r"(\w+) to (\w+) = (\d+)", line).groups())
    graph[(start, end)] = graph[(end, start)] = int(length)
  
  nodes = set(chain.from_iterable(graph.keys()))

  return [sum(graph[step] for step in zip(p, p[1:])) for p in permutations(nodes)]

def part1(input):
  return min(produce_trip_lengths(input))

def part2(input):
  return max(produce_trip_lengths(input))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))