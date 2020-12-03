import helpers
from functools import reduce

def parse_input(lines):
  return lines

def check_slope(data, col_step, row_step):
  res = 0
  height, width = len(data), len(data[0])
  for i, row in enumerate(range(0, height, row_step)):
    col = i * col_step
    if data[row][col % width] == '#':
      res += 1
  return res

def solve(data):
  hits = map(lambda s: check_slope(data, s[0], s[1]), [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
  ])
  return reduce(lambda x, y: x * y, hits)

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      '..##.......',
      '#...#...#..',
      '.#....#..#.',
      '..#.#...#.#',
      '.#...##..#.',
      '..#.##.....',
      '.#.#.#....#',
      '.#........#',
      '#.##...#...',
      '#...##....#',
      '.#..#...#.#',
    ],
    expected=336,
  )

test()
print(solver.solve(file="3.input.txt"))
