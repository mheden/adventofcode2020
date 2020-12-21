from utils import read_file, BIGNUM
from functools import reduce
import math


def part1(data):
    departure = int(data[0])
    min_ = {"bus": 0, "wait": BIGNUM}

    for bus in data[1].split(","):
        try:
            interval = int(bus)
            wait = math.ceil(departure / interval) * interval - departure
            if wait < min_["wait"]:
                min_["wait"] = wait
                min_["bus"] = interval
        except ValueError:
            pass
    return min_["bus"] * min_["wait"]


def get_intervals(data):
    intervals = []
    for x, interval in enumerate(data[1].split(",")):
        try:
            intervals.append((x, int(interval), 0))
        except ValueError:
            pass
    return intervals


def common_cycle(a, b):
    _, k_a, m_a = a
    dt_b, k_b, _ = b
    t = m_a
    while True:
        if (t + dt_b) % k_b == 0:
            return (0, k_a * k_b, t)
        t += k_a


def part2(data):
    intervals = get_intervals(data)
    return reduce(common_cycle, intervals)[2]


print("#--- Rain Risk: part1 ---#")

assert part1(["939", "7,13,x,x,59,x,31,19"]) == 295
print(part1(read_file("13.txt")))


print("#--- Rain Risk: part2 ---#")

assert part2(["n/a", "7,13,x,x,59,x,31,19"]) == 1068781
assert part2(["n/a", "17,x,13,19"]) == 3417
assert part2(["n/a", "67,7,59,61"]) == 754018
assert part2(["n/a", "67,x,7,59,61"]) == 779210
assert part2(["n/a", "67,7,x,59,61"]) == 1261476
assert part2(["n/a", "1789,37,47,1889"]) == 1202161486

print(part2(read_file("13.txt")))
