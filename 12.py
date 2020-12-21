from utils import read_file, manhattan_distance
from ant import Ant


def part1(instructions):
    ship = Ant(0, 0, heading=0)
    for ins in instructions:
        i, value = ins[0], int(ins[1:])
        if i == "F":
            ship.forward(value)
        elif i == "N":
            ship.north(value)
        elif i == "S":
            ship.south(value)
        elif i == "E":
            ship.east(value)
        elif i == "W":
            ship.west(value)
        elif i == "L":
            ship.turn(value)
        elif i == "R":
            ship.turn(-value)
    return manhattan_distance((0, 0), ship.pos())


def part2(instructions):
    ship = Ant(0, 0, 90)
    waypoint = Ant(10, 1)
    for ins in instructions:
        i, value = ins[0], int(ins[1:])
        if i == "F":
            x, y = waypoint.pos()
            ship.x += value * x
            ship.y += value * y
        elif i == "N":
            waypoint.north(value)
        elif i == "S":
            waypoint.south(value)
        elif i == "E":
            waypoint.east(value)
        elif i == "W":
            waypoint.west(value)
        elif i in "LR":
            dist = waypoint.dist()
            angle = waypoint.angle()
            waypoint.x = 0
            waypoint.y = 0
            if i == "L":
                waypoint.heading = angle + value
            else:
                waypoint.heading = angle - value
            waypoint.forward(dist)
    return manhattan_distance((0, 0), ship.pos())


print("#--- Rain Risk: part1 ---#")

instructions = """F10
N3
F7
R90
F11""".splitlines()

assert part1(instructions) == 25
print(part1(read_file("12.txt")))


print("#--- Rain Risk: part2 ---#")

assert part2(instructions) == 286
print(part2(read_file("12.txt")))
