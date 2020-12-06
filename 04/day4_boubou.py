import re, sys


class PassportData:

    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

    def set_byr(self, byr):
        self.byr = byr

    def set_iyr(self, iyr):
        self.iyr = iyr

    def set_eyr(self, eyr):
        self.eyr = eyr

    def set_hgt(self, hgt):
        self.hgt = hgt

    def set_hcl(self, hcl):
        self.hcl = hcl

    def set_ecl(self, ecl):
        self.ecl = ecl

    def set_pid(self, pid):
        self.pid = pid

    def set_cid(self, cid):
        self.cid = cid

    def set_passport_param(self, param, value):
        if param == 'byr':
            self.set_byr(value)
        if param == 'iyr':
            self.set_iyr(value)
        if param == 'eyr':
            self.set_eyr(value)
        if param == 'hgt':
            self.set_hgt(value)
        if param == 'hcl':
            self.set_hcl(value)
        if param == 'ecl':
            self.set_ecl(value)
        if param == 'pid':
            self.set_pid(value)
        if param == 'cid':
            self.set_cid(value)

    # def is_valid(self):
    #     if self.byr is None or self.iyr is None or self.eyr is None or self.hgt is None or self.hcl is None \
    #             or self.ecl is None or self.pid is None:
    #         return False
    #     else:
    #         return True

    def is_valid(self):
        if self.byr is None or self.iyr is None or self.eyr is None or self.hgt is None or self.hcl is None \
                or self.ecl is None or self.pid is None:
            return False
        else:
            try:
                if not isinstance(int(self.byr), int) or len(str(self.byr)) != 4 or int(self.byr) < 1920 or int(self.byr) > 2002:
                    return False
                if not isinstance(int(self.iyr), int) or len(str(self.iyr)) != 4 or int(self.iyr) < 2010 or int(self.iyr) > 2020:
                    return False
                if not isinstance(int(self.eyr), int) or len(str(self.eyr)) != 4 or int(self.eyr) < 2020 or int(self.eyr) > 2030:
                    return False
                m = re.match(r'(\d+)(cm|in)', self.hgt)
                if not m or (m.group(2) == 'cm' and (int(m.group(1)) < 150 or int(m.group(1)) > 193)) or (m.group(2) == 'in' and (int(m.group(1)) < 59 or int(m.group(1)) > 76)):
                    return False
                if not re.match(r'#[\da-f]{6}', self.hcl):
                    return False
                if self.ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                    return False
                print(self.pid)
                if not re.match(r'\d{9}', self.pid):
                    print("a")
                    return False
                return True
            except ValueError:
                return False


def parse_line(pp, li):
    re_fields = r'(\w+):([\w#]+)'
    for (key, val) in re.findall(re_fields, li):
        pp.set_passport_param(key, val)


filepath = "input"
with open(filepath, 'r') as f:
    lines = f.readlines()
passport = PassportData()
valid_passports = 0
last_line_empty = False
k = 0
v = []
for line in lines:
    if line.strip() == '':
        if passport.is_valid():
            valid_passports += 1
            v.append(k)
            if k == 96:
                sys.exit()
        k += 1
        passport = PassportData()
        last_line_empty = True
    else:
        parse_line(passport, line)
        last_line_empty = False
if not last_line_empty:
    if passport.is_valid():
        valid_passports += 1
        print(v)
print(valid_passports)
