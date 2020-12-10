import helpers

def parse_input(lines):
  return [int(v) for v in lines]

def get_number(inp, preamble=25):
  # This would be better off as a doubly-linked list
  prev = sorted(enumerate(inp[:preamble]), key=lambda x: x[1])
  for i in range(preamble, len(inp)):
    v = inp[i]
    a, b = 0, preamble - 1
    while a <= b and prev[a][1] + prev[b][1] != v:
      if prev[a][1] + prev[b][1] < v:
        a += 1
      else:
        b -= 1
    if a > b:
      return i
    prev.remove((i-preamble, inp[i-preamble]))
    prev.append((i, v))
    prev.sort(key=lambda x: x[1])
  return None

def solve(inp, preamble=25):
  ind = get_number(inp, preamble)
  tot = inp[ind]
  a, b, cum = 0, 0, inp[0]
  while cum != tot:
    if cum < tot:
      b += 1
      cum += inp[b]
    else:
      cum -= inp[a]
      a += 1
      if b < a:
        b += 1
        cum += inp[b]
  rng = inp[a:b]
  return min(rng) + max(rng)


solver = helpers.Solver(parse_input, solve)
def test():
  test_solver = helpers.Solver(parse_input, lambda inp: solve(inp, preamble=5))
  test_solver.test_solution(
    lines=[
      '35',
      '20',
      '15',
      '25',
      '47',
      '40',
      '62',
      '55',
      '65',
      '95',
      '102',
      '117',
      '150',
      '182',
      '127',
      '219',
      '299',
      '277',
      '309',
      '576',
    ],
    expected=62,
  )

test()
print(solver.solve(file="9.input.txt"))
