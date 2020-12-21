from utils import read_file
from itertools import product
import re

RE_MEM = re.compile(r"mem\[(\d+)\] = (\d+)")
RE_MASK = re.compile(r"mask = (\w+)")


def part1(data):
    mem = {}
    setbits = 0
    clearbits = 0

    for row in data:
        m = RE_MASK.search(row)
        if m:
            setbits = 0
            clearbits = 0
            mask = m.group(1)
            for i, c in enumerate(reversed(mask)):
                if c == "0":
                    clearbits |= 1 << i
                elif c == "1":
                    setbits |= 1 << i
            clearbits = 2 ** 36 - clearbits - 1
        m = RE_MEM.search(row)
        if m:
            addr, value = int(m.group(1)), int(m.group(2))
            mem[addr] = (value | setbits) & clearbits
    return sum(mem.values())


def part2(data):
    def replacer(ss, values):
        res = ""
        for s in ss:
            if s in "X":
                res += str(values.pop(0))
            else:
                res += s
        return res

    mem = {}
    for row in data:
        m = RE_MASK.search(row)
        if m:
            mask = m.group(1)
        m = RE_MEM.search(row)
        if m:
            addr, value = format(int(m.group(1)), "036b"), int(m.group(2))
            rmask = ""
            for a, m in zip(addr, mask):
                if m == "0":
                    rmask += a
                elif m == "1":
                    rmask += "1"
                else:
                    rmask += "X"
            raddrs = []
            for bits in product((0, 1), repeat=rmask.count("X")):
                raddrs.append(replacer(rmask, list(bits)))
            for address in raddrs:
                mem[int(address, 2)] = value
    return sum(mem.values())


print("#--- Docking Data: part1 ---#")

data = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0",
]
assert part1(data) == 165
print(part1(read_file("14.txt")))


print("#--- Docking Data: part2 ---#")

data = [
    "mask = 000000000000000000000000000000X1001X",
    "mem[42] = 100",
    "mask = 00000000000000000000000000000000X0XX",
    "mem[26] = 1",
]

assert part2(data) == 208
print(part2(read_file("14.txt")))
