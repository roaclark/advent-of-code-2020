import helpers

def parse_input(lines):
  return [l.replace(' ', '') for l in lines]

ops = {
  '+': lambda a, b: a + b,
  '*': lambda a, b: a * b,
}
def apply_op(op, a, b):
  return ops[op](a, b) if op is not None and a is not None else b

def eval_to_paren(line):
  v = None
  op = None
  ch = next(line)
  while ch != ')':
    if ch == '(':
      next_v, line = eval_to_paren(line)
      v = apply_op(op, v, next_v)
    elif ch == '*' or ch == '+':
      op = ch
    else:
      v = apply_op(op, v, int(ch))
    ch = next(line)
  return v, line

def eval(line):
  return eval_to_paren(iter(line + ')'))[0]

def solve(lines):
  return sum(eval(l) for l in lines)

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(lines=['2 * 3 + (4 * 5)'], expected=26)
  solver.test_solution(lines=['5 + (8 * 3 + 9 + 3 * 4 * 3)'], expected=437)
  solver.test_solution(lines=['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'], expected=12240)
  solver.test_solution(lines=['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'], expected=13632)

test()
print(solver.solve(file="18.input.txt"))
