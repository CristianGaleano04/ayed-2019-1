from sys import stdin
from Others.Undirected_Graph import graph


if __name__ == '__main__':
    q = int(stdin.readline())
    r_final = []
    for i in range(q):
        n, m = [int(x) for x in stdin.readline().split()]
        g = graph(n, m)
        start = int(stdin.readline().strip())
        r_final.append(g.answer(start, n))
    for i in r_final:
        print(*i)
