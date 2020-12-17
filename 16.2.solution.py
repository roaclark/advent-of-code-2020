import helpers
from functools import reduce

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
  return False
  
def validate_ticket(ticket, ranges):
  for v in ticket:
    if not validate_v(v, ranges):
      return False
  return True

def possibilities_v(v, possible_fields):
  return [f for f in possible_fields if validate_v(v, f[1])]

def possibilities_t(ticket, field_possibilities):
  return [possibilities_v(v, fields) for v, fields in zip(ticket, field_possibilities)]

def get_mapping(field_possibilities, used_fields=set()):
  mapping = [None for _ in field_possibilities]
  slots_to_compute = set(range(len(field_possibilities)))
  while slots_to_compute:
    resolved = set()
    for i in slots_to_compute:
      if len(field_possibilities[i]) == 1:
        field = list(field_possibilities[i])[0]
        mapping[i] = field
        resolved.add(i)
        for possible_fields in field_possibilities:
          if field in possible_fields:
            possible_fields.remove(field)
    slots_to_compute = slots_to_compute.difference(resolved)
  return mapping

def get_field_list(fields, ticket, other_tickets):
  fields = [(f[0], sorted(f[1])) for f in fields]
  all_ranges = sorted(r for f in fields for r in f[1])
  valid_tickets = [t for t in other_tickets if validate_ticket(t, all_ranges)] + [ticket]
  field_possibilities = [list(fields) for _ in ticket]
  for valid_ticket in valid_tickets:
    field_possibilities = possibilities_t(valid_ticket, field_possibilities)
  field_possibilities = [set(f[0] for f in pf) for pf in field_possibilities]
  return get_mapping(field_possibilities)


def solve(inp):
  fields, ticket, other_tickets = inp
  mapped_fields = get_field_list(fields, ticket, other_tickets)
  departure_values = [v for f, v in zip(mapped_fields, ticket) if f.startswith('departure')]
  return reduce(lambda a, b: a * b, departure_values)

solver = helpers.Solver(parse_input, solve)
def test():
  helpers.assert_equals(
    ans=get_field_list(
      [
        ('class', [(0,1), (4,19)]),
        ('row', [(0,5), (8,19)]),
        ('seat', [(0,13), (16,19)]),
      ],
      [11,12,13],
      [
        [3,9,18],
        [15,1,5],
        [5,14,9],
      ]
    ),
    expected=['row', 'class', 'seat']
  )

test()
print(solver.solve(file="16.input.txt"))
