import re, math
from collections import defaultdict

input_file = 'day-14/input.txt'

def create_time_dict(input, time):
  time_results = defaultdict(dict)
  for line in input.splitlines():
    reindeer, speed, duration, rest_time = list(re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line).groups())
    speed, duration, rest_time = int(speed), int(duration), int(rest_time)
    repeats = math.ceil(time / (duration + rest_time))
    increments = repeats * ([speed] * duration + [0] * rest_time)
    for i in range(1, time + 1):
      time_results[i][reindeer] = sum(increments[:i])
  return time_results

def part1(input, time = 2503):
  time_dict = create_time_dict(input, time)
  return max(distance for name, distance in time_dict[time].items())

def part2(input, time = 2503):
  time_dict = create_time_dict(input, time)
  scores = dict.fromkeys(time_dict[time].keys(), 0)
  for _, results in time_dict.items():
    max_value = max(results.values())  # maximum value
    for name in [k for k, v in results.items() if v == max_value]:
      scores[name] += 1
  return max(scores.values())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))