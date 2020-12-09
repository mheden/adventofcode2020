from utils import read_file
from dag import DAG
import re

RE_CONTAIN = re.compile(r"^(\d+)\s(.+) bag")


def get_bags(data):
    dag = DAG()
    for line in data:
        bag, contains = line.split(" bags contain ")
        for c in contains.split(","):
            m = RE_CONTAIN.match(c.strip())
            if m:
                dag.add_edge(bag, m.group(2), int(m.group(1)))
    return dag


def part1(data, node):
    dag = get_bags(data)
    return len(dag.ancestors(node))


def part2(data, node):
    def weight_subtree(graph, node):
        weight = 1
        for successor in dag.successors(node):
            weight += dag.edge_weight(node, successor) * weight_subtree(dag, successor)
        return weight

    dag = get_bags(data)
    return weight_subtree(dag, node) - 1


print("#--- Handy Haversacks: part1 ---#")

data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()

assert part1(data, "shiny gold") == 4
print(part1(read_file("07.txt"), "shiny gold"))


print("#--- Handy Haversacks: part2 ---#")

assert part2(data, "shiny gold") == 32

data = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".splitlines()

assert part2(data, "shiny gold") == 126
print(part2(read_file("07.txt"), "shiny gold"))
