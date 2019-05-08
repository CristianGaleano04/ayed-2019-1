from sys import stdin


def find_judge(N, trust):
    graph = {i: [] for i in range(1, N + 1)}
    for t in trust:
        graph[t[0]].append(t[1])
    for k in graph:
        if len(graph[k]) == 0:
            judge = k
            for person in graph:
                if person != judge and judge not in graph[person]:
                    return -1
            return judge
    return -1


if __name__ == '__main__':
    N = int(stdin.readline())
    trust = []
    while True:
        a = [int(c) for c in stdin.readline().strip().split()]
        if not a:
            break
        trust.append(a)
    print(find_judge(N, trust))
