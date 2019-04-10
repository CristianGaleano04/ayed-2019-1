import heapq
from sys import stdin


def ugly_number(n, up_list):
    uglies = [1]

    def gen_list(num):
        for i in uglies:
            yield i * num

    order = heapq.merge(*map(gen_list, up_list))
    while len(uglies) < n:
        ugly = next(order)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]


if __name__ == '__main__':
    x = int(stdin.readline())
    list_f = [int(c) for c in stdin.readline().strip().split()]
    print(ugly_number(x, list_f))
