from utils import read_file
from grid import Grid


def part1(data, num=6):
    def iterate(g):
        g.update_limits()
        result = Grid(dim=g.dim, emptyvalue=g.emptyvalue)
        for z in range(g.limits["min"][2] - 1, g.limits["max"][2] + 2):
            for y in range(g.limits["min"][1] - 1, g.limits["max"][1] + 2):
                for x in range(g.limits["min"][0] - 1, g.limits["max"][0] + 2):
                    n = g.neighbours((x, y, z))
                    value = g.get((x, y, z))
                    if value == "#" and (2 <= n.count("#") <= 3):
                        result.set((x, y, z), "#")
                    elif value == "." and n.count("#") == 3:
                        result.set((x, y, z), "#")
                    else:
                        result.set((x, y, z), ".")
        return result

    g = Grid(dim=3, emptyvalue=".")
    y = 0
    for row in data:
        for x, c in enumerate(row):
            g.set((x, y, 0), c)
        y += 1

    for _ in range(num):
        g = iterate(g)
    return g.items["#"]


def part2(data, num=6):
    def iterate(g):
        g.update_limits()
        result = Grid(dim=g.dim, emptyvalue=g.emptyvalue)
        for w in range(g.limits["min"][3] - 1, g.limits["max"][3] + 2):
            for z in range(g.limits["min"][2] - 1, g.limits["max"][2] + 2):
                for y in range(g.limits["min"][1] - 1, g.limits["max"][1] + 2):
                    for x in range(g.limits["min"][0] - 1, g.limits["max"][0] + 2):
                        n = g.neighbours((x, y, z, w))
                        value = g.get((x, y, z, w))
                        if value == "#" and (2 <= n.count("#") <= 3):
                            result.set((x, y, z, w), "#")
                        elif value == "." and n.count("#") == 3:
                            result.set((x, y, z, w), "#")
                        else:
                            result.set((x, y, z, w), ".")
        return result

    g = Grid(dim=4, emptyvalue=".")
    y = 0
    for row in data:
        for x, c in enumerate(row):
            g.set((x, y, 0, 0), c)
        y += 1

    for _ in range(num):
        g = iterate(g)
    return g.items["#"]


print("#--- Conway Cubes: part1 ---#")

print(part1(read_file("17.txt")))


print("#--- Conway Cubes: part2 ---#")

print(part2(read_file("17.txt")))
