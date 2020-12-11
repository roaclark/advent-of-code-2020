import helpers

def parse_input(lines):
  return [int(v) for v in lines]

def solve(inp):
  adapters = sorted(inp)
  prev = [(0,1)]
  for v in adapters:
    prev = [x for x in prev if x[0] > v - 4]
    prev += [(v, sum(x[1] for x in prev))]
  return prev[-1][1]

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      '16',
      '10',
      '15',
      '5',
      '1',
      '11',
      '7',
      '19',
      '6',
      '12',
      '4',
    ],
    expected=8,
  )
  solver.test_solution(
    lines=[
      '28',
      '33',
      '18',
      '42',
      '31',
      '14',
      '46',
      '20',
      '48',
      '47',
      '24',
      '23',
      '49',
      '45',
      '19',
      '38',
      '39',
      '11',
      '1',
      '32',
      '25',
      '35',
      '8',
      '17',
      '7',
      '9',
      '4',
      '2',
      '34',
      '10',
      '3',
    ],
    expected=19208,
  )

test()
print(solver.solve(file="10.input.txt"))
