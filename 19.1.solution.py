import helpers

def parse_input(lines):
  lines = iter(lines)
  line = next(lines)
  rules = {}
  while line:
    key, rule = line.split(': ')
    if rule[0] == '"':
      rules[key] = (rule[1:-1], None)
    else:
      options = [opt.split(' ') for opt in rule.split(' | ')]
      rules[key] = (None, options)
    line = next(lines)
  strings = []
  line = next(lines, None)
  while line is not None:
    strings.append(line)
    line = next(lines, None)
  return rules, strings

def match_partial(s, rules, rule, i):
  val, options = rules[rule]
  if val is not None:
    if s[i] == val:
      return i+1
    return None
  for opt in options:
    j = i
    valid = True
    for child in opt:
      if j is not None:
        j = match_partial(s, rules, child, j)
    if j is not None:
      return j
  return None

def match(s, rules):
  m = match_partial(s, rules, '0', 0)
  return m == len(s)

def solve(inp):
  rules, strings = inp
  return len([s for s in strings if match(s, rules)])

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=[
      '0: 4 1 5',
      '1: 2 3 | 3 2',
      '2: 4 4 | 5 5',
      '3: 4 5 | 5 4',
      '4: "a"',
      '5: "b"',
      '',
      'ababbb',
      'bababa',
      'abbbab',
      'aaabbb',
      'aaaabbb',
    ],
    expected=2,
  )

test()
print(solver.solve(file="19.input.txt"))
