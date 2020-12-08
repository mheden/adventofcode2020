from utils import read_file_groups


def yeses(groups):
    result = []
    for group in groups:
        result += [set(list(group.pop()))]
        for entry in group:
            result[-1] |= set(list(entry))
    return sum(map(len, result))


def yeses2(groups):
    result = []
    for group in groups:
        result += [set(list(group.pop()))]
        for entry in group:
            result[-1] &= set(list(entry))
    return sum(map(len, result))


print("#--- Custom Customs: part1 ---#")

groups = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]

assert yeses(groups) == 11
print(yeses(read_file_groups("06.txt")))


print("#--- Custom Customs: part2 ---#")

assert yeses2(groups) == 6
print(yeses2(read_file_groups("06.txt")))
