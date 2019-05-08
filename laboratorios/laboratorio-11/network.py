from sys import stdin
from Others import Dijkstra_Graph


if __name__ == '__main__':
    n, m, k = [int(c) for c in stdin.readline().strip().split()]
    graph = Dijkstra_Graph.Graph()
    for j in range(m):
        nod, nod_t, cost = [int(c) for c in stdin.readline().strip().split()]
        graph.add_edge(nod, nod_t, cost)
    nodes = []
    cont = -1
    for c in range(1, n + 1):
        if c != k:
            nodes.append(c)
    for i in nodes:
        distance = graph.dijkstra(k, i)
        if not distance:
            print("-1")
            exit()
        else:
            cont = max(cont, distance)
    print(cont)
