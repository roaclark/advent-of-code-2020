import helpers

def binary(val, z, o):
  return int(val.replace(z, '0').replace(o, '1'), 2)

def parse_input(lines):
  return [binary(line[:7], 'F', 'B') * 8 + binary(line[7:], 'L', 'R') for line in lines]

def solve(seats):
  return max(seats)

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      'BFFFBBFRRR',
    ],
    expected=567,
  )
  solver.test_solution(
    lines=[
      'BFFFBBFRRR',
      'FFFBBBFRRR',
      'BBFFBBFRLL',
    ],
    expected=820,
  )

test()
print(solver.solve(file="5.input.txt"))
