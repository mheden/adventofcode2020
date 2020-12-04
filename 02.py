from utils import read_file
from collections import Counter


def parse_input(row):
    range_, letter, password = row.split(" ")
    lower, upper = map(int, range_.split("-"))
    return lower, upper, letter[0], password


def is_password_valid(row):
    lower, upper, letter, password = parse_input(row)
    c = Counter(password)
    return lower <= c[letter] <= upper


def is_password_valid2(row):
    pos1, pos2, letter, password = parse_input(row)
    return (password[pos1 - 1] == letter) != (password[pos2 - 1] == letter)


print("#--- part1 ---#")

assert is_password_valid("1-3 a: abcde") is True
assert is_password_valid("1-3 b: cdefg") is False
assert is_password_valid("2-9 c: ccccccccc") is True


print(sum([is_password_valid(row) for row in read_file("02.txt")]))


print("#--- part2 ---#")

assert is_password_valid2("1-3 a: abcde") is True
assert is_password_valid2("1-3 b: cdefg") is False
assert is_password_valid2("2-9 c: ccccccccc") is False

print(sum([is_password_valid2(row) for row in read_file("02.txt")]))
