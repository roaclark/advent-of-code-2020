import helpers
from collections import Counter

def parse_input(lines):
  seats = set()
  spots = set()
  for r, l in enumerate(lines):
    for c, v in enumerate(l):
      if v == 'L':
        seats.add((r, c))
      spots.add((r, c))
  return seats, spots
  
adj_dir = {
  (-1,-1),
  (-1,0),
  (-1,1),
  (0,-1),
  (0,1),
  (1,-1),
  (1,0),
  (1,1),
}
def add_dir(seat, d):
  return (seat[0] + d[0], seat[1] + d[1])

def get_nearest_neighbor(seat, d, seats, spots):
  next_seat = add_dir(seat, d)
  while next_seat in spots:
    if next_seat in seats:
      return next_seat
    next_seat = add_dir(next_seat, d)
  return None

def get_neighbors(seat, seats, spots):
  neighbors = (get_nearest_neighbor(seat, d, seats, spots) for d in adj_dir)
  return set(n for n in neighbors if n is not None)

def make_neighbor_map(seats, spots):
  return {s: get_neighbors(s, seats, spots) for s in seats}

def update_occupied(seat, occupied, neighbors):
  occ_cnt = sum(1 for n in neighbors if n in occupied)
  if occ_cnt == 0:
    return True
  if occ_cnt > 4:
    return False
  return seat in occupied

def solve(inp):
  seats, spots = inp
  occupied = set()
  neighbor_map = make_neighbor_map(seats, spots)
  while True:
    next_occupied = set(seat for seat in seats if update_occupied(seat, occupied, neighbor_map[seat]))
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
    expected=26,
  )

test()
print(solver.solve(file="11.input.txt"))
