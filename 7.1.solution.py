import helpers
import re
from collections import defaultdict

def parse_input(lines):
  graph = {}
  for line in lines:
    node, children = line.split(' bags contain ')
    children = children[:-1]
    if children == 'no other bags':
      graph[node] = []
    else:
      graph[node] = [re.match(r'(\d+) (.*) bags?', child).groups() for child in children.split(', ')]
  return graph

def solve(graph):
  reverse_graph = defaultdict(set)
  for k in graph:
    for ch in graph[k]:
      reverse_graph[ch[1]].add(k)
  stack = ['shiny gold']
  visited = set()
  while stack:
    curr = stack.pop()
    if curr not in visited:
      visited.add(curr)
      stack += reverse_graph[curr]
  return len(visited) - 1


solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      'light red bags contain 1 bright white bag, 2 muted yellow bags.',
      'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
      'bright white bags contain 1 shiny gold bag.',
      'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
      'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
      'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
      'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
      'faded blue bags contain no other bags.',
      'dotted black bags contain no other bags.',
    ],
    expected=4,
  )

test()
print(solver.solve(file="7.input.txt"))
