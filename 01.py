from utils import read_file_int
from itertools import combinations


def sum2(lst):
    return [a * b for a, b in combinations(lst, 2) if a + b == 2020].pop()


def sum3(lst):
    return [a * b * c for a, b, c in combinations(lst, 3) if a + b + c == 2020].pop()


print("#--- Report Repair: part1 ---#")

assert sum2([1721, 979, 366, 299, 675, 1456]) == 514579

print(sum2(read_file_int("01.txt")))


print("#--- Report Repair: part2 ---#")

assert sum3([1721, 979, 366, 299, 675, 1456]) == 241861950

print(sum3(read_file_int("01.txt")))
