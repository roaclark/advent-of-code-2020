import helpers

def parse_input(lines):
  return map(lambda x: int(x), lines)

def solve(data):
  s = set()
  for n in data:
    if 2020 - n in s:
      return n * (2020-n)
    s.add(n)
  return None

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=['1721','979','366','299','675','1456'],
    expected=514579,
  )

test()
print(solver.solve(file="1.input.txt"))
