from sys import stdin
import collections


def boom(points):
    cnt = 0
    for a, i in enumerate(points):
        dis_list = []
        for b, k in enumerate(points[:a] + points[a + 1:]):
            dis_list.append((k[0] - i[0]) ** 2 + (k[1] - i[1]) ** 2)
        for z in collections.Counter(dis_list).values():
            if z > 1:
                cnt += z * (z - 1)
    return cnt


if __name__ == '__main__':
    while True:
        x = int(stdin.readline())
        if not x:
            break
        points = []
        for i in range(x):
            points.append([int(c) for c in stdin.readline().strip().split()])
        print(boom(points))
