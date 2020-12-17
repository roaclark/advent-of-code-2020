import helpers

def parse_input(lines):
  fields = []
  i = 0
  while lines[i]:
    name, ranges = lines[i].split(': ')
    ranges = [tuple(int(x) for x in rng.split('-')) for rng in ranges.split(' or ')]
    fields.append((name, ranges))
    i += 1
  ticket = [int(x) for x in lines[i+2].split(',')]
  other_tickets = [[int(x) for x in ticket.split(',')] for ticket in lines[i+5:]]
  return (fields, ticket, other_tickets)

def validate_v(v, ranges):
  for r in ranges:
    if v >= r[0] and v <= r[1]:
      return True
    elif v < r[0]:
      return False

def solve(inp):
  fields, _ticket, other_tickets = inp
  ranges = sorted(r for f in fields for r in f[1])
  tot = 0
  for ticket in other_tickets:
    for v in ticket:
      if not validate_v(v, ranges):
        tot += v
  return tot

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(lines=[
    'class: 1-3 or 5-7',
    'row: 6-11 or 33-44',
    'seat: 13-40 or 45-50',
    '',
    'your ticket:',
    '7,1,14',
    '',
    'nearby tickets:',
    '7,3,47',
    '40,4,50',
    '55,2,20',
    '38,6,12',
  ], expected=71)

test()
print(solver.solve(file="16.input.txt"))
