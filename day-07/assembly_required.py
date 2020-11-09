import collections, re

input_file = 'day-07/input.txt'

def get(wires, x):
  try:
    v = int(x)
    return v
  except:
    return wires.get(x)

def get_inputs(wires, inputs, indexes):
  return [get(wires, inputs[x]) for x in indexes]

def part1(input_file, variable = 'a'):
  wires = {}
  instructions = input_file.splitlines()
  while instructions:
    line = instructions.pop(0)
    input, output = line.split(' -> ')
    inputs = input.split()
    if len(inputs) == 1: # assignment
      evaluated = get_inputs(wires, inputs, [0])
      if all(input != None for input in evaluated):
        wires[output] = evaluated[0]
      else:
        instructions.append(line)
    elif len(inputs) == 2: #NOT
      evaluated = get_inputs(wires, inputs, [1])
      if all(input != None for input in evaluated):
        wires[output] = ~ evaluated[0] & 0xffff
      else:
        instructions.append(line)
    elif len(inputs) == 3: 
      evaluated = get_inputs(wires, inputs, [0,2])
      if all(input != None for input in evaluated):
        if inputs[1] == 'AND':
          wires[output] = evaluated[0] & evaluated[1]
        elif inputs[1] == 'OR':
          wires[output] = evaluated[0] | evaluated[1]
        elif inputs[1] == 'LSHIFT':
          wires[output] = evaluated[0] << evaluated[1]
        elif inputs[1] == 'RSHIFT':
          wires[output] = evaluated[0] >> evaluated[1]
      else:
        instructions.append(line)

  return wires[variable]

def part2(input):
  init_a = part1(input, 'a')
  #Override b to a
  input = input.replace('44430 -> b',str(init_a) + ' -> b')
  return part1(input, 'a')

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))