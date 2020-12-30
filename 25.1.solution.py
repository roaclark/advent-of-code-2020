import helpers
from collections import defaultdict

subject_number = 7
remainder = 20201227

def parse_input(lines):
  card_key, door_key = int(lines[0]), int(lines[1])
  return card_key, door_key

def step(v, sub=subject_number):
  return (v * sub) % remainder

def solve(inp):
  card_key, door_key = inp
  loop_card, loop_door = None, None
  loop_count, v = 0, 1
  while loop_card is None or loop_door is None:
    v = step(v)
    loop_count += 1
    if v == card_key:
      loop_card = loop_count
    if v == door_key:
      loop_door = loop_count
  res = 1
  for _ in range(min(loop_card, loop_door)):
    res = step(res, v)
  return res

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=[
      '5764801',
      '17807724',
    ],
    expected=14897079,
  )

test()
print(solver.solve(file="25.input.txt"))
