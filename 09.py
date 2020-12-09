from utils import read_file_int
from itertools import combinations


def part1(data, keylen):
    key = data[:keylen]
    for value in data[keylen:]:
        allsums = [a + b for a, b in combinations(key, 2)]
        if value in allsums:
            key = key[1:] + [value]
        else:
            return value


def part2(data, keylen, value):
    for i in range(len(data)):
        sum_ = 0
        j = i
        values = []
        while sum_ < value:
            sum_ += data[j]
            values.append(data[j])
            j += 1
        if sum_ == value:
            return min(values) + max(values)


print("#--- Encoding Error: part1 ---#")


data = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


assert part1(data, 5) == 127
print(part1(read_file_int("09.txt"), 25))


print("#--- Encoding Error: part2 ---#")

assert part2(data, 5, 127) == 62
print(part2(read_file_int("09.txt"), 25, 1124361034))
