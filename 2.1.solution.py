import helpers
import re
from collections import Counter

def parse_input(lines):
  line_regex = re.compile(r'(\d+)-(\d+) (\w): (\w*)')
  groups = map(lambda x: line_regex.search(x).groups(), lines)
  return map(lambda x: (int(x[0]), int(x[1]), x[2], x[3]), groups)

def solve(data):
  valid_passwords = 0
  for min_ch, max_ch, ch, password in data:
    ch_count = Counter(password)[ch]
    if (ch_count >= min_ch and ch_count <= max_ch):
      valid_passwords += 1
  return valid_passwords

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc'],
    expected=2,
  )

test()
print(solver.solve(file="2.input.txt"))
