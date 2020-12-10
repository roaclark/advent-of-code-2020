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


def parse_input(lines):
  return lines

def solve(program):
  comp = Computer(program)
  visited = set()
  while comp.ind not in visited:
    visited.add(comp.ind)
    comp.run_instruction()
  return comp.acc


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
    expected=5,
  )

test()
print(solver.solve(file="8.input.txt"))
