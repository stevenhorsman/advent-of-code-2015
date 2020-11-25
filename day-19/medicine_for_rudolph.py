import re

input_file = 'day-19/input.txt'

def part1(input):
  formulae_list, molecule = input.split('\n\n')
  new_molecules = set()
  for transform in formulae_list.splitlines():
    before, after = transform.split(' => ')
    for match in re.finditer(before, molecule):
      new_molecules.add(molecule[:match.start()] + after + molecule[match.end():])
  return len(new_molecules)

def part2(input):
  formulae_list, molecule = input.split('\n\n')
  target = molecule[::-1] # Reverse the string
  new_molecules = set()
  reverse_transform_dict = {}
  for transform in formulae_list.splitlines():
    before, after = transform.split(' => ')
    reverse_transform_dict[after[::-1]] = before[::-1]

  def rep(x):
    return reverse_transform_dict[x.group()]

  count = 0
  while target != 'e':
    matches = list(re.finditer('|'.join(reverse_transform_dict.keys()), target))
    target = re.sub('|'.join(reverse_transform_dict.keys()), rep, target, 1)
    count += 1
  return count

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))