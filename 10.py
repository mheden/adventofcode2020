from utils import read_file_int
from functools import lru_cache


def part1(data):
    joltage = 0
    diffs = {}
    data += [max(data) + 3]
    for adapter in sorted(data):
        diff = adapter - joltage
        diffs[diff] = diffs.get(diff, 0) + 1
        joltage = adapter
    return diffs.get(1, 0) * diffs.get(3, 0)


def part2(data):
    data = sorted(data)
    data = [0] + data + [data[-1] + 3]

    @lru_cache(maxsize=None)
    def traverse(adapter, data):
        if len(data) == 0:
            return 1
        candidates = 0
        subtree = 0
        for i, value in enumerate(data):
            if value > adapter + 3:
                break
            candidates += 1
            subtree += traverse(value, tuple(data[(i + 1) :]))
        if candidates == 0:
            return 0
        return subtree

    a = traverse(data[0], tuple(data[1:]))
    return a


print("#--- Adapter Array: part1 ---#")

data1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
data2 = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
]

assert part1(data1.copy()) == (7 * 5)
assert part1(data2.copy()) == (22 * 10)
print(part1(read_file_int("10.txt")))


print("#--- Adapter Array: part2 ---#")

assert part2(data1) == 8
assert part2(data2) == 19208
print(part2(read_file_int("10.txt")))
