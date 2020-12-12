import helpers

def parse_input(lines):
  return [(v[0], int(v[1:])) for v in lines]

dir_map = {
  'N': (0, 1),
  'E': (1, 0),
  'S': (0, -1),
  'W': (-1, 0),
}
turn_calc = {
  'L': lambda p: (-p[1], p[0]),
  'R': lambda p: (p[1], -p[0]),
}

def add_pos(a, b, m=1):
  return a[0] + b[0] * m, a[1] + b[1] * m

def solve(ins):
  pos = (0,0)
  way = (10, 1)
  for cmd, val in ins:
    if cmd in ('N', 'S', 'E', 'W'):
      way = add_pos(way, dir_map[cmd], val)
    elif cmd == 'F':
      pos = add_pos(pos, way, val)
    elif cmd in ('L', 'R'):
      for _ in range(0, val, 90):
        way = turn_calc[cmd](way)
    else:
      raise 'invalid command: ' + cmd
  return abs(pos[0]) + abs(pos[1])


solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      'F10',
      'N3',
      'F7',
      'R90',
      'F11',
    ],
    expected=286,
  )

test()
print(solver.solve(file="12.input.txt"))
