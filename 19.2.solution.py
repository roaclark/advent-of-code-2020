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

def match_8_11(s, rules):
  j = match_partial(s, rules, '42', 0)
  while j is not None:
    if match_11(s[j:], rules):
      return True
    j = match_partial(s, rules, '42', j)
  return False

def match_11(s, rules):
  match_cnt = 0
  j = 0
  match = True
  while match:
    k = match_partial(s, rules, '42', j)
    if k is None:
      match = False
    else:
      match_cnt += 1
      j = k
  if not match_cnt:
    return False
  for _ in range(match_cnt):
    j = match_partial(s, rules, '31', j)
    if j is None or j > len(s):
      return False
  return j == len(s)

def match_partial(s, rules, rule, i):
  if rule in {'0', '8', '11'}:
    raise Exception('Assumption violated')
  if i >= len(s):
    return None
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

def solve(inp):
  rules, strings = inp
  return len([s for s in strings if match_8_11(s, rules)])

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=[
      '42: 9 14 | 10 1',
      '9: 14 27 | 1 26',
      '10: 23 14 | 28 1',
      '1: "a"',
      '11: 42 31',
      '5: 1 14 | 15 1',
      '19: 14 1 | 14 14',
      '12: 24 14 | 19 1',
      '16: 15 1 | 14 14',
      '31: 14 17 | 1 13',
      '6: 14 14 | 1 14',
      '2: 1 24 | 14 4',
      '0: 8 11',
      '13: 14 3 | 1 12',
      '15: 1 | 14',
      '17: 14 2 | 1 7',
      '23: 25 1 | 22 14',
      '28: 16 1',
      '4: 1 1',
      '20: 14 14 | 1 15',
      '3: 5 14 | 16 1',
      '27: 1 6 | 14 18',
      '14: "b"',
      '21: 14 1 | 1 14',
      '25: 1 1 | 1 14',
      '22: 14 14',
      '8: 42',
      '26: 14 22 | 1 20',
      '18: 15 15',
      '7: 14 5 | 1 21',
      '24: 14 1',
      '',
      'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
      'bbabbbbaabaabba',
      'babbbbaabbbbbabbbbbbaabaaabaaa',
      'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
      'bbbbbbbaaaabbbbaaabbabaaa',
      'bbbababbbbaaaaaaaabbababaaababaabab',
      'ababaaaaaabaaab',
      'ababaaaaabbbaba',
      'baabbaaaabbaaaababbaababb',
      'abbbbabbbbaaaababbbbbbaaaababb',
      'aaaaabbaabaaaaababaa',
      'aaaabbaaaabbaaa',
      'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
      'babaaabbbaaabaababbaabababaaab',
      'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
    ],
    expected=12,
  )

test()
print(solver.solve(file="19.input.txt"))
