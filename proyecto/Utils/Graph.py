from itertools import product


class Graph:
    def __init__(self, map):
        self.edges = {}
        self.starts = []
        self.exits = []
        self.graph = map
        for x, y in product(range(len(self.graph[0])), range(len(self.graph))):
            if self.graph[y][x] != "#":
                if self.graph[y][x] != "G":
                    self.edges[(x, y)] = []
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for key, d in product(self.edges.keys(), self.dirs):
            neighbour = (key[0] + d[0], key[1] + d[1])
            if neighbour in self.edges:
                self.edges[key].append(neighbour)
