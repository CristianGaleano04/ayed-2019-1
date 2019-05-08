from queue import Queue
from sys import stdin


def murder(n, s, neighbors):
    distances = [-1] * n
    unvisited = set(range(n))
    distances[s] = 0
    unvisited.remove(s)
    q = Queue()
    q.put(s)
    while not q.empty():
        cur = q.get()
        visited = set()
        for i in unvisited:
            if i not in neighbors[cur]:
                q.put(i)
                distances[i] = distances[cur] + 1
                visited.add(i)
        unvisited -= visited
        if len(unvisited) == 0:
            break
    dis_r = []
    for x in distances:
        if x != 0:
            dis_r.append(x)
    return dis_r


if __name__ == '__main__':
    res = []
    t = int(stdin.readline())
    for l in range(t):
        n, m = [int(x) for x in input().split()]
        neighbors = []
        for k in range(n):
            neighbors.append(set())
        for j in range(m):
            a, b = [int(x) - 1 for x in stdin.readline().split()]
            neighbors[a].add(b)
            neighbors[b].add(a)
        s = int(stdin.readline()) - 1
        res.append(murder(n, s, neighbors))
    for h in res:
        print(*h)
