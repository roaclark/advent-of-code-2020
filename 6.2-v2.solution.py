import helpers
from functools import reduce
from copy import deepcopy

class State:
  def __init__(self):
    self.ans = 0
    self.first_char = True
    self.first_member = True
    self.prev_group_common = set()
    self.next_group_common = set()

  def pretty_print(self):
    print('State')
    print('  ans:', self.ans)
    print('  first_char:', self.first_char)
    print('  first_member:', self.first_member)
    print('  prev_group_common:', ','.join(self.prev_group_common))
    print('  next_group_common:', ','.join(self.next_group_common))


def update_state(state, char, debug=False):
  if debug:
    state.pretty_print()
    print('Next char:', '\\n' if char == '\n' else char)
  if char == '\n':
    if state.first_char:
      # empty line, finished group
      next_state = State()
      next_state.ans = state.ans + len(state.prev_group_common)
      return next_state
    else:
      # end of member
      next_state = State()
      next_state.ans = state.ans
      next_state.first_member = False
      next_state.prev_group_common = set(state.next_group_common)
      return next_state
  # character a-z
  next_state = deepcopy(state)
  if state.first_member or char in state.prev_group_common:
    next_state.next_group_common.add(char)
  next_state.first_char = False
  return next_state


def solve(input):
  final_state = reduce(update_state, input, State())
  final_state = update_state(final_state, '\n')
  final_state = update_state(final_state, '\n')
  return final_state.ans
  

def test():
  helpers.assert_equals(3, solve('\n'.join([
    'abcx',
    'abcy',
    'abcz',
  ])))
  helpers.assert_equals(6, solve('\n'.join([
    'abc',
    '',
    'a',
    'b',
    'c',
    '',
    'ab',
    'ac',
    '',
    'a',
    'a',
    'a',
    'a',
    '',
    'b',
  ])))

test()
with open("6.input.txt") as f:
  inp = f.read()
print(solve(inp))
