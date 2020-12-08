from collections import namedtuple

BIGNUM = 10 ** 100

Point2d = namedtuple("Point2d", ["x", "y"])
Point3d = namedtuple("Point3d", ["x", "y", "z"])


def manhattan_distance(p0, p1):
    return sum([abs(a - b) for a, b in zip(p0, p1)])


def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines


def read_file_int(filename):
    return map(int, read_file(filename))


def read_file_groups(filename):
    with open(filename) as f:
        groups = []
        for group in f.read().strip().split("\n\n"):
            groups.append(group.split("\n"))
    return groups


def xor(a, b):
    return bool(a) ^ bool(b)


if __name__ == "__main__":
    # print(manhattan_distance(Point2d(1, 2), Point2d(3, 4)))
    # print(manhattan_distance(Point3d(1, 2, 3), Point3d(4, 5, 6)))

    import pprint
    pprint.pprint(read_file_groups('06.txt'))

# TODO:
# - Grid
#
# Reminders:
# - collections.Counter
# - collections.defaultdict
# - collections.deque
# - itertools
