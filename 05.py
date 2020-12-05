from utils import read_file


def decode_seat(seat):
    xmin, xmax, dx = 0, 127, 64
    ymin, ymax, dy = 0, 7, 4
    for s in seat:
        if s == "F":
            xmax -= dx
            dx //= 2
        elif s == "B":
            xmin += dx
            dx //= 2
        elif s == "L":
            ymax -= dy
            dy //= 2
        elif s == "R":
            ymin += dy
            dy //= 2
    return xmin * 8 + ymin


print("#--- part1 ---#")

assert decode_seat("FBFBBFFRLR") == 357
assert decode_seat("BFFFBBFRRR") == 567
assert decode_seat("FFFBBBFRRR") == 119
assert decode_seat("BBFFBBFRLL") == 820

print(max([decode_seat(s) for s in read_file("05.txt")]))


print("#--- part2 ---#")

ids = sorted(set([decode_seat(s) for s in read_file("05.txt")]))
lastid = None
for id_ in ids:
    if lastid != None and id_ != lastid + 1:
        print(id_ - 1)
        exit
    lastid = id_