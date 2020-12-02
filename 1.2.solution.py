import helpers

def parse_input(lines):
  return map(lambda x: int(x), lines)

def solve(data):
  data = sorted(data)
  for a in data:
    s = set()
    for b in data:
      if 2020 - a - b in s:
        return a * b * (2020-a-b)
      s.add(b)
  return None

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=['1721','979','366','299','675','1456'],
    expected=241861950,
  )

test()
print(solver.solve(file="1.input.txt"))
