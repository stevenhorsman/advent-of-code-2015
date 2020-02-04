import collections

input_file = 'day-03/input.txt'

def get_visited(input):
  move = lambda x,y, d: {'^':(x,y+1),'v':(x,y-1),'<':(x-1,y),'>':(x+1,y)}[d]
  x,y = 0,0
  visited = collections.defaultdict(int)
  visited[(x,y)] = 1
  for dir in input:
    (x,y) = move(x, y, dir)
    visited[(x, y)] += 1
  return visited

def part1(input):
  return len(get_visited(input))

def part2(input):
  santa_visited = get_visited(input[::2])
  robot_visited = get_visited(input[1::2])
  return len(santa_visited.keys() | robot_visited.keys())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))