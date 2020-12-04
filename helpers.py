def read_input_file(filename):
    lines = None
    with open(filename) as f:
      lines = f.readlines()
    return [l.strip() for l in lines]

def assert_equals(expected, ans):
  assert expected == ans, 'Expected {0} but got {1}'.format(expected, ans)

class Solver:
  def __init__(self, parser, solver):
    self.parser = parser
    self.solver = solver    

  def solve(self, file=None, lines=None, data=None):
    if data is not None:
      return self.solver(data)
    if lines is not None:
      data = self.parser(lines)
      return self.solver(data)
    if file is not None:
      lines = read_input_file(file)
      data = self.parser(lines)
      return self.solver(data)
    return self.solver(None)

  def test_solution(self, lines=None, data=None, expected=None):
    ans = self.solve(lines=lines, data=data)
    assert_equals(expected, ans)
