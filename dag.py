class DAG:
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    def add_edge(self, from_, to_, weight):
        for node in [from_, to_]:
            if node not in self.nodes:
                self.nodes[node] = {"pre": set(), "suc": set()}
        self.nodes[from_]["suc"].add(to_)
        self.nodes[to_]["pre"].add(from_)
        self.edges[(from_, to_)] = weight

    def dump(self):
        for node in self.nodes:
            print(
                "Node(%s, p:%s s:%s)"
                % (node, self.nodes[node]["pre"], self.nodes[node]["suc"])
            )

    def edge_weight(self, from_, to_):
        return self.edges[(from_, to_)]

    def predecessors(self, node):
        return self.nodes[node]["pre"]

    def successors(self, node):
        return self.nodes[node]["suc"]

    def ancestors(self, node):
        def get_ancestors(nodes):
            a = set()
            for node in nodes:
                a |= set(self.predecessors(node))
            return a

        len_ = 0
        result = set(self.predecessors(node))
        while len(result) != len_:
            len_ = len(result)
            updated = get_ancestors(result)
            result |= updated
        return result
