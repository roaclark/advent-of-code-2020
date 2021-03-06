import helpers
from collections import defaultdict

def parse_input(lines):
  tiles = []
  for l in lines:
    dirs = []
    i = 0
    while i < len(l):
      if l[i] == 'n' or l[i] == 's':
        dirs.append(l[i:i+2])
        i += 2
      else:
        dirs.append(l[i])
        i += 1
    tiles.append(dirs)
  return tiles

dir_map = {
  'ne': lambda x: (x[0] + 1, x[1] + 1),
  'nw': lambda x: (x[0]    , x[1] + 1),
  'se': lambda x: (x[0]    , x[1] - 1),
  'sw': lambda x: (x[0] - 1, x[1] - 1),
  'e':  lambda x: (x[0] + 1, x[1]    ),
  'w':  lambda x: (x[0] - 1, x[1]    ),
}

def solve(tiles):
  floor = defaultdict(bool)
  for tile in tiles:
    loc = (0,0)
    for d in tile:
      loc = dir_map[d](loc)
    floor[loc] = not floor[loc]
  return len([k for k in floor if floor[k]])

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=[
      'sesenwnenenewseeswwswswwnenewsewsw',
      'neeenesenwnwwswnenewnwwsewnenwseswesw',
      'seswneswswsenwwnwse',
      'nwnwneseeswswnenewneswwnewseswneseene',
      'swweswneswnenwsewnwneneseenw',
      'eesenwseswswnenwswnwnwsewwnwsene',
      'sewnenenenesenwsewnenwwwse',
      'wenwwweseeeweswwwnwwe',
      'wsweesenenewnwwnwsenewsenwwsesesenwne',
      'neeswseenwwswnwswswnw',
      'nenwswwsewswnenenewsenwsenwnesesenew',
      'enewnwewneswsewnwswenweswnenwsenwsw',
      'sweneswneswneneenwnewenewwneswswnese',
      'swwesenesewenwneswnwwneseswwne',
      'enesenwswwswneneswsenwnewswseenwsese',
      'wnwnesenesenenwwnenwsewesewsesesew',
      'nenewswnwewswnenesenwnesewesw',
      'eneswnwswnwsenenwnwnwwseeswneewsenese',
      'neswnwewnwnwseenwseesewsenwsweewe',
      'wseweeenwnesenwwwswnew',
    ],
    expected=10,
  )

test()
print(solver.solve(file="24.input.txt"))
