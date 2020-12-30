import helpers

def parse_input(lines):
  d_sz = (len(lines) - 3) // 2
  deck1 = [int(c) for c in lines[1:d_sz+1]]
  deck2 = [int(c) for c in lines[d_sz+3:]]
  return deck1, deck2

def solve(inp):
  deck1, deck2 = inp
  while deck1 and deck2:
    c1, c2 = deck1.pop(0), deck2.pop(0)
    if c1 > c2:
      deck1.append(c1)
      deck1.append(c2)
    else:
      deck2.append(c2)
      deck2.append(c1)
  winner = deck1 or deck2
  return sum(c * (i+1) for i, c in enumerate(winner[::-1]))

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=['Player 1:', '9', '2', '6', '3', '1', '', 'Player 2:', '5', '8', '4', '7', '10'],
    expected=306,
  )

test()
print(solver.solve(file="22.input.txt"))
