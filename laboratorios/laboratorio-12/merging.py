from sys import stdin
from Others.Disjoint import Disjoint


if __name__ == '__main__':
    num = [int(c) for c in stdin.readline().split()]
    n = num[0]
    q = num[1]
    ds = Disjoint()
    for i in range(n):
        ds.make_set(i + 1)
    for i in range(q):
        arguments = list(stdin.readline().split())
        op = arguments[0]
        args = arguments[1:]
        args = list(map(int, args))
        if op == 'Q':
            print(ds.get_size(args[0]))
        elif op == 'M':
            ds.union(args[0], args[1])
