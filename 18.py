from utils import read_file


class I1:
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        return self.__class__(self.value + other.value)

    def __sub__(self, other):
        return self.__class__(self.value * other.value)


class I2:
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        return self.__class__(self.value * other.value)

    def __mul__(self, other):
        return self.__class__(self.value + other.value)


def tokenize(expression):
    return (
        expression.replace("(", " ( ")
        .replace(")", " ) ")
        .replace("  ", " ")
        .strip()
        .split(" ")
    )


def calculate_part1(expression):
    expr = []
    for token in tokenize(expression):
        if token in "+()":
            expr.append(token)
        elif token in "*":
            expr.append("-")
        else:
            expr.append("I1(%s)" % token)
    return eval(" ".join(expr)).value


def calculate_part2(expression):
    expr = []
    for token in tokenize(expression):
        if token in "()":
            expr.append(token)
        elif token in "*":
            expr.append("+")
        elif token in "+":
            expr.append("*")
        else:
            expr.append("I2(%s)" % token)
    return eval(" ".join(expr)).value


print("#--- Operation Order: part1 ---#")


def part1(rows):
    return sum(calculate_part1(row) for row in rows)


assert calculate_part1("1 + 2 * 3 + 4 * 5 + 6") == 71
assert calculate_part1("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert calculate_part1("2 * 3 + (4 * 5)") == 26
assert calculate_part1("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
assert calculate_part1("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
assert calculate_part1("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
print(part1(read_file("18.txt")))


print("#--- Operation Order: part2 ---#")


def part2(rows):
    return sum(calculate_part2(row) for row in rows)


assert calculate_part2("1 + 2 * 3 + 4 * 5 + 6") == 231
assert calculate_part2("1 + (2 * 3) + (4 * (5 + 6))") == 51
assert calculate_part2("2 * 3 + (4 * 5)") == 46
assert calculate_part2("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
assert calculate_part2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
assert calculate_part2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340
print(part2(read_file("18.txt")))
