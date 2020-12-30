import helpers
from collections import defaultdict

def parse_input(lines):
  actives = set()
  for r, line in enumerate(lines):
    for c, val in enumerate(line):
      if val == '#':
        actives.add((r, c, 0, 0))
  return actives

def cycle(actives):
  scores = defaultdict(int)
  for act in actives:
    for i in range(-1, 2):
      for j in range(-1, 2):
        for k in range(-1, 2):
          for l in range(-1, 2):
            if i or j or k or l:
              scores[(act[0]+i, act[1]+j, act[2]+k, act[3]+l)] += 1
  return set(k for k in scores if scores[k] == 3 or (scores[k] == 2 and k in actives))

def solve(inp):
  actives = inp
  for _ in range(6):
    actives = cycle(actives)
  return len(actives)

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      '.#.',
      '..#',
      '###',
    ],
    expected=848
  )

test()
print(solver.solve(file="17.input.txt"))
