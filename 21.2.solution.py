import helpers

def parse_input(lines):
  foods = []
  for l in lines:
    ing, al = l[:-1].split(' (contains ')
    ing = set(ing.split(' '))
    al = set(al.split(', '))
    foods.append((ing, al))
  return foods

def isolate_als(al_map):
  al_to_ing = {}
  solved_ings = set()
  while len(al_to_ing) != len(al_map):
    progress = False
    for al in al_map:
      if al not in al_to_ing:
        poss = al_map[al] - solved_ings
        if len(poss) == 1:
          ing = list(poss)[0]
          al_to_ing[al] = ing
          solved_ings.add(ing)
          progress = True
    if not progress:
      raise Exception('No solution found')
  return al_to_ing

def solve(foods):
  al_map = {}
  for f in foods:
    ing, al = f
    for a in al:
      if a in al_map:
        al_map[a] = al_map[a] & ing
      else:
        al_map[a] = ing
  al_to_ing = isolate_als(al_map)
  return ','.join(ing for _al, ing in sorted(al_to_ing.items()))

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=[
      'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
      'trh fvjkl sbzzf mxmxvkd (contains dairy)',
      'sqjhc fvjkl (contains soy)',
      'sqjhc mxmxvkd sbzzf (contains fish)',
    ],
    expected='mxmxvkd,sqjhc,fvjkl',
  )

test()
print(solver.solve(file="21.input.txt"))
