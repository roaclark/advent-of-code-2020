import helpers
from functools import reduce

def parse_input(lines):
  return [(int(b), -i) for i, b in enumerate(lines[1].split(',')) if b != 'x']

# i such that (a * i) % b == 1
def mod_1(a, b):
  i = 0
  while True:
    i += 1
    if a * i % b == 1:
      return i

def chinese_remainder(entries):
  total = 0
  lcm = reduce(lambda acc, x: acc * x[0], entries, 1)
  for v, r in entries:
    p = int(lcm / v)
    total += r * mod_1(p, v) * p
  return total % lcm

def solve(buses):
  return chinese_remainder(buses)

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(lines=['', '5,6,7'], expected=5)
  solver.test_solution(lines=['', '5,11'], expected=10)
  solver.test_solution(lines=['', '7,13,x,x,59,x,31,19'], expected=1068781)
  solver.test_solution(lines=['', '17,x,13,19'], expected=3417)
  solver.test_solution(lines=['', '67,7,59,61'], expected=754018)
  solver.test_solution(lines=['', '67,x,7,59,61'], expected=779210)
  solver.test_solution(lines=['', '67,7,x,59,61'], expected=1261476)
  solver.test_solution(lines=['', '1789,37,47,1889'], expected=1202161486)

test()
print(solver.solve(file="13.input.txt"))
