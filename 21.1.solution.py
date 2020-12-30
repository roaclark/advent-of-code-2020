import helpers

def parse_input(lines):
  foods = []
  for l in lines:
    ing, al = l[:-1].split('(contains ')
    ing = set(ing.split(' '))
    al = set(al.split(', '))
    foods.append((ing, al))
  return foods

def solve(foods):
  al_map = {}
  for f in foods:
    ing, al = f
    for a in al:
      if a in al_map:
        al_map[a] = al_map[a] & ing
      else:
        al_map[a] = ing
  al_ings = set()
  for k in al_map:
    al_ings |= al_map[k]
  return len([ing for ings, _al in foods for ing in ings if ing not in al_ings])

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=[
      'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
      'trh fvjkl sbzzf mxmxvkd (contains dairy)',
      'sqjhc fvjkl (contains soy)',
      'sqjhc mxmxvkd sbzzf (contains fish)',
    ],
    expected=5,
  )

test()
print(solver.solve(file="21.input.txt"))
