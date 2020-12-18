from collections import deque


class DAG:
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()

    def add_edge(self, from_, to_, weight=1):
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

    def descendants_pre(self, root):
        def _path(root):
            res = [root]
            for successor in sorted(self.successors(root)):
                res += _path(successor)
            return res
        return _path(root)


    def descendants_post(self, root):
        def _path(root):
            res = []
            for successor in sorted(self.successors(root)):
                res += _path(successor)
            return res + [root]
        return _path(root)

    def pathsfrom(self, from_):
        def _pathsfrom(from_, path):
            path.append(from_)

            if len(self.successors(from_)) == 0:
                paths.append(tuple(path))

            for successor in sorted(self.successors(from_)):
                _pathsfrom(successor, path)
            path.pop()

        paths = []
        path = deque()
        _pathsfrom(from_, path)
        return paths

    def pathsfromto(self, from_, to_):
        def _pathsfrom(from_, to_, path):
            path.append(from_)

            if len(self.successors(from_)) == 0:
                if from_ == to_:
                    paths.append(tuple(path))

            for successor in sorted(self.successors(from_)):
                _pathsfrom(successor, to_, path)
            path.pop()

        paths = []
        path = deque()
        _pathsfrom(from_, to_, path)
        return paths


if __name__ == "__main__":
    dag = DAG()
    dag.add_edge('a', 'aa')
    dag.add_edge('a', 'ab')
    dag.add_edge('aa', 'aaa')
    dag.add_edge('ab', 'aaab')
    dag.add_edge('aaa', 'aaaa')
    dag.add_edge('aaa', 'aaab')
    dag.add_edge('ab', 'aba')
    dag.dump()

    # print(dag.descendants_pre('a'))
    # print(dag.descendants_post('a'))

    # print(dag.pathsfrom('a'))
    # print(dag.pathsfrom('aaa'))

    print(dag.pathsfromto('a', 'aaab'))