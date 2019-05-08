from sys import stdin


def visit_rooms(rooms):
    seen = [False] * len(rooms)
    seen[0] = True
    stack = [0]
    while stack:
        node = stack.pop()
        for i in rooms[node]:
            if not seen[i]:
                seen[i] = True
                stack.append(i)
    return all(seen)


if __name__ == '__main__':
    N = int(stdin.readline())
    a = []
    for i in range(N):
        a.append([int(c) for c in stdin.readline().strip().split()])
    print(visit_rooms(a))
