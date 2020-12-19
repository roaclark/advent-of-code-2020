import helpers

def parse_input(lines):
  return [l.replace(' ', '') for l in lines]

class Op:
  def __init__(self, op):
    self.a = None
    self.b = None
    self.op = op

def shunting_yard(line):
  op_stack = []
  out_queue = []
  for tok in line:
    if tok == '(':
      op_stack.append(tok)
    elif tok == ')':
      op = op_stack.pop()
      while op != '(':
        out_queue.append(op)
        op = op_stack.pop()
    elif tok == '*' or tok == '+':
      if tok == '*':
        while op_stack and op_stack[-1] == '+':
          out_queue.append(op_stack.pop())
      op_stack.append(tok)
    else:
      out_queue.append(int(tok))
  while op_stack:
    out_queue.append(op_stack.pop())
  return out_queue

def eval_polish(out_queue):
  v = out_queue.pop()
  if v == '+':
    a = eval_polish(out_queue)
    b = eval_polish(out_queue)
    return a + b
  if v == '*':
    a = eval_polish(out_queue)
    b = eval_polish(out_queue)
    return a * b
  return v

def eval(line):
  out_queue = shunting_yard(line)
  return eval_polish(out_queue)

def solve(lines):
  return sum(eval(l) for l in lines)

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(lines=['1 + (2 * 3) + (4 * (5 + 6))'], expected=51)
  solver.test_solution(lines=['2 * 3 + (4 * 5)'], expected=46)
  solver.test_solution(lines=['5 + (8 * 3 + 9 + 3 * 4 * 3)'], expected=1445)
  solver.test_solution(lines=['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'], expected=669060)
  solver.test_solution(lines=['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'], expected=23340)

test()
print(solver.solve(file="18.input.txt"))
