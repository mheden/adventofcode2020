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


if __name__ == "__main__":
    print(manhattan_distance(Point2d(1, 2), Point2d(3, 4)))
    print(manhattan_distance(Point3d(1, 2, 3), Point3d(4, 5, 6)))


# TODO:
# - Grid
#
# Reminders:
# - collections.Counter
# - collections.defaultdict
# - collections.deque
# - itertools
