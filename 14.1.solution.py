import helpers
from collections import defaultdict

def parse_line(line):
  l, r = line.split(' = ')
  if l == 'mask':
    return ('mask', r)
  return ('mem', int(l[4:-1]), int(r))

def parse_input(lines):
  return map(parse_line, lines)

def make_mask(mask_str):
  return int(mask_str.replace('X', '1'), 2), int(mask_str.replace('X', '0'), 2)

def apply_mask(v, mask):
  return v & mask[0] | mask[1]

def solve(insts):
  memory = defaultdict(int)
  mask = make_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
  for inst in insts:
    if inst[0] == 'mask':
      mask = make_mask(inst[1])
    else:
      memory[inst[1]] = apply_mask(inst[2], mask)
  return sum(memory.values())

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(lines=[
    'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
    'mem[8] = 11',
    'mem[7] = 101',
    'mem[8] = 0',
  ], expected=165)
  

test()
print(solver.solve(file="14.input.txt"))
