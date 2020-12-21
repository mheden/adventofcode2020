from collections import Counter
from itertools import product


class Grid:
    def __init__(self, dim=2, emptyvalue=""):
        self.grid = {}
        self.dim = dim
        self.emptyvalue = emptyvalue
        self.limits = {"min": {}, "max": {}}
        self.items = Counter()
        self.deltas = []
        for delta in product((-1, 0, 1), repeat=dim):
            if any(delta):
                self.deltas.append(delta)

    def update_limits(self):
        for coord in self.grid:
            for dim, value in enumerate(coord):
                if dim not in self.limits["min"]:
                    self.limits["min"][dim] = value
                if dim not in self.limits["max"]:
                    self.limits["max"][dim] = value
                self.limits["min"][dim] = min(self.limits["min"][dim], value)
                self.limits["max"][dim] = max(self.limits["max"][dim], value)

    def set(self, coords, value):
        # assert len(coords) == self.dim
        self.grid[tuple(coords)] = value
        self.items[value] += 1

    def size(self):
        s = 1
        for i in range(len(self.limits["min"])):
            s *= self.limits["max"][i] - self.limits["min"][i] + 1
        return s

    def get(self, coords):
        # assert len(coords) == self.dim
        try:
            return self.grid[tuple(coords)]
        except KeyError:
            return self.emptyvalue

    def neighbours(self, coords):
        # assert len(coords) == self.dim
        n = ""
        for delta in self.deltas:
            n += self.get(a + b for a, b in zip(coords, delta))
        return n

    def view(self, coords):
        v = ""
        for delta in self.deltas:
            c = self.line_of_sight(coords, delta)
            if c != self.emptyvalue:
                v += c
        return v

    def line_of_sight(self, coords, deltas):
        # assert len(coords) == self.dim
        coord = coords
        inside = True
        while inside:
            coord = [a + b for a, b in zip(coord, deltas)]
            for i, c in enumerate(coord):
                if c < self.limits["min"][i] or c > self.limits["max"][i]:
                    inside = False
            if inside:
                c = self.get(coord)
                if c != self.emptyvalue:
                    return c
        return self.emptyvalue

    def print_layer(self, higher_layers=[]):
        higher_layers = list(higher_layers)
        for i, dim in enumerate(higher_layers):
            print("dim(%d)=%d" % (i + 2, dim), end=" ")
        print("")
        for y in range(self.limits["min"][1], self.limits["max"][1] + 1):
            for x in range(self.limits["min"][0], self.limits["max"][0] + 1):
                print("%s" % self.get([x, y] + higher_layers), end="")
            print("")

    def serialize(self):
        return "|".join(["%s%s" % (k, v) for k, v in sorted(self.grid.items())])

    def __eq__(self, other):
        return self.serialize() == other.serialize()


if __name__ == "__main__":
    g = Grid(dim=2, emptyvalue=".")
    data = [
        ".......#.",
        "...#.....",
        ".#.......",
        ".........",
        "..#L....#",
        "....#....",
        ".........",
        "#........",
        "...#.....",
    ]
    y = 0
    for row in data:
        for x, c in enumerate(row):
            g.set((x, y), c)
        y += 1

    # g.print_layer()
    g.update_limits()
    # print(g.deltas)
    assert g.view((3, 4)) == "########"
    assert g.view((0, 0)) == "##"
