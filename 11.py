from utils import read_file
import math
from grid import Grid


def part1(data):
    def iterate(g):
        result = Grid(dim=2, emptyvalue="")
        for x, y in g.grid:
            n = g.neighbours((x, y))
            value = g.get((x, y))
            if value == "L" and n.count("#") == 0:
                result.set((x, y), "#")
            elif value == "#" and n.count("#") >= 4:
                result.set((x, y), "L")
            else:
                result.set((x, y), value)
        return result

    last = Grid(dim=2, emptyvalue="")
    y = 0
    for row in data:
        for x, c in enumerate(row):
            last.set((x, y), c)
        y += 1

    i = 0
    current = iterate(last)
    while last != current:
        i += 1
        last = current
        current = iterate(last)
    return current.items["#"]


def part2(data):
    def iterate(g, log=False):
        g.update_limits()
        result = Grid(dim=2, emptyvalue=".")
        for x, y in g.grid:
            v = g.view((x, y))
            value = g.get((x, y))
            if value == "L" and v.count("#") == 0:
                result.set((x, y), "#")
            elif value == "#" and v.count("#") >= 5:
                result.set((x, y), "L")
            else:
                result.set((x, y), value)
        return result

    last = Grid(dim=2, emptyvalue=".")
    y = 0
    for row in data:
        for x, c in enumerate(row):
            last.set((x, y), c)
        y += 1

    i = 1
    current = iterate(last)
    while last != current:
        last = current
        current = iterate(last)
        i += 1
    return current.items["#"]


print("#--- Seating System: part1 ---#")

data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()

assert part1(data) == 37
print(part1(read_file("11.txt")))


print("#--- Seating System: part2 ---#")

assert part2(data) == 26
print(part2(read_file("11.txt")))
