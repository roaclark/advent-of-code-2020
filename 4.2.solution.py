import helpers
import re

expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def in_range(val, min, max):
  return val <= max and val >= min

def validate_range(field, min, max):
  def validate(pp):
    return in_range(int(pp[field]), min, max)
  return validate

def validate_height(pp):
  hgt = pp['hgt']
  if re.match(r'^\d+cm$', hgt):
    return in_range(int(hgt[:-2]), 150, 193)
  if re.match(r'^\d+in$', hgt):
    return in_range(int(hgt[:-2]), 59, 76)
  return False

validators = [
  validate_range('byr', 1920, 2002),
  validate_range('iyr', 2010, 2020),
  validate_range('eyr', 2020, 2030),
  validate_height,
  lambda pp: bool(re.match(r'#[0-9a-f]{6}$', pp['hcl'])),
  lambda pp: pp['ecl'] in valid_eye_colors,
  lambda pp: bool(re.match(r'\d{9}$', pp['pid'])),
]

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
  for pp in passports:
    if all(k in pp for k in expected_fields):
  return len([pp for pp in passports if all(k in pp for k in expected_fields) and all(validator(pp) for validator in validators)])

solver = helpers.Solver(parse_input, solve)
def test():
  helpers.assert_equals(True, validate_height({'hgt': '60in'}))
  helpers.assert_equals(True, validate_height({'hgt': '190cm'}))
  helpers.assert_equals(False, validate_height({'hgt': '190in'}))
  helpers.assert_equals(False, validate_height({'hgt': '190'}))
  helpers.assert_equals(True, validate_range('byr', 1920, 2002)({'byr': '1920'}))
  helpers.assert_equals(True, validate_range('byr', 1920, 2002)({'byr': '2002'}))
  helpers.assert_equals(False, validate_range('byr', 1920, 2002)({'byr': '2003'}))
  helpers.assert_equals(False, validate_range('byr', 1920, 2002)({'byr': '1919'}))
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
  solver.test_solution(
    lines=[
      'eyr:1972 cid:100',
      'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
      '',
      'iyr:2019',
      'hcl:#602927 eyr:1967 hgt:170cm',
      'ecl:grn pid:012533040 byr:1946',
      '',
      'hcl:dab227 iyr:2012',
      'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
      '',
      'hgt:59cm ecl:zzz',
      'eyr:2038 hcl:74454a iyr:2023',
      'pid:3556412378 byr:2007',
      '',
      'pid:087499704 hgt:58in ecl:grn iyr:2012 eyr:2030 byr:1980',
      'hcl:#623a2f',
    ],
    expected=0,
  )
  solver.test_solution(
    lines=[
      'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
      'hcl:#623a2f',
      '',
      'eyr:2029 ecl:blu cid:129 byr:1989',
      'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
      '',
      'hcl:#888785',
      'hgt:164cm byr:2001 iyr:2015 cid:88',
      'pid:545766238 ecl:hzl',
      'eyr:2022',
      '',
      'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719',
    ],
    expected=4,
  )

test()
print(solver.solve(file="4.input.txt"))
