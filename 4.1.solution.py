import helpers

expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def parse_input(lines):
  passports = []
  passport = {}
  for line in lines:
    if line.strip() == '':
      passports.append(passport)
      passport = {}
    else:
      for field in line.split(' '):
        key, val = field.split(':')
        passport[key] = val
  passports.append(passport)
  return passports

def solve(passports):
  return len([pp for pp in passports if all(k in pp for k in expected_fields)])

solver = helpers.Solver(parse_input, solve)
def test():
  solver.test_solution(
    lines=[
      'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
      'byr:1937 iyr:2017 cid:147 hgt:183cm',
      '',
      'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
      'hcl:#cfa07d byr:1929',
      '',
      'hcl:#ae17e1 iyr:2013',
      'eyr:2024',
      'ecl:brn pid:760753108 byr:1931',
      'hgt:179cm',
      '',
      'hcl:#cfa07d eyr:2025 pid:166559648',
      'iyr:2011 ecl:brn hgt:59in',
    ],
    expected=2,
  )

test()
print(solver.solve(file="4.input.txt"))
