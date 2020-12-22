import helpers
from collections import defaultdict

def parse_input(lines):
  tiles = {}
  id = None
  tile = []
  for l in lines:
    if not l:
      tiles[id] = tile
      id = None
      tile = []
    elif l.startswith('Tile'):
      id = int(l[5:-1])
    else:
      tile.append(l)
  if tile:
    tiles[id] = tile
  return tiles

def solve(tiles):
  edges = defaultdict(list)
  for k in tiles:
    t = tiles[k]
    edges[t[0]].append(k)
    edges[t[-1]].append(k)
    edges[''.join([l[0] for l in t])].append(k)
    edges[''.join([l[-1] for l in t])].append(k)
  mismatched = defaultdict(int)
  for e in edges:
    rev_e = e[::-1]
    if len(edges[e]) == 1 and not rev_e in edges:
      mismatched[edges[e][0]] += 1
  corners = [k for k in mismatched if mismatched[k] == 2]
  return corners[0] * corners[1] * corners[2] * corners[3]

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=[
      'Tile 2311:',
      '..##.#..#.',
      '##..#.....',
      '#...##..#.',
      '####.#...#',
      '##.##.###.',
      '##...#.###',
      '.#.#.#..##',
      '..#....#..',
      '###...#.#.',
      '..###..###',
      '',
      'Tile 1951:',
      '#.##...##.',
      '#.####...#',
      '.....#..##',
      '#...######',
      '.##.#....#',
      '.###.#####',
      '###.##.##.',
      '.###....#.',
      '..#.#..#.#',
      '#...##.#..',
      '',
      'Tile 1171:',
      '####...##.',
      '#..##.#..#',
      '##.#..#.#.',
      '.###.####.',
      '..###.####',
      '.##....##.',
      '.#...####.',
      '#.##.####.',
      '####..#...',
      '.....##...',
      '',
      'Tile 1427:',
      '###.##.#..',
      '.#..#.##..',
      '.#.##.#..#',
      '#.#.#.##.#',
      '....#...##',
      '...##..##.',
      '...#.#####',
      '.#.####.#.',
      '..#..###.#',
      '..##.#..#.',
      '',
      'Tile 1489:',
      '##.#.#....',
      '..##...#..',
      '.##..##...',
      '..#...#...',
      '#####...#.',
      '#..#.#.#.#',
      '...#.#.#..',
      '##.#...##.',
      '..##.##.##',
      '###.##.#..',
      '',
      'Tile 2473:',
      '#....####.',
      '#..#.##...',
      '#.##..#...',
      '######.#.#',
      '.#...#.#.#',
      '.#########',
      '.###.#..#.',
      '########.#',
      '##...##.#.',
      '..###.#.#.',
      '',
      'Tile 2971:',
      '..#.#....#',
      '#...###...',
      '#.#.###...',
      '##.##..#..',
      '.#####..##',
      '.#..####.#',
      '#..#.#..#.',
      '..####.###',
      '..#.#.###.',
      '...#.#.#.#',
      '',
      'Tile 2729:',
      '...#.#.#.#',
      '####.#....',
      '..#.#.....',
      '....#..#.#',
      '.##..##.#.',
      '.#.####...',
      '####.#.#..',
      '##.####...',
      '##..#.##..',
      '#.##...##.',
      '',
      'Tile 3079:',
      '#.#.#####.',
      '.#..######',
      '..#.......',
      '######....',
      '####.#..#.',
      '.#...#.##.',
      '#.#####.##',
      '..#.###...',
      '..#.......',
      '..#.###...',
    ],
    expected=20899048083289,
  )

test()
print(solver.solve(file="20.input.txt"))