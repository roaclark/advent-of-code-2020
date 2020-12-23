import helpers

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def parse_input(lines):
  node_map = {}
  prev = None
  for ch in lines[0]:
    node = Node(int(ch))
    node_map[node.val] = node
    node.prev = prev
    if prev is not None:
      prev.next = node
    prev = node
  head = node_map[int(lines[0][0])]
  head.prev, prev.next = prev, head
  return head, node_map

def turn(head, node_map):
  removed = head.next
  new_next = removed.next.next.next
  head.next, new_next.prev = new_next, head
  removed_vs = {removed.val, removed.next.val, removed.next.next.val}
  dst_v = (head.val - 1) or 9
  while dst_v in removed_vs:
    dst_v = (dst_v - 1) or 9
  dest = node_map[dst_v]
  removed.next.next.next, dest.next.prev = dest.next, removed.next.next
  dest.next, removed.prev = removed, dest
  return head.next

def solve(inp, moves=100):
  head, node_map = inp
  for _ in range(moves):
    head = turn(head, node_map)
  curr = node_map[1].next
  res = []
  while curr.val != 1:
    res += [str(curr.val)]
    curr = curr.next
  return ''.join(res)

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=['389125467'],
    expected='67384529',
  )

test()
print(solver.solve(file="23.input.txt"))
