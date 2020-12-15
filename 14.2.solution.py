import helpers
from collections import defaultdict
import itertools

def parse_line(line):
  l, r = line.split(' = ')
  if l == 'mask':
    return ('mask', r)
  return ('mem', int(l[4:-1]), int(r))

def to_int(bin):
  return int(bin, 2)

def parse_input(lines):
  return map(parse_line, lines)

def make_mask(mask_str):
  f_mask = to_int(mask_str.replace('X', '0'))
  x_spots = [i for i, v in enumerate(mask_str) if v == 'X']
  ret = [f_mask]
  if not len(x_spots):
    return ret
  for rep_vs in itertools.product('01', repeat=len(x_spots)):
    m0 = list(mask_str.replace('1', '0'))
    m1 = list(mask_str.replace('0', '1'))
    for i, xs in enumerate(x_spots):
      m0[xs] = rep_vs[i]
      m1[xs] = rep_vs[i]
    ret.append((to_int(''.join(m0)), to_int(''.join(m1))))
  return ret

def apply_mask(v, mask):
  return [((v | mask[0]) | m0) & m1 for m0, m1 in mask[1:]]

def solve(insts):
  memory = defaultdict(int)
  mask = None
  for inst in insts:
    if inst[0] == 'mask':
      mask = make_mask(inst[1])
    else:
      for mem in apply_mask(inst[1], mask):
        memory[mem] = inst[2]
  return sum(memory.values())

solver = helpers.Solver(parse_input, solve)
def test():
  helpers.assert_equals(
    ans=make_mask('000000000000000000000000000000X1001X'),
    expected=[
      18,
      (0, 68719476702),
      (1, 68719476703),
      (32, 68719476734),
      (33, 68719476735)
    ],
  )
  helpers.assert_equals(
    ans=make_mask('000000000000000000000000000000X1001X'),
    expected=[
      to_int('000000000000000000000000000000010010'),
      (to_int('000000000000000000000000000000000000'), to_int('111111111111111111111111111111011110')),
      (to_int('000000000000000000000000000000000001'), to_int('111111111111111111111111111111011111')),
      (to_int('000000000000000000000000000000100000'), to_int('111111111111111111111111111111111110')),
      (to_int('000000000000000000000000000000100001'), to_int('111111111111111111111111111111111111')),
    ],
  )
  helpers.assert_equals(
    ans=sorted(apply_mask(42, make_mask('000000000000000000000000000000X1001X'))),
    expected=sorted([26, 27, 58, 59]),
  )
  solver.test_solution(lines=[
    'mask = 000000000000000000000000000000X1001X',
    'mem[42] = 100',
    'mask = 00000000000000000000000000000000X0XX',
    'mem[26] = 1',
  ], expected=208)

test()
print(solver.solve(file="14.input.txt"))
