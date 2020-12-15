import helpers

def parse_input(lines):
  return int(lines[0]), [int(x) for x in lines[1].split(',') if x != 'x']

def solve(inp):
  start, buses = inp
  bus, wait = min([(id, id - start % id) for id in buses], key=lambda x: x[1])
  return bus * wait


solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      '939',
      '7,13,x,x,59,x,31,19',
    ],
    expected=295,
  )

test()
print(solver.solve(file="13.input.txt"))
