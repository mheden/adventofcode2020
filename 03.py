from utils import read_file
import math


def count_trees(map_, x, y, dx, dy):
    width = len(map_[0])
    height = len(map_)
    x = x % width
    if y >= height:
        return 0
    elif map_[y][x] == "#":
        return 1 + count_trees(map_, x + dx, y + dy, dx, dy)
    else:
        return 0 + count_trees(map_, x + dx, y + dy, dx, dy)


print("#--- Toboggan Trajectory: part1 ---#")

map_ = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]

assert count_trees(map_, 0, 0, 3, 1) == 7
print(count_trees(read_file("03.txt"), 0, 0, 3, 1))


print("#--- Toboggan Trajectory: part2 ---#")

deltas = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

assert math.prod([count_trees(map_, 0, 0, dx, dy) for dx, dy in deltas]) == 336

map_ = read_file("03.txt")
print(math.prod([count_trees(map_, 0, 0, dx, dy) for dx, dy in deltas]))
