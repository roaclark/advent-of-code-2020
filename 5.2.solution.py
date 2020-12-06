import helpers

def binary(val, z, o):
  return int(val.replace(z, '0').replace(o, '1'), 2)

def parse_input(lines):
  return [binary(line[:7], 'F', 'B') * 8 + binary(line[7:], 'L', 'R') for line in lines]

def solve(seats):
  seats = sorted(seats)
  for i in range(1, len(seats)):
    if seats[i] != seats[i-1] + 1:
      return seats[i] - 1
  return None

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      'FFFFFFFLLR',
      'FFFFFFFLRL',
      'FFFFFFFRLL',
    ],
    expected=3,
  )

test()
print(solver.solve(file="5.input.txt"))
