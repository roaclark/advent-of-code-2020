import helpers

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def parse_input(lines):
  line = lines[0]
  node_map = {}
  prev = None
  for v in range(1, 1000001):
    node = Node(int(line[v-1]) if v < 10 else v)
    node_map[node.val] = node
    node.prev = prev
    if prev is not None:
      prev.next = node
    prev = node
  head = node_map[int(line[0])]
  head.prev, prev.next = prev, head
  return head, node_map

def turn(head, node_map):
  removed = head.next
  new_next = removed.next.next.next
  head.next, new_next.prev = new_next, head
  removed_vs = {removed.val, removed.next.val, removed.next.next.val}
  dst_v = (head.val - 1) or 1000000
  while dst_v in removed_vs:
    dst_v = (dst_v - 1) or 1000000
  dest = node_map[dst_v]
  removed.next.next.next, dest.next.prev = dest.next, removed.next.next
  dest.next, removed.prev = removed, dest
  return head.next

def solve(inp, moves=10000000):
  head, node_map = inp
  for _ in range(moves):
    head = turn(head, node_map)
  return node_map[1].next.val * node_map[1].next.next.val

solver = helpers.Solver(parse_input, solve)

def test():
  solver.test_solution(
    lines=['389125467'],
    expected=149245887792,
  )

test()
print(solver.solve(file="23.input.txt"))
