from utils import read_file


def run(program):
    seen = set()
    ip = 0
    acc = 0
    while True:
        if ip in seen:
            return ("hang", acc)
        seen.add(ip)
        try:
            op, arg = program[ip].split(" ")
        except IndexError:
            return ("done", acc)
        arg = int(arg)
        if op == "nop":
            ip += 1
        elif op == "acc":
            acc += arg
            ip += 1
        elif op == "jmp":
            ip += arg
        else:
            print("illegal instruction: %s" % op)
            exit()


def mutator(program):
    for i in range(len(program)):
        mutation = program.copy()
        if "nop" in mutation[i]:
            mutation[i] = mutation[i].replace("nop", "jmp")
        else:
            mutation[i] = mutation[i].replace("jmp", "nop")
        status, acc = run(mutation)
        if status == "done":
            return acc


print("#--- Handheld Halting: part1 ---#")

program = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]

assert run(program) == ("hang", 5)
print(run(read_file("08.txt"))[1])


print("#--- Handheld Halting: part2 ---#")

assert mutator(program) == 8
print(mutator(read_file("08.txt")))
