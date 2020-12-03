import helpers

def parse_input(lines):
  return lines

def solve(data):
  res = 0
  height, width = len(data), len(data[0])
  for row in range(height):
    col = row * 3
    if data[row][col % width] == '#':
      res += 1
  return res

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
    expected=7,
  )

test()
print(solver.solve(file="3.input.txt"))
