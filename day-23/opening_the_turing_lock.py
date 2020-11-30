from collections import defaultdict

input_file = 'day-23/input.txt'

class Program:
  def __init__(self, lines, reg_a = 0):
    self.lines = lines
    self.pc = 0
    self.regs = defaultdict(int)
    self.regs['a'] = reg_a

  def run(self):
    while self.tick():
      # print(self.regs, self.pc)
      pass

  def get(self, x):
    try:
      v = int(x)
      return v
    except:
      return self.regs[x]

  def tick(self):
    if not (0 <= self.pc < len(self.lines)):
      return False

    instruction, parameters = self.lines[self.pc].split(' ', 1)
    parameters = parameters.split(', ')
    x = y = None
    if len(parameters) == 2:
      x, y = parameters[0], self.get(parameters[1])
    else:
      x = parameters[0]

    if instruction == 'hlf':
      self.regs[x] /= 2
    elif instruction == 'tpl':
      self.regs[x] *= 3
    elif instruction == 'inc':
      self.regs[x] += 1
    elif instruction == 'jmp':
      x = self.get(x)
      self.pc += x
      return True # skip the pc += 1
    elif instruction == 'jie':
      if self.regs[x] % 2 == 0:
        self.pc += y
        return True # skip the pc += 1
    elif instruction == 'jio':
       if self.regs[x] == 1:
        self.pc += y
        return True # skip the pc += 1
    self.pc += 1
    return True

def part1(input, output_reg = 'b'):
  program = Program([line.split('#')[0] for line in input.splitlines()])
  program.run()
  return program.get(output_reg)

def part2(input, output_reg = 'b'):
  program = Program([line.split('#')[0] for line in input.splitlines()], 1)
  program.run()
  return program.get(output_reg)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))