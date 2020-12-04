from utils import read_file
import math
import re

REQUIRED_KEYS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
RE_HCL = re.compile(r"^#[0-9a-f]{6}$")
RE_HGT = re.compile(r"^(\d+)(cm|in)$")
RE_PID = re.compile(r"^\d{9}$")


def is_valid(passport):
    data = {}
    passport = passport.strip()
    for item in passport.split(" "):
        k, v = item.split(":")
        data[k] = v
    for r in REQUIRED_KEYS:
        try:
            data[r]
        except Exception:
            return False
    return True


def has_valid_keys(data):
    for r in REQUIRED_KEYS:
        try:
            data[r]
        except Exception:
            return False
    return True


def has_valid_birth_year(data):
    return not (int(data["byr"]) < 1920 or int(data["byr"]) > 2002)


def has_valid_issue_year(data):
    return not (int(data["iyr"]) < 2010 or int(data["iyr"]) > 2020)


def has_valid_expiration_year(data):
    return not (int(data["eyr"]) < 2020 or int(data["eyr"]) > 2030)


def has_valid_height(data):
    m = RE_HGT.match(data["hgt"])
    if not m:
        return False
    if m.group(2) == "cm":
        if int(m.group(1)) < 150 or int(m.group(1)) > 193:
            return False
    elif m.group(2) == "in":
        if int(m.group(1)) < 59 or int(m.group(1)) > 76:
            return False
    return True


def has_valid_hair_color(data):
    return bool(RE_HCL.match(data["hcl"]))


def has_valid_eye_color(data):
    return data["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def has_valid_id(data):
    return bool(RE_PID.match(data["pid"]))


def is_valid2(passport):
    data = {}
    passport = passport.strip()
    for item in passport.split(" "):
        k, v = item.split(":")
        data[k] = v
    return (
        has_valid_keys(data)
        and has_valid_birth_year(data)
        and has_valid_issue_year(data)
        and has_valid_expiration_year(data)
        and has_valid_height(data)
        and has_valid_hair_color(data)
        and has_valid_eye_color(data)
        and has_valid_id(data)
    )


print("#--- part1 ---#")

data = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929",
    "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm",
    "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in",
]

assert sum([is_valid(passport) for passport in data]) == 2
print(sum([is_valid(passport) for passport in read_file("04.txt")]))


print("#--- part2 ---#")

invalid = [
    "eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946",
    "hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007",
]

valid = [
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f",
    "eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
]

assert sum([is_valid2(passport) for passport in invalid]) == 0
assert sum([is_valid2(passport) for passport in valid]) == 4
print(sum([is_valid2(passport) for passport in read_file("04.txt")]))
