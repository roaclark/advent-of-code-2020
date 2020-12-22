import helpers

def parse_input(lines):
  d_sz = (len(lines) - 3) // 2
  deck1 = [int(c) for c in lines[1:d_sz+1]]
  deck2 = [int(c) for c in lines[d_sz+3:]]
  return deck1, deck2

# Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.

def play_game(deck1, deck2):
  prev_states = set()
  while deck1 and deck2:
    state = (tuple(deck1), tuple(deck2))
    if state in prev_states:
      return 1, deck1, deck2
    else:
      prev_states.add(state)
    c1, c2 = deck1.pop(0), deck2.pop(0)
    if len(deck1) >= c1 and len(deck2) >= c2:
      winner = play_game(deck1[:c1], deck2[:c2])[0]
    else:
      winner = 1 if c1 > c2 else 2
    if winner == 1:
      deck1.append(c1)
      deck1.append(c2)
    else:
      deck2.append(c2)
      deck2.append(c1)
  return (1 if deck1 else 2), deck1, deck2

def solve(inp):
  deck1, deck2 = inp
  winner, deck1, deck2 = play_game(deck1, deck2)
  win_deck = deck1 if winner == 1 else deck2
  return sum(c * (i+1) for i, c in enumerate(win_deck[::-1]))

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=['Player 1:', '9', '2', '6', '3', '1', '', 'Player 2:', '5', '8', '4', '7', '10'],
    expected=291,
  )

test()
print(solver.solve(file="22.input.txt"))
