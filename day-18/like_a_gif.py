input_file = 'day-18/input.txt'

WIDTH = HEIGHT = 0

def create_input_set(input):
  on_set = set()
  grid = [[char for char in line] for line in input.splitlines()]
  
  global HEIGHT, WIDTH
  HEIGHT = len(grid)
  WIDTH = len(grid[0])
  
  for y in range(HEIGHT):
    for x in range(WIDTH):
      if grid[y][x] == '#':
        on_set.add((x,y))
  return on_set

def get_adjacents(x, y):
  return [
    (x - 1, y - 1),
    (x - 1, y),
    (x - 1, y + 1),
    (x, y - 1),
    (x, y + 1),
    (x + 1, y - 1),
    (x + 1, y),
    (x + 1, y + 1)
  ]

def count_neighbours(on_set, x, y):
  return sum(1 for neighbour in get_adjacents(x, y) if neighbour in on_set)

def print_grid(iteration, on_set):
  output = 'Iteration' + str(iteration) + ':\n'
  output += '(' + str(WIDTH) + ',' + str(HEIGHT) + ')\n'
  for h in range(HEIGHT):
    for w in range(WIDTH):
      if (w,h) in on_set:
        output += '#'
      else:
        output += '.'
    output += '\n'
  output += '= ' + str(len(on_set)) + '\n'
  print(output)

# Corners are set on for part 2
def corners_on(on_set):
  on_set.add((0,0))
  on_set.add((0,HEIGHT-1))
  on_set.add((WIDTH-1,0))
  on_set.add((WIDTH-1,HEIGHT-1))
  return on_set

def evolve(input, iterations, is_corners_on = False):
  on_set = create_input_set(input)
  if is_corners_on:
    on_set = corners_on(on_set)
  # print_grid(0, on_set)
  for it in range(iterations):
    next_gen = set()
    for x in range(WIDTH):
      for y in range(HEIGHT):
        neighbours = count_neighbours(on_set, x, y)
        if neighbours == 3:
          next_gen.add((x,y))
        if (x,y) in on_set and neighbours == 2:
          next_gen.add((x,y))
    
    on_set = next_gen
    if is_corners_on:
      on_set = corners_on(on_set)
  return on_set


def part1(input, iterations = 100):
  return len(evolve(input, iterations))

def part2(input, iterations = 100):
    return len(evolve(input, iterations, True))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))