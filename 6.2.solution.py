import helpers
from collections import Counter

def parse_input(lines):
  groups = []
  group = []
  for line in lines:
    if line:
      group.append(line)
    else:
      groups.append(group)
      group = []
  groups.append(group)
  return groups

def solve(groups):
  return sum(len([q for q, count in Counter(''.join(group)).items() if count == len(group)]) for group in groups)

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      'abcx',
      'abcy',
      'abcz',
    ],
    expected=3,
  )
  solver.test_solution(
    lines=[
      'abc',
      '',
      'a',
      'b',
      'c',
      '',
      'ab',
      'ac',
      '',
      'a',
      'a',
      'a',
      'a',
      '',
      'b',
    ],
    expected=6,
  )

test()
print(solver.solve(file="6.input.txt"))
