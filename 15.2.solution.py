import helpers
from collections import defaultdict
import itertools

def parse_input(lines):
  return [int(v) for v in lines[0].split(',')]

def solve(inp, end=30000000):
  history = {v: i for i, v in enumerate(inp[:-1])}
  prev = inp[-1]
  for t in range(len(inp), end):
    if prev in history:
      history[prev], prev = t - 1, t - history[prev] - 1
    else:
      history[prev], prev = t - 1, 0
  return prev

solver = helpers.Solver(parse_input, solve)
def test():
  helpers.Solver(parse_input, lambda x: solve(x, end=9)).test_solution(lines=['0,3,6'], expected=4)
  helpers.Solver(parse_input, lambda x: solve(x, end=10)).test_solution(lines=['0,3,6'], expected=0)

test()
print(solver.solve(file="15.input.txt"))
