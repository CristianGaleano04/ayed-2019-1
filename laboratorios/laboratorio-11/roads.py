from collections import defaultdict
from collections import deque
from sys import stdin


class graph:
    def __init__(self):
        self.nodes = []
        self.edges = defaultdict(set)

    def clone(self):
        g = graph()
        g.nodes = self.nodes[:]
        for n in self.nodes:
            for e in self.edges[n]:
                g.edges[n].add(e)
        return g


def count_clusters(g):
    lust = 0
    used = set()
    c_size = []
    for node in g.nodes:
        if node in used:
            continue
        used.add(node)
        size = 1
        q = deque()
        q.appendleft(node)
        while q:
            cur = q.pop()
            for neigh in g.edges[cur]:
                if neigh in used:
                    continue
                used.add(neigh)
                q.appendleft(neigh)
                size += 1
        lust += 1
        c_size.append(size)
    return [lust, c_size]


if __name__ == '__main__':
    q = int(stdin.readline())
    for i in range(q):
        n, m, clib, road = [int(x) for x in stdin.readline().split()]
        edges = [[int(x) for x in stdin.readline().split()] for c in range(m)]
        if clib < road:
            print(clib * n)
            continue
        g = graph()
        g.nodes = range(1, n + 1)
        for a, b in edges:
            g.edges[a].add(b)
            g.edges[b].add(a)
        list_count = count_clusters(g)
        nc = list_count[0]
        cs = list_count[1]
        print(nc * clib + sum((x - 1) * road for x in cs))
