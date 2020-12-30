import helpers
from collections import defaultdict

sea_monster = [
  '                  # ',
  '#    ##    ##    ###',
  ' #  #  #  #  #  #   ',
]

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

def rotate(tile, deg):
  deg = deg % 360
  if deg == 0:
    return tile
  if deg == 90:
    return [''.join(l[i] for l in tile)[::-1] for i in range(len(tile[0]))]
  if deg == 180:
    return [l[::-1] for l in tile[::-1]]
  if deg == 270:
    return [''.join(l[-(i+1)] for l in tile) for i in range(len(tile[0]))]
  raise Exception('Unexpected degree: ' + str(deg))

def flip(tile, horizontal):
  if horizontal:
    return [l[::-1] for l in tile]
  return tile[::-1]

def get_edges(tiles):
  edges = defaultdict(list)
  for k in tiles:
    t = tiles[k]
    edges[t[0]].append((k, 'n'))
    edges[t[-1]].append((k, 's'))
    edges[''.join([l[0] for l in t])].append((k, 'w'))
    edges[''.join([l[-1] for l in t])].append((k, 'e'))
  return edges

def get_corners(edges):
  mismatched = defaultdict(list)
  for e in edges:
    rev_e = e[::-1]
    if len(edges[e]) == 1 and not rev_e in edges:
      key, side = edges[e][0]
      mismatched[key].append(side)
  return [i for i in mismatched.items() if len(i[1]) == 2]

def arrange_corner(key, mismatched, tiles):
  tile = tiles[key]
  d = ''.join(sorted(mismatched))
  if d == 'en':
    return rotate(tile, -90)
  if d == 'es':
    return rotate(tile, 180)
  if d == 'sw':
    return rotate(tile, 90)
  if d == 'nw':
    return tile
  raise Exception('Unexpected mismatched sides: ' + d)

def get_right(tile_t, edges, tiles):
  key, tile = tile_t
  edge = ''.join([l[-1] for l in tile])
  if edge in edges:
    neighbors = [n for n in edges[edge] if n[0] != key]
    if len(neighbors):
      n_key, n_d = neighbors[0]
      if n_d == 'n':
        return (n_key, flip(rotate(tiles[n_key], 90), True))
      if n_d == 'e':
        return (n_key, flip(tiles[n_key], True))
      if n_d == 's':
        return (n_key, rotate(tiles[n_key], 90))
      if n_d == 'w':
        return (n_key, tiles[n_key])
  rev_edge = edge[::-1]
  if rev_edge in edges:
    neighbors = [n for n in edges[rev_edge] if n[0] != key]
    if len(neighbors):
      n_key, n_d = neighbors[0]
      if n_d == 'n':
        return (n_key, rotate(tiles[n_key], -90))
      if n_d == 'e':
        return (n_key, rotate(tiles[n_key], 180))
      if n_d == 's':
        return (n_key, flip(rotate(tiles[n_key], 90), False))
      if n_d == 'w':
        return (n_key, flip(tiles[n_key], False))
  return None

def get_down(tile_t, edges, tiles):
  key, tile = tile_t
  edge = tile[-1]
  if edge in edges:
    neighbors = [n for n in edges[edge] if n[0] != key]
    if len(neighbors):
      n_key, n_d = neighbors[0]
      if n_d == 'n':
        return (n_key, tiles[n_key])
      if n_d == 'e':
        return (n_key, rotate(tiles[n_key], -90))
      if n_d == 's':
        return (n_key, flip(tiles[n_key], False))
      if n_d == 'w':
        return (n_key, flip(rotate(tiles[n_key], 90), True))
  rev_edge = edge[::-1]
  if rev_edge in edges:
    neighbors = [n for n in edges[rev_edge] if n[0] != key]
    if len(neighbors):
      n_key, n_d = neighbors[0]
      if n_d == 'n':
        return (n_key, flip(tiles[n_key], True))
      if n_d == 'e':
        return (n_key, flip(rotate(tiles[n_key], -90), True))
      if n_d == 's':
        return (n_key, rotate(tiles[n_key], 180))
      if n_d == 'w':
        return (n_key, rotate(tiles[n_key], 90))
  return None

def get_tile_arrangement(corner_key, corner_tile, tiles, edges):
  arranged_tiles = []
  leftmost_t = (corner_key, corner_tile)
  while leftmost_t is not None:
    row = [leftmost_t]
    right_t = get_right(leftmost_t, edges, tiles)
    while right_t is not None:
      row.append(right_t)
      right_t = get_right(right_t, edges, tiles)
    arranged_tiles.append(row)
    leftmost_t = get_down(leftmost_t, edges, tiles)
  return arranged_tiles

def get_map(tile_arrangement):
  def trim_tile(tile):
    return [l[1:-1] for l in tile[1:-1]]
  tile_arrangement = [[trim_tile(t) for _k, t in r] for r in tile_arrangement]
  final_map = []
  for r in tile_arrangement:
    for i in range(len(r[0])):
      final_map.append(''.join([t[i] for t in r]))
  return final_map

def match(final_map, monster_image, ri, ci):
  for m_ri, row in enumerate(monster_image):
    for m_ci, ch in enumerate(row):
      if ch == '#' and final_map[ri + m_ri][ci + m_ci] != '#':
        return False
  return True

def scan(final_map, monster_image):
  cnt = 0
  for r in range(len(final_map) - len(monster_image) + 1):
    for c in range(len(final_map[0]) - len(monster_image[0]) + 1):
      if match(final_map, monster_image, r, c):
        cnt += 1
  return cnt

def scan_all_sea_monsters(final_map):
  cnt = 0
  for monster in [
    sea_monster,
    rotate(sea_monster, 90),
    rotate(sea_monster, 180),
    rotate(sea_monster, 270),
    flip(sea_monster, True),
    rotate(flip(sea_monster, True), 90),
    rotate(flip(sea_monster, True), 180),
    rotate(flip(sea_monster, True), 270),
  ]:
    cnt += scan(final_map, monster)
  return cnt

def count_hash(tile):
  return sum(sum(c == '#' for c in r) for r in tile)

def solve(tiles):
  edges = get_edges(tiles)
  corners = get_corners(edges)
  corner_key, corner_mimatches = corners[0]
  corner_tile = arrange_corner(corner_key, corner_mimatches, tiles)
  tile_arrangement = get_tile_arrangement(corner_key, corner_tile, tiles, edges)
  final_map = get_map(tile_arrangement)
  monster_count = scan_all_sea_monsters(final_map)
  return count_hash(final_map) - count_hash(sea_monster) * monster_count

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
    expected=273,
  )

test()
print(solver.solve(file="20.input.txt"))
