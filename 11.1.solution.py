import helpers
from collections import Counter

def parse_input(lines):
  seats = set()
  for r, l in enumerate(lines):
    for c, v in enumerate(l):
      if v == 'L':
        seats.add((r, c))
  return seats
  
adjacencies = [
  (-1,-1),
  (-1,0),
  (-1,1),
  (0,-1),
  (0,1),
  (1,-1),
  (1,0),
  (1,1),
]
def update_occupied(seat, occupied):
  adj_cnt = sum(1 for adj in adjacencies if (seat[0] + adj[0], seat[1] + adj[1]) in occupied)
  if adj_cnt == 0:
    return True
  if adj_cnt > 3:
    return False
  return seat in occupied

def solve(seats):
  occupied = set()
  while True:
    next_occupied = set(seat for seat in seats if update_occupied(seat, occupied))
    if not occupied.symmetric_difference(next_occupied):
      return len(occupied)
    occupied = next_occupied


solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      'L.LL.LL.LL',
      'LLLLLLL.LL',
      'L.L.L..L..',
      'LLLL.LL.LL',
      'L.LL.LL.LL',
      'L.LLLLL.LL',
      '..L.L.....',
      'LLLLLLLLLL',
      'L.LLLLLL.L',
      'L.LLLLL.LL',
    ],
    expected=37,
  )

test()
print(solver.solve(file="11.input.txt"))
