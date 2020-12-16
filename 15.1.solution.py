import helpers
from collections import defaultdict
import itertools

def parse_input(lines):
  return [int(v) for v in lines[0].split(',')]

def solve(inp, end=2020):
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
  solver.test_solution(lines=['0,3,6'], expected=436)
  solver.test_solution(lines=['1,3,2'], expected=1)
  solver.test_solution(lines=['2,1,3'], expected=10)
  solver.test_solution(lines=['1,2,3'], expected=27)
  solver.test_solution(lines=['2,3,1'], expected=78)
  solver.test_solution(lines=['3,2,1'], expected=438)
  solver.test_solution(lines=['3,1,2'], expected=1836)

test()
print(solver.solve(file="15.input.txt"))
