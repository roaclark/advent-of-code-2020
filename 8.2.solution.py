import helpers

class Computer:
  def __init__(self, program):
    self.program = program
    self.ind = 0
    self.acc = 0
  
  def run_instruction(self):
    ins, val = self.program[self.ind].split(' ')
    val = int(val)
    if ins == 'acc':
      self.ind += 1
      self.acc += val
    elif ins == 'jmp':
      self.ind += val
    elif ins == 'nop':
      self.ind += 1
    
  def run_program(self):
    visited = set()
    while self.ind not in visited and self.ind < len(self.program):
      visited.add(self.ind)
      self.run_instruction()
    return self.acc if self.ind == len(self.program) else None


def parse_input(lines):
  return lines

def solve(program):
  for i, cmd in enumerate(program):
    if cmd[:3] == 'nop':
      alt_program = program[:i] + ['jmp' + cmd[3:]] + program[i+1:]
      res = Computer(alt_program).run_program()
      if res is not None:
        return res
    if cmd[:3] == 'jmp':
      alt_program = program[:i] + ['nop' + cmd[3:]] + program[i+1:]
      res = Computer(alt_program).run_program()
      if res is not None:
        return res
  return None


solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      'nop +0',
      'acc +1',
      'jmp +4',
      'acc +3',
      'jmp -3',
      'acc -99',
      'acc +1',
      'jmp -4',
      'acc +6',
    ],
    expected=8,
  )

test()
print(solver.solve(file="8.input.txt"))
