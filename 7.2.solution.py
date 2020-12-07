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
  memo = {}

  def compute_cost(bag):
    if not graph[bag]:
      return 1
    if bag in memo:
      return memo[bag]
    res = sum(compute_cost(ch) * int(ct) for ct, ch in graph[bag]) + 1
    memo[bag] = res
    return res

  return compute_cost('shiny gold') - 1


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
    expected=32,
  )
  solver.test_solution(
    lines=[
      'shiny gold bags contain 2 dark red bags.',
      'dark red bags contain 2 dark orange bags.',
      'dark orange bags contain 2 dark yellow bags.',
      'dark yellow bags contain 2 dark green bags.',
      'dark green bags contain 2 dark blue bags.',
      'dark blue bags contain 2 dark violet bags.',
      'dark violet bags contain no other bags.',
    ],
    expected=126,
  )

test()
print(solver.solve(file="7.input.txt"))
